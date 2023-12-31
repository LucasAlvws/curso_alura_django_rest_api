from django.db import models

# Create your models here.


class Alunos(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    

class Cursos(models.Model):

    NIVEL = [
        ('B' , 'Básico'),
        ('I' , 'Intermediário'),
        ('A' , 'Avançado')
    ]

    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(choices=NIVEL, max_length=1, blank=False, default='B')

    def __str__(self):
        return self.descricao


class Matriculas(models.Model):
    PERIODO = [
        ('M' , 'Matutino'),
        ('V' , 'Vespertino'),
        ('N' , 'Noturno')
    ]
    aluno = models.ForeignKey(Alunos, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    periodo = models.CharField(choices=PERIODO, max_length=1, blank=False, null=False, default='M')
