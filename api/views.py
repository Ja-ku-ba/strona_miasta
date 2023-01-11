from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import PostSerializer, LocalSerializer, LocalProductSerializer
from posts.models import Post
from places.models import Locals, LocalProducts
# Create your views here.

@api_view(["GET"])
def PostsView(request):
    posts = Post.objects.all()
    serialize = PostSerializer(posts, many=True)
    return Response(serialize.data)

@api_view(["GET"])
def LocalsView(request):
    locals = Locals.objects.all()
    serialize = LocalSerializer(locals, many=True)
    return Response(serialize.data)

@api_view(["GET"])
def LocalProductsView(request, pk):
    try:
        local = Locals.objects.get(id=pk)
        products = LocalProducts.objects.filter(product_local=local)
        serialize = LocalProductSerializer(products, many=True)
        return Response(serialize.data)
    except Locals.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)