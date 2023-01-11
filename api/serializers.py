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

class LocalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locals
        fields = [
            "name",
            "description",
            "street",
            "local_addres"
        ]

class LocalProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocalProducts
        fields = [
            "id",
            "name",
            "description",
            "price",
            "product_local",
        ]