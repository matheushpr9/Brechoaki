from django.urls import path
from usuarios.views import login, cadastro
# path(urlNoSite, MetodoChamado,nome )

urlpatterns = [
    path('login', login, name="login"),
    path('cadastro', cadastro, name="cadastro"),
]