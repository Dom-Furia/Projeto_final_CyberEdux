from django.contrib import admin
from .models import Professor, Aluno, Curso, Departamento, Matricula
# Adicionando as tabelas no Adm do Django
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Departamento)
admin.site.register(Matricula)