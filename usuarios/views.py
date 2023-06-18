from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from vitrine.models import Cliente 

# Create your views here.

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {"form":form})

def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():

            if form["senha1"].value()!= form["senha2"].value():
                return redirect('cadastro')
            
            nome = form["nomeCompleto"].value()
            cpf = form["cpf"].value()
            telefone = form["telefone"].value()
            email = form["email"].value()
            senha1 = form["senha1"].value()
        
            if Cliente.objects.filter(email=email).exists() or Cliente.objects.filter(cpf=cpf).exists():
                return redirect('cadastro')
            
            usuario = Cliente(
                nome = nome,
                cpf = cpf,
                telefone = telefone,
                email = email,
                senha = senha1
            )

            usuario.save()
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form":form})