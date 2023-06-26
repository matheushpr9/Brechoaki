from django.db import models
from datetime import datetime

    
class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    cpf = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    telefone = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    senha = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self):
        return f"{self.cpf} - {self.nome}"
    
    def auth(email, password):
        if Cliente.objects.filter(email=email).exists():
            field_name = 'senha'
            #obj = Cliente.objects.filter(email=email)
            obj = Cliente.objects.filter(email=email).first()
            field_object = Cliente._meta.get_field(field_name)
            
            if field_object.value_from_object(obj) == password:
                return True
            
        return False


class EnderecoLoja(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=100, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade =  models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.rua},{self.bairro},{self.numero} {self.complemento},{self.cidade}"
    
class EnderecoCliente(models.Model):
    id = models.AutoField(primary_key=True)
    rua = models.CharField(max_length=100, null=False, blank=False)
    bairro = models.CharField(max_length=100, null=False, blank=False)
    cidade =  models.CharField(max_length=100, null=False, blank=False)
    numero = models.IntegerField(null=False)
    complemento = models.CharField(max_length=100, null=True, blank=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.rua},{self.bairro},{self.numero} {self.complemento},{self.cidade}"

class Loja(models.Model):
    nomeFantasia = models.CharField(max_length=100, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    cnpj = models.CharField(max_length=100, null=False, blank=False, primary_key=True)
    telefone= models.CharField(max_length=100, null=False,blank=False)
    email = models.CharField(max_length=100, null=False, blank=False)
    endereco = models.ForeignKey(EnderecoLoja, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nomeFantasia}-{self.cnpj}"

class Produto(models.Model):

    OPCOES_CATEGORIA = [
        ("MASCULINO","Masculino"),
        ("FEMININO","Feminino"),
        ("INFANTIL","Infantil"),
        ("UNISEX","Unisex")
    ]

    OPCOES_ESTADO =[
        ("EXECELENTE","Execelente"),
        ("BOM", "Bom"),
        ("DEFEITUOSO","Defeituoso")
    ]

    id = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to=f"fotos/{id}", blank=True)
    nome = models.CharField(max_length=100, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(max_length=100, blank=False)
    tamanho = models.CharField(max_length=2, blank=False, null=False)
    preco = models.FloatField(null=False)
    estadoDaPeca = models.CharField(max_length=100, choices=OPCOES_ESTADO, default='')
    disponibilidade = models.BooleanField(default=False)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    criadoEm = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return f"{self.id} - {self.nome}"
    
class Compra(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(default=datetime.now, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)

class Venda(models.Model):
    id = models.AutoField(primary_key=True)
    data = models.DateTimeField(default=datetime.now, blank=False)
    cliente = models.ForeignKey(Cliente, on_delete=models.DO_NOTHING)
    loja = models.ForeignKey(Loja, on_delete=models.DO_NOTHING)