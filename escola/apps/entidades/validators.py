from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from domplus import govplus


def validate_cpf(value):
    if not govplus.is_valid_br_cpf(value):
        raise ValidationError(_('{} não é um CPF válido'.format(value)))
