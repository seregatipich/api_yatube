from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    group = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Group.objects.all(),
        required=False
    )
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    publication_date = serializers.DateTimeField(
        source='pub_date',
        read_only=True
    )

    class Meta:
        fields = '__all__'
        model = Post
