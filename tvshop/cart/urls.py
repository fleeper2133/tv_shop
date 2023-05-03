from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('add/<int:id_item>', AddInCart.as_view(), name="add"),
    path('remove/<int:id_item>', RemoveFromCart.as_view(), name="remove")
]
