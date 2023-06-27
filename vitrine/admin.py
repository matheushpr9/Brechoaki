from django.contrib import admin

from vitrine.models import EnderecoCliente,EnderecoLoja,Loja,Produto,Compra,Venda
from carrinho.models import Carrinho
from usuarios.models import Cliente

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria","tamanho", "preco", "estadoDaPeca","loja","disponibilidade")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")
    list_filter = ("categoria","tamanho")
    list_editable = ("disponibilidade",)
    list_per_page = 10
admin.site.register(EnderecoCliente)
admin.site.register(EnderecoLoja)
admin.site.register(Cliente)
admin.site.register(Loja)
admin.site.register(Produto, ListandoProdutos)
admin.site.register(Compra)
admin.site.register(Venda)
admin.site.register(Carrinho)