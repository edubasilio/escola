from rest_framework import serializers

from entidades.models import Sala, Curso, Turma, Aluno, Matricula


class SalaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sala
        fields = '__all__'


class CursoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class TurmaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class AlunoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class MatriculaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'
