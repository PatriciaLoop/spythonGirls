from django.contrib import admin
from .models import Produto, Vendedor

# Register your models here.

class Produtos(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'product_price', 'product_code', 'id_seller', 'product_quant', 'status')
    list_display_links = ('id', 'product_name')
    list_per_page = 10

admin.site.register(Produto, Produtos)

class Vendedores(admin.ModelAdmin):
    list_display = ('id', 'seller_name')
    list_display_links = ('id', 'seller_name')
    list_per_page = 10

admin.site.register(Vendedor, Vendedores)