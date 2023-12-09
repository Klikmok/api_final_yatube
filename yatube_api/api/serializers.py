from rest_framework import serializers

from posts.models import Post, Group, Comment, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )
    image = serializers.ImageField(default=None)

    class Meta():
        model = Post
        fields = ['id', 'text', 'group', 'author', 'pub_date', 'image']
        read_only_fields = ('author', 'pub_date')


class GroupSerializer(serializers.ModelSerializer):
    class Meta():
        model = Group
        fields = ['id', 'title', 'slug', 'description']


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=serializers.CurrentUserDefault(),
    )
    following = serializers.SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

    class Meta():
        model = Follow
        fields = ['user', 'following']
        read_only_fields = ('user',)

    def validate(self, data):
        """Проверка подписки(нельзя подписаться на себя самого же.)."""
        if data['user'] == data['following']:
            raise serializers.ValidationError(
                'Вы не можете подписаться сам на себя!'
            )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta():
        model = Comment
        fields = ['id', 'text', 'author', 'created', 'post']
        read_only_fields = ('author', 'created', 'post')
