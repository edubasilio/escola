import six

from filters.schema import base_query_params_schema
from filters.validations import CSVofIntegers, IntegerLike


# make a validation schema for matriculas filter query params
matriculas_query_schema = base_query_params_schema.extend(
    {
        "id": IntegerLike(),
        "curso": CSVofIntegers(),  # /?curso=1,2,3
        "aluno": CSVofIntegers(),  # /?aluno=1,2,3
        "turma": CSVofIntegers(),  # /?turma=1,2,3
    }
)

alunos_query_schema = base_query_params_schema.extend(
    {
        "id": IntegerLike(),
        "nome": six.text_type,
        "cpf": six.text_type,
    }
)
