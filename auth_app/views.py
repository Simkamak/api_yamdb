from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail, BadHeaderError
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_confirmation_code(request):
    email = request.data['email']
    user = get_object_or_404(User, email=email)
    confirmation_code = User.objects.make_random_password()
    user.confirmation_code = confirmation_code
    user.save()
    try:
        send_mail('Confirmation', f'Your code: {confirmation_code}',
                  'admin@admin.ru', [email])
        return Response({'email': confirmation_code},
                        status=status.HTTP_200_OK)
    except BadHeaderError:
        return Response({'errors': 'incorrect e-mail {}'.format(email)},
                        status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def get_token(request):
    try:
        email = request.data['email']
        confirmation_code = request.data['confirmation_code']
        user = get_object_or_404(User, email=email,
                                 confirmation_code=confirmation_code)
        token = AccessToken.for_user(user)
        user.confirmation_code = ''
        user.save()
        return Response({'token': str(token)}, status=status.HTTP_200_OK)
    except BadHeaderError:
        return Response({}, status.HTTP_400_BAD_REQUEST)








