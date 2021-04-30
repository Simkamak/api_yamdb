from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views
from .user_auth.views import get_confirmation_code, get_token

router_v1 = DefaultRouter()

router_v1.register('', views.UserList)

urlpatterns = [

    path('v1/users/', include(router_v1.urls)),
    path('v1/auth/email/', get_confirmation_code),
    path('v1/auth/token/', get_token),

]
