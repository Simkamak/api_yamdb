from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews',
                views.ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet, basename='comments')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]