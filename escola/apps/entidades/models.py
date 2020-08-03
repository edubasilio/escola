from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.db import models

from .validators import validate_cpf


class Sala(models.Model):
    codigo = models.CharField(max_length=8, unique=True, verbose_name=_('Código'))
    lotacao = models.IntegerField(verbose_name=_('Lotação'))

    class Meta:
        verbose_name = _('Sala')
        verbose_name_plural = _('Salas')
    
    def __str__(self):
        return "{}".format(self.codigo)


class Curso(models.Model):
    nome = models.CharField(max_length=128, unique=True, verbose_name=_('Nome'))

    class Meta:
        verbose_name = _('Curso')
        verbose_name_plural = _('Cursos')
    
    def __str__(self):
        return "{}".format(self.nome)


class Turma(models.Model):
    codigo = models.CharField(max_length=8, unique=True, verbose_name=_('Código'))
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, verbose_name=_('Curso'))

    class Meta:
        verbose_name = _('Turma')
        verbose_name_plural = _('Turmas')
    
    def __str__(self):
        return "{}".format(self.codigo)


class Aluno(models.Model):
    nome = models.CharField(max_length=256, verbose_name=_('Nome'))
    cpf = models.CharField(
        max_length=11,
        unique=True,
        validators=[
            RegexValidator(
                regex="^.{11}$", message=_("Length has to be 11"), code="nomatch"
            ),
            validate_cpf,
        ],
        verbose_name=_("CPF"),
        help_text=_("Cadastro de Pessoa Física"),
    )
    
    class Meta:
        verbose_name = _('Aluno')
        verbose_name_plural = _('Alunos')

    def __str__(self):
        return "{}".format(self.nome)


class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, verbose_name=_('Aluno'))
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, verbose_name=_('Curso'))
    turma = models.ForeignKey(Turma, on_delete=models.SET_NULL, null=True, verbose_name=_('Turma'))

    class Meta:
        unique_together = ['aluno', 'turma']
        verbose_name = _('Matrícula')
        verbose_name_plural = _('Matrículas')
    
    def __str__(self):
        return "{}".format(self.pk)