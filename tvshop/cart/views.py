from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from items.models import Tv


class CartView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = self.request.session.get('cart')

        if cart:
            items_cart = Tv.objects.filter(pk__in=cart)
            #  Считаем общую цену
            total = 0
            for item in items_cart:
                total += cart[str(item.pk)]['quantity'] * item.get_value()

            context['items_cart'] = items_cart
            context['quantity_cart'] = len(items_cart)
            context['total_cart'] = total

        context['title'] = "Корзина"

        return context


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


class RemoveOneItemFromCart(View):

    @staticmethod
    def post(request, id_item):
        cart = request.session.get('cart', {})
        id_item = str(id_item)

        cart[id_item]['quantity'] -= 1

        if cart[id_item]['quantity'] < 1:
            del cart[id_item]

        request.session['cart'] = cart

        return redirect(request.POST.get('url_from'))


class RemoveFromCart(View):

    @staticmethod
    def post(request, id_item):
        cart = request.session.get('cart')

        id_item = str(id_item)
        del cart[id_item]

        request.session['cart'] = cart

        return redirect(request.POST.get('url_from'))


