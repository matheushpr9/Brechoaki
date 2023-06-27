from django.db import models

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
