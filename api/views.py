from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .serializers import PostSerializer, LocalSerializer, LocalProductSerializer, DistrictSerializer, StreetSerializer
from posts.models import Post
from places.models import Locals, LocalProducts, Street, District
from users.models import Account
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

class ProductView(mixins.ListModelMixin, mixins.RetrieveModelMixin):
    queryset = LocalProducts.objects.all()
    serializer_class = LocalProductSerializer

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(self, *args, **kwargs)
        return self.list(request, *args, **kwargs)











# apis to populate db
@api_view(["POST"])
def add_district(request):
    if request.method == "POST":
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["POST"])
def add_street(request):
    district_name = request.data.get("street_district")
    if district_name is None:
        district = District.objects.all().order_by("?").first()
        request.data["street_district"] = district.id

    serializer = StreetSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
def add_local(request):
    street = Street.objects.all().order_by("?").first()
    request.data["local_street"] = street.id
    random_user = Account.objects.all().order_by("?").first()
    request.data["owner"] = random_user.id
    serializer = LocalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)