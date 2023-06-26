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
    return redirect('verCarrinho')

def verCarrinho(request):
    if(request.session["logado"]):
        #cliente = Cliente.objects.filter(cpf=request.session["user"]).values_list('cpf', flat=True)[0]
        cliente = Cliente.objects.filter(cpf=request.session["user"]).first()
        carrinho = Carrinho.objects.filter(cliente=cliente).values_list('produto', flat=True)
        request.session["ids"] = str(carrinho)
        data = Produto.objects.filter(id__in=carrinho)
        return render(request, 'carrinho/carrinho.html', {'cards':data})
    return redirect('login')

def removerCarrinho(request, item_id):
    if(request.session["logado"]):
        produto = get_object_or_404(Produto, pk=item_id)
        item = get_object_or_404(Carrinho, produto=produto)
        item.delete()
        return redirect('verCarrinho')
    return redirect('login')