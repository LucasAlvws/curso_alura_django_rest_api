from django.http import JsonResponse
from rest_framework import viewsets, generics
from .models import Alunos,Cursos,Matriculas
from .serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, MatriculasListaAlunoSerializer

# Create your views here.


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matriculas.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matriculas.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer

class MatriculasListaAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Matriculas.objects.filter(curso_id=self.kwargs['pk'])
        return queryset
    serializer_class = MatriculasListaAlunoSerializer
    