from django.db import models
from vitrine.models import Produto, Cliente

# Create your models here.
class Carrinho(models.Model):
    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)