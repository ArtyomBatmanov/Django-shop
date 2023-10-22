from django.contrib import admin
from django.urls import path
from django.urls import path, include
from .views import AuthView, LogoutView, SignUpView, AvatarUpdateView, ProfileDetailView, PasswordUpdateView

urlpatterns = [
    path('api/sign-up/', SignUpView.as_view(), name='sign-up'),
    path('api/sign-out/', LogoutView.as_view(), name='sign-out'),
    path('api/sign-in/', AuthView.as_view(), name='login'),
    path('api/profile/', ProfileDetailView.as_view(), name='profile'),
    path('api/profile/avatar/', AvatarUpdateView.as_view(), name='avatar'),
    path('api/profile/password/', PasswordUpdateView.as_view(), name='password'),

]
