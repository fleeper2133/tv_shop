from django.contrib import admin

from orders.models import Order, OrderTV


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_email', 'customer_address', 'note', 'time_create')


@admin.register(OrderTV)
class OrderTvAdmin(admin.ModelAdmin):
    list_display = ('order', 'tv', 'quantity')
