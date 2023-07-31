from rest_framework import serializers
from .models import Alunos, Curso


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'
