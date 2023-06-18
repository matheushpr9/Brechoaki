from django.contrib import admin

from vitrine.models import Endereco,Cliente,Loja,Produto,Compra,Venda

class ListandoProdutos(admin.ModelAdmin):
    list_display = ("id", "nome", "categoria","tamanho", "preco", "estadoDaPeca","loja","disponibilidade")
    list_display_links = ("id", "nome")
    search_fields = ("id", "nome")
    list_filter = ("categoria","tamanho")
    list_editable = ("disponibilidade",)
    list_per_page = 10
admin.site.register(Endereco)
admin.site.register(Cliente)
admin.site.register(Loja)
admin.site.register(Produto, ListandoProdutos)
admin.site.register(Compra)
admin.site.register(Venda)