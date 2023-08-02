from rest_framework import serializers
from .models import Alunos, Cursos, Matriculas


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alunos
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cursos
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matriculas
        fields = '__all__'

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matriculas
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class MatriculasListaAlunoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Matriculas
        fields = ['aluno']
    
    