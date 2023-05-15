from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from users.models import CustomUser
from users.forms import CustomUserChangeForm


class CreateOrder(View):

    def post(self, request):

        address = AddressUser.objects.filter(user_id=self.request.user.pk)
        address = address[0]
        custom_user = CustomUser.objects.get(pk=self.request.user.pk)

        update_account = request.POST.get("update_account")

        if update_account == 'Yes':
            address_form = AddressCustomerForm(request.POST, instance=address)

            customer_first_name = request.POST.get('customer_first_name')
            customer_last_name = request.POST.get('customer_last_name')
            customer_phone = request.POST.get('customer_phone')
            data = {
                'first_name': customer_first_name,
                'last_name': customer_last_name,
                'phone': customer_phone,
            }
            custom_user_form = CustomUserChangeForm(data, instance=custom_user)

            if address_form.is_valid() and custom_user_form.is_valid():
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

        copy_request = request.POST.copy()
        copy_request['customer_email'] = request.user.email
        order_form = OrderForm(copy_request)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.customer_address_id = address.pk
            order.customer_user_id = custom_user.pk
            order.save()
        else:
            print(order_form)

        return redirect("cart:view")
