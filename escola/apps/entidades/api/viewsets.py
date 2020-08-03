from rest_framework import viewsets

from filters.mixins import FiltersMixin

from entidades.models import Sala, Curso, Turma, Aluno, Matricula
from .serializers import SalaSerializer, CursoSerializer, TurmaSerializer, AlunoSerializer, MatriculaSerializer
from .validators import matriculas_query_schema, alunos_query_schema


class SalaViewSet(viewsets.ModelViewSet):
    queryset = Sala.objects.all()
    serializer_class = SalaSerializer


class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


class AlunoViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_validation_schema = alunos_query_schema
    filter_mappings = {
        'id': 'id',
        'nome': 'nome__icontains',
        'cpf': 'cpf',
    }


class MatriculaViewSet(FiltersMixin, viewsets.ModelViewSet):
    queryset = Matricula.objects.prefetch_related('aluno', 'curso', 'turma').all()
    serializer_class = MatriculaSerializer
    filter_validation_schema = matriculas_query_schema
    filter_mappings = {
        'id': 'id',
        'curso_id': 'curso',
        'turma_id': 'turma',
        'aluno_id': 'aluno',
    }
