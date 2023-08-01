from django.http import JsonResponse
from rest_framework import viewsets
from .models import Alunos,Cursos
from .serializer import AlunoSerializer, CursoSerializer

# Create your views here.


class AlunosViewSet(viewsets.ModelViewSet):
    queryset = Alunos.objects.all()
    serializer_class = AlunoSerializer

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Cursos.objects.all()
    serializer_class = CursoSerializer


