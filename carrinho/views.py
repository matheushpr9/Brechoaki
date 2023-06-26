from django.shortcuts import render, get_object_or_404, redirect
from vitrine.models import Produto, Cliente
from carrinho.models import Carrinho


def adicionarCarrinho(request):
    produto = Produto.objects.filter(id=request.session["item_id"]).first()
    cliente = Cliente.objects.filter(cpf = request.session["user"]).first()
    carrinho = Carrinho(
        produto = produto,
        cliente = cliente
    )
    carrinho.save()
    return redirect('home')