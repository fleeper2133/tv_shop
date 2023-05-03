from django.shortcuts import render, redirect


def add_in_cart(request, id_item):

    if request.POST:
        cart = request.session.get('cart', {})

        id_item = str(id_item)
        if id_item not in cart:
            cart[id_item] = {'quantity': 1}
        else:
            cart[id_item]['quantity'] += 1

        request.session['cart'] = cart

        return redirect(request.POST.get('url_from'))


