from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import SignInView, LogoutView, SignUpView, ProfileView, AvatarUpdateView, PasswordUpdateView

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='register'),
    path('sign-out/', LogoutView.as_view(), name='sign-out'),
    path("sign-in/", SignInView.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/avatar/', AvatarUpdateView.as_view(), name='avatar'),
    path('profile/password/', PasswordUpdateView.as_view(), name='password'),

]
