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
    
class Departamento(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()

    def __str__(self):
        return self.nome
    
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, null=True, blank=True)
    data_contratacao = models.DateField(null=True)
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    disciplina_ministrada = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    nota = models.FloatField(null=True)
    situacao = models.CharField(max_length=10, null=True)
    carga_horaria = models.IntegerField()
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.nome
    
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='matriculas')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
