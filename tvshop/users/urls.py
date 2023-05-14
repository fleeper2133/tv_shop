from django.urls import path, include
from .views import *

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
    path('registration/', UserRegistrationView.as_view(), name='reg'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/update', UserProfileUpdate.as_view(), name='profile_update')
]