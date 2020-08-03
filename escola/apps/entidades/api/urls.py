from rest_framework import routers

from . import viewsets


router = routers.DefaultRouter()
router.register(r'salas', viewsets.SalaViewSet, basename='sala')
router.register(r'cursos', viewsets.CursoViewSet, basename='curso')
router.register(r'turmas', viewsets.TurmaViewSet, basename='turma')
router.register(r'alunos', viewsets.AlunoViewSet, basename='aluno')
router.register(r'matriculas', viewsets.MatriculaViewSet, basename='matricula')

urlpatterns = router.urls
