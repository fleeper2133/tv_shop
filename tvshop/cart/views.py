from django.contrib.auth import login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from items.models import Tv
from users.forms import CustomUserChangeForm, CustomUserCreationForm
from users.models import CustomUser
from orders.forms import *
from orders.models import OrderTV
from .utils import is_ajax


class CartOrderView(View):
    template_name = 'cart/cart.html'

    @staticmethod
    def get_context_data(request, context=None):
        if context is None:
            context = {}
        cart = request.session.get('cart')
        if request.user.is_authenticated:
            address = AddressUser.objects.filter(user_id=request.user.pk)
        else:
            address = None

        if cart:
            items_cart = Tv.objects.filter(pk__in=cart)
            #  Считаем общую цену
            total = 0
            for item in items_cart:
                total += cart[str(item.pk)]['quantity'] * item.get_value()

            context['items_cart'] = items_cart
            context['quantity_cart'] = len(items_cart)
            context['total_cart'] = total

        if address:
            context['address_form'] = AddressCustomerForm(instance=address[0])
        else:
            context['address_form'] = AddressCustomerForm

        if request.user.is_authenticated:
            context['order_form'] = OrderForm(initial={
                'customer_first_name': request.user.first_name,
                'customer_last_name': request.user.last_name,
                'customer_phone': request.user.phone,

            })
        else:
            context['order_form'] = OrderForm
        context['title'] = "Корзина"
        return context

    @staticmethod
    def __data_for_update_user(request):
        data = {
            'first_name': request.POST.get('customer_first_name'),
            'last_name': request.POST.get('customer_last_name'),
            'phone': request.POST.get('customer_phone')
        }
        return data

    @staticmethod
    def __create_order_tv(cart: dict, order: Order) -> None:
        for i in cart:
            OrderTV.objects.create(order_id=order.pk, tv_id=i, quantity=cart[i]['quantity'])

    def get(self, request):
        context = self.get_context_data(request)
        return render(request, self.template_name, context)

    def post(self, request):
        context = self.get_context_data(request)
        cart = request.session.get('cart', {})

        if cart == {}:
            error_no_items = '<h4 style="color: red;">Добавьте товары чтобы совершить покупку!</h3>'
            context['error_no_items'] = error_no_items

        else:

            if request.user.is_authenticated:  # Если пользователь зарегистрирован
                copy_request = request.POST.copy()
                copy_request['customer_email'] = request.user.email
                order_form = OrderForm(copy_request)

                address = AddressUser.objects.get(user_id=request.user.pk)
                custom_user = CustomUser.objects.get(pk=request.user.pk)
                update_account = request.POST.get("update_account")

                if update_account == 'Yes':
                    address_form = AddressCustomerForm(request.POST, instance=address)

                    data = self.__data_for_update_user(request)
                    custom_user_form = CustomUserChangeForm(data, instance=custom_user)

                    if address_form.is_valid() and custom_user_form.is_valid() and order_form.is_valid():
                        address_form.save()
                        custom_user_form.save()

                else:
                    address_form = AddressCustomerForm(request.POST)

                    if not (address.street == address_form.data.get('street') and
                            str(address.corpus) == address_form.data.get('corpus') and
                            str(address.house) == address_form.data.get('house') and
                            str(address.flat) == address_form.data.get('flat') and
                            address.city == address_form.data.get('city') and
                            address.country == address_form.data.get('country') and
                            address.postcode == address_form.data.get('postcode')):
                        if address_form.is_valid():
                            address = address_form.save()

                if order_form.is_valid() and address_form.is_valid():
                    order = order_form.save(commit=False)
                    order.customer_address_id = address.pk
                    if request.user.is_authenticated:
                        order.customer_user_id = custom_user.pk
                    order.save()

                    self.__create_order_tv(cart, order)
                    request.session['cart'] = {}
                    context['items_cart'] = {}

                else:
                    context['order_form'] = order_form
                    context['address_form'] = address_form

            else:  # Если пользователь не зарегистрирован
                create_account = request.POST.get('create_account')
                address_form = AddressCustomerForm(request.POST)
                order_form = OrderForm(request.POST)

                if create_account == 'Yes':
                    copy_request = request.POST.copy()
                    email = request.POST.get('customer_email')
                    copy_request['email'] = email
                    create_user = CustomUserCreationForm(copy_request)

                    data = self.__data_for_update_user(request)
                    update_user = CustomUserChangeForm(data)

                    if create_user.is_valid() and address_form.is_valid() \
                            and order_form.is_valid() and update_user.is_valid():

                        user = create_user.save()
                        update_user = CustomUserChangeForm(data, instance=user)
                        update_user.save()

                        custom_address = AddressUser.objects.get(user_id=user.pk)
                        address_form = AddressCustomerForm(request.POST, instance=custom_address)
                        address = address_form.save()

                        order = order_form.save(commit=False)
                        order.customer_address_id = address.pk
                        order.customer_user_id = user.pk
                        order.save()

                        self.__create_order_tv(cart, order)
                        request.session['cart'] = {}
                        context['items_cart'] = {}
                        login(request, user)
                    else:
                        context['user_form'] = create_user
                        context['order_form'] = order_form
                        context['address_form'] = address_form
                        context['update_form'] = update_user
                        context['checked'] = 'checked'

                else:
                    if address_form.is_valid() and order_form.is_valid():
                        address = address_form.save()
                        order = order_form.save(commit=False)
                        order.customer_address_id = address.pk
                        order.save()

                        self.__create_order_tv(cart, order)
                        request.session['cart'] = {}
                        context['items_cart'] = {}

        return render(request, self.template_name, context)


class AddInCart(View):

    @staticmethod
    def post(request, id_item):
        cart = request.session.get('cart', {})

        id_item = str(id_item)
        if id_item not in cart:
            cart[id_item] = {'quantity': 1}
        else:
            cart[id_item]['quantity'] += 1

        request.session['cart'] = cart

        return redirect(request.POST.get('url_from'))


def plus_minus_item_to_cart(request, plus_or_minus: str):  # plus_or_minus = + or -
    if is_ajax(request):
        cart = request.session.get('cart', {})
        id_item = request.POST.get('id')
        item = Tv.objects.get(pk=id_item)
        items_cart = Tv.objects.filter(pk__in=cart)

        if id_item in cart:

            if plus_or_minus == '-' and cart[id_item]['quantity'] > 1:
                cart[id_item]['quantity'] -= 1
            elif plus_or_minus == '+':
                cart[id_item]['quantity'] += 1

            request.session['cart'] = cart

            value = item.get_value()

            #  Считаем общую цену
            total = 0
            for item in items_cart:
                total += cart[str(item.pk)]['quantity'] * item.get_value()

            data = {
                "id": id_item,
                'quantity': cart[id_item]['quantity'],
                'value': value * int(cart[id_item]['quantity']),
                'total': total

            }
            return data


class PlusOne(View):

    @staticmethod
    def post(request):
        data = plus_minus_item_to_cart(request, '+')
        return JsonResponse(data, status=200)


class RemoveOneItemFromCart(View):

    @staticmethod
    def post(request):
        data = plus_minus_item_to_cart(request, '-')
        return JsonResponse(data, status=200)


class RemoveFromCart(View):

    @staticmethod
    def post(request, id_item):
        cart = request.session.get('cart')

        id_item = str(id_item)
        del cart[id_item]

        request.session['cart'] = cart

        return redirect(request.POST.get('url_from'))
