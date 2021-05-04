from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.settings import SERVER_EMAIL
from users.serializers import (UserAuthSerializer, UserConfirmationSerializer,
                               UserSerializer)

User = get_user_model()


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_confirmation_code(request):
    serializer = UserAuthSerializer(data=request.data)
    if serializer.is_valid():
        username = serializer.validated_data['username']
        email = serializer.validated_data['email']
        user, created = User.objects.get_or_create(username=username,
                                                   email=email)
        confirmation_code = User.objects.make_random_password()
        user.confirmation_code = confirmation_code
        user.save()
        send_mail('Confirmation', f'Your code: {user.confirmation_code}',
                  SERVER_EMAIL, [email])
        if created:
            return Response({'Success registration data': serializer.data},
                            status.HTTP_201_CREATED)
        return Response({'Success registration data': serializer.data,
                         'confirmation_code': confirmation_code},
                        status=status.HTTP_200_OK)
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    serializer = UserConfirmationSerializer(data=request.data)
    if serializer.is_valid():
        confirmation_code = serializer.validated_data['confirmation_code']
        email = serializer.validated_data['email']
        username = serializer.validated_data['username']
        user = get_object_or_404(User, email=email, username=username,
                                 confirmation_code=confirmation_code)
        token = AccessToken.for_user(user)
        user.confirmation_code = ''
        user.save()

        return Response({'token': str(token)}, status=status.HTTP_200_OK)
    return Response(serializer.errors)




