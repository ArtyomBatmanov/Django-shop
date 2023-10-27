from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import AuthView, LogoutView, SignUpView, ProfileView, AvatarUpdateView, ChangePasswordView

urlpatterns = [
    path('api/sign-up', SignUpView.as_view(), name='sign-up'),
    path('api/sign-out', LogoutView.as_view(), name='sign-out'),
    path('api/sign-in', AuthView.as_view(), name='login'),
    path('api/profile', ProfileView.as_view(), name='profile'),
    path('api/profile/avatar', AvatarUpdateView.as_view(), name='avatar'),
    path('api/profile/password', ChangePasswordView.as_view(), name='password'),

]
