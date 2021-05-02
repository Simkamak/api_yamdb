from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from api_yamdb.settings import SERVER_EMAIL

User = get_user_model()


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_confirmation_code(request):
    try:
        email = request.data['email']
        username = request.data['username']
        user = get_object_or_404(User, email=email, username=username)
        confirmation_code = User.objects.make_random_password()
        user.confirmation_code = confirmation_code
        user.save()
        send_mail('Confirmation', f'Your code: {confirmation_code}',
                  SERVER_EMAIL, [email])
        return Response({'email': confirmation_code, 'username': username},
                        status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'errors': str(e)},
                        status.HTTP_203_NON_AUTHORITATIVE_INFORMATION)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    try:
        email = request.data['email']
        confirmation_code = request.data['confirmation_code']
        if confirmation_code != '':
            user = get_object_or_404(
                User, email=email, confirmation_code=confirmation_code
                )
            token = AccessToken.for_user(user)
            user.confirmation_code = ''
            user.save()
            return Response({'token': str(token)}, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Confirmation_code  is required.'},
                status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
            )

    except Exception as e:
        return Response(
            {'error': str(e)}, status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
        )
