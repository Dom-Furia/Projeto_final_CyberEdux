from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.IntegerField()
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    data_nascimento = models.DateField()
    matricula = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    departamento = models.CharField(max_length=100)
    data_contratacao = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2)
    disciplina_ministrada = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    duracao = models.IntegerField()
    coordenador = models.CharField(max_length=100)
    carga_horaria = models.IntegerField()

    def __str__(self):
        return self.nome
    
class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome