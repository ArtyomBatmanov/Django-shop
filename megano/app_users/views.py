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
            profile = Profile.objects.create(user=user)
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
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request):
        new_avatar = request.FILES["avatar"]
        user = request.user.pk
        profile = Profile.objects.get(user_id=user)
        avatar, created = Avatar.objects.get_or_create(src=profile.pk)

        if str(new_avatar).endswith(('.png', '.jpg', '.jpeg')):
            avatar.image = new_avatar
            avatar.save()
        else:
            return Response('Wrong file format', status=status.HTTP_400_BAD_REQUEST)
        return Response('Update successful', status=status.HTTP_200_OK)


# class ChangePasswordView(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#
#     def post(self, request):
#         user = request.user
#         current_password = request.data.get('current_password')
#         new_password = request.data.get('new_password')
#
#         if not current_password or not new_password:
#             return Response({"message": "Both current and new passwords must be provided."},
#                             status=status.HTTP_400_BAD_REQUEST)
#
#         if not user.check_password(current_password):
#             return Response({"message": "Current password is not correct"}, status=status.HTTP_400_BAD_REQUEST)
#
#         user.set_password(new_password)
#         user.save()
#
#         return Response({'message': 'Password changed successfully'})


class PasswordUpdateView(GenericAPIView, UpdateModelMixin):
    serializer_class = PasswordChangeSerializer

    def get_object(self):
        return self.request.user

    def post(self, *args, **kwargs):
        return self.update(self.request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            if not self.object.check_password(serializer.data.get("passwordCurrent")):
                return Response({"passwordCurrent": ["Wrong password"]}, status=status.HTTP_400_BAD_REQUEST)

            elif not serializer.data.get("password") == serializer.data.get("passwordReply"):
                return Response({'password': ['Passwords must match']}, status=status.HTTP_400_BAD_REQUEST)

            self.object.set_password(serializer.data.get('passwordReply'))
            self.object.save()
            return Response('Update successful', status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.
