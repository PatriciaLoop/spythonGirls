from rest_framework import serializers
from .models import Produto, Vendedor

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['product_name', 'product_price', 'product_code', 'id_seller', 'product_quant', 'status']

class VendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendedor
        fields = '__all__'