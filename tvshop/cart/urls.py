from django.urls import path
from .views import *

app_name = 'cart'

urlpatterns = [
    path('', CartOrderView.as_view(), name="view"),
    path('add/<int:id_item>', AddInCart.as_view(), name="add"),
    path('remove/<int:id_item>', RemoveFromCart.as_view(), name="remove"),
    path('minus', RemoveOneItemFromCart.as_view(), name='minus'),
    path('plus', PlusOne.as_view(), name='plus'),
]
