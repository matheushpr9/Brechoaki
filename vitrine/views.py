from django.shortcuts import render, get_object_or_404, redirect
from vitrine.models import Produto
from usuarios.models import Cliente


def index(request):
   
    try:
        if(request.session["logado"]):
            data = Produto.objects.order_by("criadoEm").filter(disponibilidade =True)
            return render(request, 'vitrine/index.html', {'cards':data})
    except:
        request.session["logado"] = False
    return redirect('login')


def imagem(request, item_id):
    if(request.session["logado"]):
        item = get_object_or_404(Produto, pk=item_id)
        request.session["item_id"] = item_id
        return render(request, 'vitrine/imagem.html', {"item":item})
    return redirect('login')

def busca(request):
    if(request.session["logado"]):
        data = Produto.objects.order_by("criadoEm").filter(disponibilidade =True)

        if "busca" in request.GET:
            produtoBusca = request.GET['busca']
            if produtoBusca:
                data = data.filter(nome__icontains=produtoBusca)

        return render(request, 'vitrine/busca.html', {'cards':data})
    return redirect('login')
