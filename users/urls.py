from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register('', views.UserList)

urlpatterns = [
    path('me/', views.UserDetailAPIView.as_view()),
    path('', include(router_v1.urls)),

]