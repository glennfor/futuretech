from django.urls import path
from .views import index, show_profile
from users.views import register, signin, signout, signup

urlpatterns = [
    path('', index, name="Home"),
    path('home/', index),
    path('register/', register, name="Register"),
    path('accounts/login/', signin),
    path('accounts/logout/', signout),
    path('accounts/signup/', signup),
    path('user/profile', show_profile),
]
