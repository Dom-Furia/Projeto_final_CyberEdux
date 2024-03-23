from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Aluno, Curso, Departamento, Professor, Matricula
from django.contrib import messages
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_django

@login_required(login_url="/")
def home(request):
    alunos_cursos = Aluno.objects.prefetch_related('matriculas__curso').all()
    return render(request, 'home.html', {'alunos_cursos': alunos_cursos})


@login_required(login_url="/")
def delete_aluno(request, id):
    alunos = Aluno.objects.get(id=id)
    if request.method == "POST":
        alunos.delete()
        return redirect('home')
    return render(request, 'delete_aluno.html', {'alunos': alunos})

@login_required(login_url="/")
def editar_aluno(request, id):
    alunos = Aluno.objects.get(id=id)
    if request.method == "POST":
        alunos.nome = request.POST.get('nome')
        alunos.matricula = request.POST.get('matricula')
        alunos.telefone = request.POST.get('telefone')
        alunos.save()
        return redirect('home')
    return render(request, 'editar_aluno.html', {'alunos': alunos})

@login_required(login_url="/")
def adicionar_aluno(request):
    alunos_cursos = Aluno.objects.prefetch_related('matriculas__curso').all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        matricula = request.POST.get('matricula')
        telefone = request.POST.get('telefone')
        cpf = request.POST.get('cpf')
        endereco = request.POST.get('endereco')
        email = request.POST.get('email')
        data_nascimento = request.POST.get('data_nascimento')
        data_formatada = datetime.strptime(data_nascimento, '%d/%m/%Y').strftime('%Y-%m-%d')
        Aluno.objects.create(nome=nome, matricula=matricula, telefone=telefone,cpf=cpf,endereco=endereco,data_nascimento=data_formatada,email=email)
        return redirect('adicionar_aluno')
    return render(request, 'adicionar_aluno.html', {'alunos_cursos': alunos_cursos})

@login_required(login_url="/")
def criar_curso(request):
    cursos = Curso.objects.all()
    departamento = Departamento.objects.all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        descricao = request.POST.get('descricao')
        carga_horaria = request.POST.get('carga_horaria')
        departamento_id = request.POST.get('departamento')
        dp = Departamento.objects.get(id=departamento_id)
        if cursos.filter(nome=nome).exists():
            messages.error(request, 'Já existe um curso com este nome.')
            return redirect('criar_curso')
        else:
            try:
                cursos.create(nome=nome, descricao=descricao,carga_horaria=carga_horaria, departamento = dep)
                messages.success(request, 'Curso criado com sucesso!')
                return redirect('criar_curso')
            except Exception as e:
                messages.error(request, f'Erro ao criar curso: {e}')
                return redirect('criar_curso')
    return render(request, 'criar_curso.html', {'cursos':cursos, 'departamento':departamento})

@login_required(login_url="/")
def ver_aluno(request, id):
    aluno = Aluno.objects.prefetch_related('matriculas__curso').get(id=id)
    return render(request, 'ver_aluno.html', {'aluno': aluno})

@login_required(login_url="/")
def listar_cursos_e_departamentos(request):
    todos_os_cursos = Curso.objects.all()
    todos_os_departamentos = Departamento.objects.all()
    return render(request, 'lista_cursos_departamentos.html', {'cursos': todos_os_cursos, 'departamentos': todos_os_departamentos})

@login_required(login_url="/")
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
                return redirect('matricular_aluno')
            except Exception as e:
                messages.error(request, f'Erro ao matricular aluno (a): {e}')
                return redirect('home')
    else:
        alunos = Aluno.objects.all()
        cursos = Curso.objects.all()
        return render(request, 'matricular_aluno.html', {'alunos': alunos, 'cursos': cursos})

@login_required(login_url="/")
def cadastrar_Professor(request):
    professor = Professor.objects.all()
    departamentos = Departamento.objects.all()
    curso = Curso.objects.all()
    if request.method == "POST":
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        disciplinas = request.POST.get('disciplinas')
        telefone = request.POST.get('telefone')
        endereco = request.POST.get('endereco')
        departamento_id = request.POST.get('departamento')
        dep = Departamento.objects.get(id=departamento_id)
        print(departamento_id)
        if professor.filter(nome=nome).exists():
            messages.error(request, 'Já existe um professor com este nome.')
            return redirect('cadastrar_professor')
        else:
            try:
                professor.create(nome=nome,email = email,telefone = telefone,  disciplina_ministrada = disciplinas,endereco = endereco, departamento = dep)
                messages.success(request, 'Professor adicionado com sucesso!')
                return redirect('cadastrar_professor')
            except Exception as e:
                messages.error(request, f'Erro ao criar professor: {e}')
                return redirect('cadastrar_professor')     
    return render(request, 'cadastrar_professor.html', {'professor':professor, 'departamentos':departamentos, 'curso':curso})

@login_required(login_url="/")
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

@login_required(login_url="/")
def edite_curso(request, id):
    cursos = Curso.objects.get(id=id)
    departamentos = Departamento.objects.all()
    if request.method == "POST":
        cursos.nome = request.POST.get('nome', cursos.nome)
        cursos.descricao = request.POST.get('descricao', cursos.descricao)
        cursos.duracao = request.POST.get('duracao', cursos.duracao)
        cursos.coordenador = request.POST.get('coordenador', cursos.coordenador)
        cursos.carga_horaria = request.POST.get('carga_horaria', cursos.carga_horaria)
        dp_id = request.POST.get('departamento', cursos.departamento)
        departamento = Departamento.objects.get(id=dp_id)
        cursos.departamento = departamento
        try:
            cursos.save()
            messages.success(request, 'Curso salvo com sucesso!')
        except Exception as e:
            messages.error(request, f'Ocorreu um erro ao salvar o curso: {str(e)}')
        return redirect('edite_curso', id=id)
    return render(request, 'editar_curso.html', {'cursos': cursos, 'departamentos':departamentos})

@login_required(login_url="/")
def delete_curso(request, id):
    cursos = Curso.objects.get(id=id)
    if request.method == "POST":
        cursos.delete()
        return redirect('criar_curso')
    return render(request, 'delete_curso.html', {'cursos': cursos})

@login_required(login_url="/")
def delete_disciplina(request, id, curso_id):

    if request.method == 'POST':
        try:
            # Exclua a disciplina
            matricula = Matricula.objects.get(aluno_id=id, curso_id=curso_id)
            matricula.delete()
            # Redirecione para a página de confirmação após a exclusão
            return redirect('ver_aluno', id=id)
        except Matricula.DoesNotExist:
            pass
    else:
        try:
            # Renderize a página de confirmação
            disciplina = Matricula.objects.get(aluno_id=id, curso_id=curso_id)
            return render(request, 'delete_disciplina.html', {'disciplina': disciplina})
        except Matricula.DoesNotExist:
            pass
    return redirect('pagina_de_erro')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        nome = request.POST.get('nome')
        senha = request.POST.get('senha')
        user = authenticate(username = nome, password = senha)
        if user:
            login_django(request, user)
            return redirect ('home')
        else:
            return HttpResponse('Dados invalidos')

def logout(request):
    logout_django(request)
    return redirect('login')


        






