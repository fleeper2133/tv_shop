from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='reg'),
]