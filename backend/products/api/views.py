from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from ..models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def git_queryset(self):
        return Product.objects.filter(active=True)
