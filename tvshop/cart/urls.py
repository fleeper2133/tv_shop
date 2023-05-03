from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('add/<int:id_item>', add_in_cart, name="add"),
    path('remove/<int:id_item>', remove_from_cart, name="remove")
]
