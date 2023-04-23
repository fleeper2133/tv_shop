from django.urls import path
from .views import *

urlpatterns = [
    path('', ItemList.as_view(), name="home"),
    path('models/<slug:model_slug>', ItemList.as_view(), name='model'),
    path('tv/<int:pk>', ItemDetail.as_view(), name='detail')
]