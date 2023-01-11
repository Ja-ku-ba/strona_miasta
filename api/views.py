from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import PostSerializer
from posts.models import Post
from places.models import Locals, LocalProducts
# Create your views here.

@api_view(["GET"])
def ProductView(request):
    posts = Post.objects.all()
    serialize = PostSerializer(posts, many=True)
    return Response(serialize.data)