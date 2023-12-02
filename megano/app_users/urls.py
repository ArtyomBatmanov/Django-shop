from django.urls import path
from .views import (SignUpView, UserLogoutView, AuthView,
                    ProfileDetail, AvatarUpdateView, PasswordUpdateView)

urlpatterns = [
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-out/', UserLogoutView.as_view(), name='sign-out'),
    path('sign-in/', AuthView.as_view(), name='login'),
    path('profile/', ProfileDetail.as_view(), name='profile'),
    path('profile/avatar/', AvatarUpdateView.as_view(), name='avatar'),
    path('profile/password/', PasswordUpdateView.as_view(), name='password'),

]