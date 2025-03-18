from django.shortcuts import render, redirect
from apps.aluno.models import Aluno
from apps.aluno.forms import AlunoForms

def index(request):
    return render(request, 'aluno/index.html')

def listar(request):
    alunos = Aluno.objects.order_by("-id")

    return render(request, "aluno/lista.html", {"alunos": alunos})

def cadastrar(request):
    form = AlunoForms()

    if request.method == 'POST':
        form = AlunoForms(request.POST)
        if form.is_valid:
            form.save()
            return redirect("aluno/lista")
    
    return render(request, "aluno/cadastro.html", {"form": form})

def editar(request):
    pass

def exibir(request):
    pass