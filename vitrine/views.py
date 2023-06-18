from django.shortcuts import render, get_object_or_404
from vitrine.models import Produto


def index(request):
    data = Produto.objects.order_by("criadoEm").filter(disponibilidade =True)
    return render(request, 'vitrine/index.html', {'cards':data})

def imagem(request, item_id):
    item = get_object_or_404(Produto, pk=item_id)
    return render(request, 'vitrine/imagem.html', {"item":item})

def busca(request):
    data = Produto.objects.order_by("criadoEm").filter(disponibilidade =True)

    if "busca" in request.GET:
        produtoBusca = request.GET['busca']
        if produtoBusca:
            data = data.filter(nome__icontains=produtoBusca)

    return render(request, 'vitrine/busca.html', {'cards':data})