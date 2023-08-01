from rest_framework import serializers
from .models import Alunos, Cursos


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'
