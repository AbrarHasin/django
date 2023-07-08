import random
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product

# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #/api/products
        products = Product.objects.all()
        serializers = ProductSerializer(products, many=True)
        return Response(serializers.data)

    def create(self, request): #/api/products
        pass

    def retrieve(self, request, pk=None): #/api/products/<str:id>
        pass

    def update(self, request, pk=None): #/api/products/<str:id>
        pass

    def destroy(self, request, pk=None): #/api/products/<str:id>
        pass

# class UserAPIView(APIView):
#     def get(self, _):
#         user = User.objects.all()
#         user = random.choice(users)
#         return Response({
#             'id': user.id
#         })