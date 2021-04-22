from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
import uuid
from django.core.mail import send_mail
from .serializers import RegistrationSerializer
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


@api_view(['POST'])
#@permission_classes(AllowAny)
def get_confirmation_code(request):
    email = request.data['email']
    confirmation_code = uuid.uuid3(uuid.NAMESPACE_DNS, email)
    updated, created = User.objects.update_or_create(username=email, email=email, defaults={'password': confirmation_code})
    if created:
        send_mail('Confirmation', f'Your code: {confirmation_code}',
                      'admin@admin.ru', [request.data['email']])
        data = {
            'email': email,
            'confirmation_code': confirmation_code
                }

        serializer = RegistrationSerializer(
                data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(f'You are already signed in', status=status.HTTP_200_OK)


@api_view(['POST'])
#@permission_classes(AllowAny)
def get_token(request):
    try:
        email = request.data['email']
        confirmation_code = request.data['confirmation_code']
        user = get_object_or_404(User, email=email,
                                 confirmation_code=confirmation_code)
        refresh = AccessToken.for_user(user)

        return Response({'access': str(refresh)}, status=status.HTTP_200_OK)
    except:
        return Response(status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def api_users(request):
    users = User.objects.all()
    role_admin = request.user.has_perm('admin')
    serializer = RegistrationSerializer(users, many=True)

