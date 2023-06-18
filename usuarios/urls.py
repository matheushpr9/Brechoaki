from django.urls import path
from usuarios.views import login, cadastro, logout
# path(urlNoSite, MetodoChamado,nome )

urlpatterns = [
    path('login', login, name="login"),
    path('cadastro', cadastro, name="cadastro"),
    path('logout', logout, name="logout")
]