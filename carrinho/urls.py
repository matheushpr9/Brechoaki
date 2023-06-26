from django.urls import path
from carrinho.views import adicionarCarrinho, verCarrinho,removerCarrinho

urlpatterns = [
    path("adicionarCarrinho",adicionarCarrinho, name="adicionarCarrinho"),
    path("verCarrinho", verCarrinho, name="verCarrinho"),
    path('removerCarrinho<int:item_id>', removerCarrinho, name = 'removerCarrinho')
]