from rest_framework import viewsets
from rest_framework.serializers import *
from .models import Produto, Vendedor
from products.serializer import ProdutoSerializer, VendedorSerializer

# Create your views here.

class ProdutosViewSet(viewsets.ModelViewSet):
    """Exibindo Produtos"""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class VendedoresViewSet(viewsets.ModelViewSet):
    """Exibindo Vendedores"""
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer
