from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'titles/(?P<title_id>\d+)/reviews', views.ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    views.CommentViewSet, basename='comments')
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'titles', views.TitleViewSet, basename='titles')
router.register(r'genres', views.GenreViewSet, basename='genres')

urlpatterns = [
    path('v1/', include(router.urls)),
]
