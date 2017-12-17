from django.urls import path
from .views import register, user_profile
from django.contrib.auth.views import login

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', user_profile, name='profile'),
]