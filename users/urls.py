from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register('v1/users/', views.CustomUserViewSet)

urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/auth/email/', views.get_confirmation_code),
    path('v1/auth/token/', views.get_token),

]