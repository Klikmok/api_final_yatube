from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (
    PostViewSet,
    GroupViewSet,
    CommentViewSet,
    FollowViewSet
)

# Здесь прописываем все вьюсеты. Не вьюсеты оставляем в path.
router = DefaultRouter()
router.register(
    r'^posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='detail'
)
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet, basename='following')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
