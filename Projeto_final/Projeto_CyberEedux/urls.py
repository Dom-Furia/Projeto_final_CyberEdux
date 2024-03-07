
from django.contrib import admin
from django.urls import path
from sistema_academico import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('remover/<int:id>/', views.delete_aluno, name='delete_aluno'),
    path('alterar/<int:id>/', views.editar_aluno, name='editar_aluno'),
]
