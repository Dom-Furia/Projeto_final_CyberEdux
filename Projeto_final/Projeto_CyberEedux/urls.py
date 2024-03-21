
from django.contrib import admin
from django.urls import path
from sistema_academico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('remover/<int:id>/', views.delete_aluno, name='delete_aluno'),
    path('alterar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('adicionar/', views.adicionar_aluno, name='adicionar_aluno'),
    path('matricular_aluno/', views.matricular_aluno, name='matricular_aluno'),
    path('criar_curso/', views.criar_curso, name='criar_curso'),
    path('cadastrar_professor/',views.cadastrar_Professor, name='cadastrar_professor'),
    path('cadastrar_departamento/',views.Cadastrar_departamento, name='cadastrar_departamento'),
    path('ver_aluno/<int:id>/', views.ver_aluno, name='ver_aluno'),
    path('editar_curso/<int:id>/', views.edite_curso, name='edite_curso'),
    path('deletar_curso/<int:id>/', views.delete_curso, name='delete_curso'),
    path('deletar_disciplina/<int:id>/<int:curso_id>/', views.delete_disciplina, name='delete_disciplina'),
    
    

]
