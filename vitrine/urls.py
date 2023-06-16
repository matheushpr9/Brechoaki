from django.urls import path
from vitrine.views import index, imagem, busca

urlpatterns = [
    path('', index, name = 'home'),
    path('imagem<int:item_id>', imagem, name = 'imagem'),
    path("busca",busca,name="busca")
]