from django.contrib import admin
from .models import Alunos, Curso
# Register your models here.

class Aluno(admin.ModelAdmin):
    list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento',)
    list_display_links = ('id', 'nome',)
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Alunos, Aluno)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao', 'nivel',)
    list_display_links = ('id', 'codigo_curso', )
    search_fields = ('codigo_curso',)

admin.site.register(Curso, Cursos)
