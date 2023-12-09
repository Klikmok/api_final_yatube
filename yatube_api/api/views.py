from rest_framework import viewsets, generics, permissions, filters, mixins
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend

from posts.models import Post, Group, Comment, Follow, User
from .serializers import (
    PostSerializer,
    GroupSerializer,
    CommentSerializer,
    FollowSerializer
)
from .permissions import IsAuthorOrReadOnlyPermission


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowListCreate(generics.ListCreateAPIView):
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    filterset_fields = ('following',)
    search_fields = ('following__username',)
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = get_object_or_404(User, username=self.request.user)
        queryset = Follow.objects.filter(user=user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class CommentListCreate(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        queryset = Comment.objects.filter(post=post)
        return queryset


class DefaultModelMixin(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    None


class CommentViewSet(DefaultModelMixin):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnlyPermission,)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        comment_id = self.kwargs.get('comment_id', False)
        if comment_id:
            comment = get_object_or_404(
                Comment, post=post, pk=comment_id
            )
            return comment
        comments = Comment.objects.filter(post_id=post_id)
        return comments

    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        serializer.save(author=self.request.user, post=post)
