from rest_framework import serializers

from posts.models import Post
from places.models import Locals, LocalProducts
from users.models import Account

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            "id", 
            "title", 
            "body", 
            "added", 
            "owner_post"
        ]
