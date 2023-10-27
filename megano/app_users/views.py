from rest_framework import status, permissions
from django.urls import reverse_lazy
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, AvatarSerializer, PasswordChangeSerializer
from django.contrib.auth.views import LogoutView
from .models import Profile, Avatar
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
import json


class SignUpView(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        name = user_data.get("name")
        username = user_data.get("username")
        password = user_data.get("password")

        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = name
            user.save()
            profile = Profile.objects.create(user=user, first_name=name)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignInView(APIView):

    def post(self, request):
        user_data = json.loads(request.body)
        username = user_data.get("username")
        password = user_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AuthView(APIView):
    def post(self, request):
        data = json.loads(list(request.data.keys())[0])
        username = data.get('username')
        password = data.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
        else:
            return Response('Invalid credentials', status=status.HTTP_401_UNAUTHORIZED)

        return Response('Authentication successful', status=status.HTTP_200_OK)


class UserLogoutView(LogoutView):
    next_page = reverse_lazy('app_users:sign-in')


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AvatarUpdateView(APIView):
    def post(self, request: Request):
        new_avatar = request.data.get('avatar')
        user = request.user.pk
        profile = Profile.objects.get(user_id=user)
        avatar, created = Avatar.objects.get_or_create(profile_id=profile.pk)

        if str(new_avatar).endswith(('.png', '.jpg', '.jpeg')):
            avatar.image = new_avatar
            avatar.save()
        else:
            return Response('Wrong file format', status=status.HTTP_400_BAD_REQUEST)
        return Response('Update successful', status=status.HTTP_200_OK)


class ChangePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        if not user.check_password(current_password):
            return Response({'error': 'Invalid current password'}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({'message': 'Password changed  successfully'})
# Create your views here.
