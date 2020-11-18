from django.db import models

# Create your models here.
class Produto(models.Model):
    STATUS = (
        ('A', 'Ativo'),
        ('I', 'Inativo')
    )
    product_name = models.CharField(max_length = 200)
    product_price = models.IntegerField()
    product_code = models.IntegerField()
    id_seller = models.IntegerField()
    product_quant = models.IntegerField()
    status = models.CharField(max_length = 1, choices = STATUS, blank = False, null = False, default = 'A')

    def __str__(self):
        return self.product_name

class Vendedor(models.Model):
    seller_name = models.CharField(max_length = 200)

    def __str__(self):
        return self.seller_name