from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from usuarios.models import Cliente 
from django.contrib import messages


def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            email= form["email"].value()
            senha= form["senha"].value()

            usuario = Cliente.auth(email=email,password=senha)
            if usuario:
                field_name = 'nome'

                obj = Cliente.objects.filter(email=email).first()
                field_object = Cliente._meta.get_field(field_name)
                nome = field_object.value_from_object(obj)
                obj = Cliente.objects.filter(email=email).first()
                field_object = Cliente._meta.get_field('cpf')
                cpf = field_object.value_from_object(obj)
                request.session["logado"] = True
                request.session["user"] = f"{cpf}"
                messages.success(request, f"Seja Bem vindo de volta {nome}!!!")
                return redirect('home')
            messages.error(request, "Email ou senha invaĺálido(s)")
            return redirect('login')

    return render(request, 'usuarios/login.html', {"form":form})

def cadastro(request):

    form = CadastroForms()

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():

            if form["senha1"].value()!= form["senha2"].value():
               messages.error(request, "As senhas não são iguais")
               return redirect('cadastro')
            
            nome = form["nomeCompleto"].value()
            cpf = form["cpf"].value()
            telefone = form["telefone"].value()
            email = form["email"].value()
            senha1 = form["senha1"].value()
        
            if Cliente.objects.filter(email=email).exists() or Cliente.objects.filter(cpf=cpf).exists():
                messages.error(request, "Email ou CPF já cadastrado")
                return redirect('cadastro')
            
            usuario = Cliente(
                nome = nome,
                cpf = cpf,
                telefone = telefone,
                email = email,
                senha = senha1
            )

            usuario.save()
            messages.success(request, "Usúario criado com sucesso! faça seu login!")
            return redirect('login')

    return render(request, 'usuarios/cadastro.html', {"form":form})

def logout(request):
    messages.success(request, "Até mais!")
    request.session["logado"] = False
    return redirect("login")