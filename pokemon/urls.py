from django.urls import path

from pokemon.views.auth import (RegisterView, 
                                LogInView, 
                                LogOutView)
from pokemon.views.base_view import BaseView, MyProfileView

urlpatterns = [
    path("", BaseView.as_view(), name="home"),
    path("my/profile/<int:user>/", MyProfileView.as_view(), name='profile'),

    path("signup/user/", RegisterView.as_view(), name='signup'),
    path("login/user/", LogInView.as_view(), name="login"),
    path("logout/user/", LogOutView.as_view(), name="logout")
]