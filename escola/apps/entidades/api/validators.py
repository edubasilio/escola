from filters.schema import base_query_params_schema
from filters.validations import CSVofIntegers, IntegerLike


# make a validation schema for matriculas filter query params
matriculas_query_schema = base_query_params_schema.extend(
    {
        "id": IntegerLike(),
        "curso_id": CSVofIntegers(),  # /?curso_id=1,2,3
        "aluno_id": CSVofIntegers(),  # /?aluno_id=1,2,3
        "turma_id": CSVofIntegers(),  # /?turma_id=1,2,3
    }
)
