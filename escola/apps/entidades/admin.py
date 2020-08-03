from django.contrib import admin

from .models import Sala, Curso, Turma, Aluno, Matricula


admin.site.register(Sala)
admin.site.register(Curso)
admin.site.register(Turma)
admin.site.register(Aluno)
admin.site.register(Matricula)
