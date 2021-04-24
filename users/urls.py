from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()

router_v1.register('', views.UserList)

urlpatterns = [
    path('me/', views.UserDetailAPIView.as_view()),
    path('', include(router_v1.urls)),

]