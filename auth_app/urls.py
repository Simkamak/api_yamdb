from django.urls import path, include
from . import views


urlpatterns = [
    path('v1/auth/email/', views.get_confirmation_code),
    path('v1/auth/token/', views.get_token),

]