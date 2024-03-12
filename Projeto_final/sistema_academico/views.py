from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Aluno

def home(request):
    alunos = Aluno.objects.all()
    return render(request, 'home.html', {'alunos': alunos})


def delete_aluno(request, id):
    alunos = Aluno.objects.get(id=id)
    if request.method == "POST":
        alunos.delete()
        return redirect('home')
    return render(request, 'delete_aluno.html', {'alunos': alunos})

def editar_aluno(request, id):
    alunos = Aluno.objects.get(id=id)
    if request.method == "POST":
        alunos.nome = request.POST['nome']
        alunos.matricula = request.POST['matricula']
        alunos.telefone = request.POST['telefone']
        alunos.save()
        return redirect('home')
    return render(request, 'editar_aluno.html', {'alunos': alunos})
from django.shortcuts import render, redirect
from .models import Aluno

def adicionar_aluno(request):
    if request.method == "POST":
        nome = request.POST['nome']
        matricula = request.POST['matricula']
        telefone = request.POST['telefone']
        cpf = request.POST['cpf']
        endereco = request.POST['endereco']
        email = request.POST['email']
        data_nascimento = request.POST['data_nascimento']
        Aluno.objects.create(nome=nome, matricula=matricula, telefone=telefone,cpf=cpf,endereco=endereco,data_nascimento=data_nascimento,email=email)
        return redirect('home')
    return render(request, 'adicionar_aluno.html')


