from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Aluno, Curso, Departamento, Professor, Matricula

def home(request):
    alunos_cursos = Aluno.objects.prefetch_related('matriculas__curso').all()
    return render(request, 'home.html', {'alunos_cursos': alunos_cursos})



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
def listar_cursos_e_departamentos(request):
    todos_os_cursos = Curso.objects.all()
    todos_os_departamentos = Departamento.objects.all()
    return render(request, 'lista_cursos_departamentos.html', {'cursos': todos_os_cursos, 'departamentos': todos_os_departamentos})

def matricular_aluno(request):
    if request.method == 'POST':
        aluno_id = request.POST['aluno']
        curso_id = request.POST['curso']
        
        aluno = Aluno.objects.get(id=aluno_id)
        curso = Curso.objects.get(id=curso_id)
        
        # Verificar se o aluno já está matriculado no curso
        if Matricula.objects.filter(aluno=aluno, curso=curso).exists():
            return render(request, 'erro_matriculado', {'mensagem': 'Aluno já está matriculado neste curso'})
        
        # Se não estiver matriculado, criar uma nova matrícula
        Matricula.objects.create(aluno=aluno, curso=curso)
        
        return redirect('home.html', aluno_id=aluno_id)
    else:
        alunos = Aluno.objects.all()
        cursos = Curso.objects.all()
        
        return render(request, 'matricular_aluno.html', {'alunos': alunos, 'cursos': cursos})

