from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register('v1/users', views.UserList)

urlpatterns = [
    path('', include(router_v1.urls)),

]