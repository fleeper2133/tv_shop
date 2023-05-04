from django.shortcuts import render, redirect
from django.views import View


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


