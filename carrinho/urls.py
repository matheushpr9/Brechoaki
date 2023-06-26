from django.urls import path
from carrinho.views import adicionarCarrinho

urlpatterns = [
    path("adicionarCarrinho",adicionarCarrinho, name="adicionarCarrinho")
]