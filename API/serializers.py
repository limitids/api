from rest_framework import serializers
from API.models import Post

class PostSerializer(serializers.Serializer):
    class Meta:
        model = Post
        fields=['content']