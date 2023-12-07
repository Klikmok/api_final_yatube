from rest_framework.routers import DefaultRouter
from django.urls import include, path

from .views import (
    PostViewSet, GroupViewSet, CommentListCreate, CommentDetail, FollowViewSet
)

router = DefaultRouter()
router.register('groups', GroupViewSet)
router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/posts/<int:post_id>/comments/', CommentListCreate.as_view()),
    path(
        'v1/posts/<int:post_id>/comments/<int:comment_id>/',
        CommentDetail.as_view(),
    ),
    path('v1/follow/', FollowViewSet.as_view()),
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
