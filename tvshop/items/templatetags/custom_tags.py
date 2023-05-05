from django.template.defaulttags import register
from items.models import Tv


@register.inclusion_tag('cart/menu_cart.html', takes_context=True)
def cart(context):
    cart = context['request'].session.get('cart')

    if cart:
        items_cart = Tv.objects.filter(pk__in=cart)
        #  Считаем общую цену
        total = 0
        for item in items_cart:
            total += cart[str(item.pk)]['quantity'] * item.get_value()

        data = {
            'items_cart': items_cart,
            'quantity_cart': len(items_cart),
            'total_cart': total,
            'request': context['request']
        }

        return data