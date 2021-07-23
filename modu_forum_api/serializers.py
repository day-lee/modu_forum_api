from rest_framework.serializers import ModelSerializer
from modu_forum_api.models import Post, Comment

class CommentSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'post', 'name', 'content', 'published')
        model = Comment

class PostSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'published', 'likes')
        model = Post




