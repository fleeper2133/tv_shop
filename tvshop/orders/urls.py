from django.urls import path
from .views import *


urlpatterns = [
    path('', CreateOrder.as_view(), name="create_order")
]
