from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Aluno, Curso, Departamento, Professor, Matricula
from django.contrib import messages

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
        alunos.nome = request.POST.get('nome')
        alunos.matricula = request.POST.get('matricula')
        alunos.telefone = request.POST.get('telefone')
        alunos.save()
        return redirect('home')
    return render(request, 'editar_aluno.html', {'alunos': alunos})

def adicionar_aluno(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        Aluno.objects.create(nome=nome, matricula=matricula, telefone=telefone,cpf=cpf,endereco=endereco,data_nascimento=data_nascimento,email=email)
        return redirect('home')
    return render(request, 'adicionar_aluno.html')

def criar_curso(request):
    cursos = Curso.objects.all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        if cursos.filter(nome=nome).exists():
            messages.error(request, 'Já existe um curso com este nome.')
            return redirect('criar_curso')
        else:
            try:
                cursos.create(nome=nome, descricao=descricao,duracao=50,coordenador='Felipe',carga_horaria=120)
                cursos.save()
                messages.success(request, 'Curso criado com sucesso!')
                return redirect('criar_curso')
            except Exception as e:
                messages.error(request, f'Erro ao criar curso: {e}')
                return redirect('criar_curso')
            
    return render(request, 'criar_curso.html', {'cursos':cursos})


def listar_cursos_e_departamentos(request):
    todos_os_cursos = Curso.objects.all()
    todos_os_departamentos = Departamento.objects.all()
    return render(request, 'lista_cursos_departamentos.html', {'cursos': todos_os_cursos, 'departamentos': todos_os_departamentos})


def matricular_aluno(request):
    if request.method == 'POST':
        aluno_id = request.POST.get('aluno')
        curso_id = request.POST.get('curso')
        print(aluno_id)
        
        aluno = Aluno.objects.get(id=aluno_id)
        curso = Curso.objects.get(id=curso_id)
        print(aluno)

        if  Matricula.objects.filter(aluno=aluno, curso=curso).exists():
            messages.error(request, 'Este aluno (a) ja esta matriculado (a) neste curso.')
            return redirect('matricular_aluno')
        else:
            try:
                Matricula.objects.create(aluno=aluno, curso=curso)
                messages.success(request, 'Aluno (a) matriculado com sucesso!')
                Matricula.objects.save()
                return redirect('matricular_aluno')
            except Exception as e:
                messages.error(request, f'Erro ao matricular aluno (a): {e}')
                return redirect('home')
    else:
        alunos = Aluno.objects.all()
        cursos = Curso.objects.all()
        return render(request, 'matricular_aluno.html', {'alunos': alunos, 'cursos': cursos})

def cadastrar_Professor(request):
    professor = Professor.objects.all()
    departamentos = Departamento.objects.all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        disciplinas = request.POST.get('disciplinas')
        telefone = request.POST.get('telefone')
        departamento_id = request.POST.get('departamento')
        dep = Departamento.objects.get(id=departamento_id)
        print(departamento_id)
        if professor.filter(nome=nome).exists():
            messages.error(request, 'Já existe um professor com este nome.')
            return redirect('cadastrar_professor')
        else:
            try:
                professor.create(nome=nome,email = 'curso@cyberedux.com.br',telefone = telefone, data_contratacao='2024-1-15', salario = 4000.78, disciplina_ministrada = disciplinas,endereco = 'Rua B', departamento = dep)
                messages.success(request, 'Professor adicionado com sucesso!')
                return redirect('cadastrar_professor')
            except Exception as e:
                messages.error(request, f'Erro ao criar professor: {e}')
                return redirect('cadastrar_professor')     
    return render(request, 'cadastrar_professor.html', {'professor':professor, 'departamentos':departamentos})

def Cadastrar_departamento(request):
    departamentos = Departamento.objects.all()
    if request.method == "POST":
        nome = request.POST['nome']
        descricao = request.POST['descricao']
        telefone = request.POST['telefone']
        email = request.POST['email']
        if departamentos.filter(nome=nome).exists():
            messages.error(request, 'Já existe um departamento com este nome.')
            return redirect('cadastrar_departamento')
        else:
            try:
                departamentos.create(nome=nome, descricao=descricao,telefone=telefone,email=email)
                messages.success(request, 'Curso criado com sucesso!')
                return redirect('cadastrar_departamento')
            except Exception as e:
                messages.error(request, f'Erro ao criar curso: {e}')
                return redirect('cadastrar_departamento')
            
    return render(request, 'cadastrar_departamento.html', {'departamentos':departamentos})


