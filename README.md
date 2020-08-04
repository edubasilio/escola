# Escola
Pequena API REST para cadastro de _aluno_, _curso_, _turma_ e _sala_

# Tecnologias
* **Python** como linhguagem de programação
* **Django** como framework de aplicação web
* **Django Rest Framework** como lib de aplicações REST
* **Docker** como gerenciador de container
* **Docker Composer** como orquestrador de container
* **Gunicorn** como servidor de produção
* **Nginx** como servidor proxy
* **PostgreSQL** como banco de dados

# Instalação
1. Instale o Docker e Docker-Compose;
2. Faça o download deste repositório git;
3. No diretório `escola` (diretório que contém o arquivo `docker-compose.yml`), crie um arquivo `.env` para guardar as variáveis de ambiente utilizadas por este projeto como no exemplo abaixo:
```env
MULTISTAGE=LOCAL
SECRET_KEY=+p1-v2)-1mgln%m2&_3bxkszjx^89g3jbonf(kz1o605n=b7-&

STATICFILES_PATH=/caminho/absoluto/para/staticfiles
STATIC_URL=/static/
MEDIA_PATH=/caminho/absoluto/para/media
MEDIA_URL=/media/

DB_DATA_PATH=/caminho/absoluto/para/data
DB_ENGINE=django.db.backends.postgresql
DB_NAME=escola
DB_USER=escola_user
DB_PASSWORD=3bxkszjx
DB_HOST=db
DB_PORT=5432

ALLOWED_HOSTS=.escola.com
HOST_HTTP_PORT=80
HOST_HTTP_DEV_PORT=8000
GUNICORN_WORKERS=2
```

Para um teste rápido deste projeto, utilize os valores já setados acima modificando apenas: `STATICFILES_PATH`, `MEDIA_PATH`, `DB_DATA_PATH`, `ALLOWED_HOSTS`, `HOST_HTTP_PORT` e `HOST_HTTP_DEV_PORT`.

Sobre as variáveis de ambiente:
* `MULTISTAGE` Define o [stage](https://medium.com/@basiliocode/desenvolvimento-de-software-com-multi-stage-8caa38ca7a46) da aplicação. Quando setado para `PROD` o django executará com [settings.DEBUG](https://docs.djangoproject.com/en/3.0/ref/settings/#debug) = `False` no servidor de produção GUNICORN. Caso o valor seja diferente de `PROD`, `settings.DEBUG` receberá `True` e, além do servidor GUNICORN, o servidor de desenvolvimento do django, o _runserver_, será iniciado na porta definida em `HOST_HTTP_DEV_PORT`
* `SECRET_KEY` Define a [chave de segurança](https://docs.djangoproject.com/en/3.0/ref/settings/#secret-key) do projeto django
* `STATICFILES_PATH` Caminho absoluto do diretório em que será arquivado os arquivos estáticos do projeto (html, css, js, etc). Em sua máquina host, crie este diretório (fora do diretório versionado) e registre o caminho absoluto aqui
* `STATIC_URL` [Define a URL de acesso aos arquivos estáticos.](https://docs.djangoproject.com/en/3.0/ref/settings/#static-url) **Deve finalizar com /**
* `MEDIA_PATH` Caminho absoluto do diretório em que será arquivado os arquivos enviados pelo usuário. Em sua máquina host, crie este diretório (fora do diretório versionado) e registre o caminho absoluto aqui
* `MEDIA_URL` [Define a URL de acesso aos arquivos medias](https://docs.djangoproject.com/en/3.0/ref/settings/#media-url). **Deve finalizar com /**
* `DB_DATA_PATH` Caminho absoluto do diretório em que será arquivado os dados do banco de dados. Em sua máquina host, crie este diretório (fora do diretório versionado) e registre o caminho absoluto aqui
* `DB_ENGINE` Define a engine do banco de dados utilizado pelo projeto. O banco de dados deste projeto é o PostgreSQL, portanto, a engine deve ser: `django.db.backends.postgresql`. Mais informações na [documentação](https://docs.djangoproject.com/en/3.0/ref/settings/#engine) do django
* `DB_NAME` Define o nome do schema no banco de dados a ser utilizado pelo projeto
* `DB_USER` Define o nome de usuário a ser usado para acessar o banco de dados
* `DB_PASSWORD` Define o password do usuário do banco de dados
* `DB_HOST` [Define o endereço do banco de dados](https://docs.djangoproject.com/en/3.0/ref/settings/#host). Neste projeto, o endereço do container docker com o banco de dados é `db`
* `DB_PORT` Define a porta de acesso do banco de dados. O banco de dados no container docker deste projeto escuta a porta 5432
* `ALLOWED_HOSTS` Define as [URLs válidas](https://docs.djangoproject.com/en/3.0/ref/settings/#allowed-hosts) de acesso ao sistema separadas por espaço. Para acessar o sistema localmente, edite o arquivo `hosts` (`/etc/hosts no Ubuntu`) na máquina host recionando a URL para a máquina local
* `HOST_HTTP_PORT` Define a porta, na máquina host, de acesso HTTP ao sistema. **Certifique-se de que esta porta na máquina host esteja livre**. No Docker a requisição passará pelo servidor proxy (NGINX) no container docker `escola_proxy` que redirecionará para o servidor da aplicação (GUNICORN) no container docker `escola_web`
* `HOST_HTTP_DEV_PORT` Define a porta, na máquina host, de acesso direto ao sistema através do servidor de desenvolvimento _runserver_ do django. **Certifique-se de que esta porta na máquina host esteja livre**. Este servidor só funcionará quando o valor de `MULTISTAGE` for diferente de `PROD`
* `GUNICORN_WORKERS` Define a [quantidade de workers](https://docs.gunicorn.org/en/stable/configure.html#configuration-file) para o servidor de produção Gunicorn

# Iniciar, Parar e Criar um superusuário

## Iniciar o serviço
Com o terminal no diretório `escola` (diretório que contém o arquivo `docker-compose.yml`), faça:
```sh
docker-compose up -d --build
```

## Parar o serviço
```sh
docker-compose down
```

## Criar um superusuário
Com o serviço iniciado, no terminal faça:
```sh
docker exec -it escola_web pipenv run ./manage.py createsuperuser
```

# Acessando os endpoints da API na máquina host

Considerando as variáveis de ambiente `ALLOWED_HOSTS=.escola.com` e `HOST_HTTP_PORT=80` e que no arquivo `hosts` do Sistema Operacional da máquina host foi inserido a linha `127.0.0.1 local.escola.com`:

## Aluno
#### Listar
URL: http://local.escola.com/api/entidades/alunos/
Method: GET

#### Filtrar
URL: http://local.escola.com/api/entidades/alunos/?nome=Nome&cpf=CPF
Method: GET

#### Criar
* URL: http://local.escola.com/api/entidades/alunos/
* Method: POST
* Payload: JSON
```json
{
    "nome": "Nome",
    "cpf": "CPF válido"
}
```

#### Atualizar
* URL: http://local.escola.com/api/entidades/alunos/AlunoID
* Method: PUT
* Payload: JSON
```json
{
    "nome": "Nome",
    "cpf": "CPF válido"
}
```

#### Deletar
* URL: http://local.escola.com/api/entidades/alunos/AlunoID
* Method: DELETE

## Curso
#### Listar
URL: http://local.escola.com/api/entidades/cursos/
Method: GET

#### Criar
* URL: http://local.escola.com/api/entidades/cursos/
* Method: POST
* Payload: JSON
```json
{
    "nome": "Nome"
}
```

#### Atualizar
* URL: http://local.escola.com/api/entidades/cursos/CursoID
* Method: PUT
* Payload: JSON
```json
{
    "nome": "Nome"
}
```

#### Deletar
* URL: http://local.escola.com/api/entidades/cursos/CursoID
* Method: DELETE

## Sala
#### Listar
URL: http://local.escola.com/api/entidades/salas/
Method: GET

#### Criar
* URL: http://local.escola.com/api/entidades/salas/
* Method: POST
* Payload: JSON
```json
{
    "codigo": "Codigo",
    "lotacao": Integer
}
```

#### Atualizar
* URL: http://local.escola.com/api/entidades/salas/SalaID
* Method: PUT
* Payload: JSON
```json
{
    "codigo": "Codigo",
    "lotacao": Integer
}
```

#### Deletar
* URL: http://local.escola.com/api/entidades/salas/SalaID
* Method: DELETE

## Turma
#### Listar
URL: http://local.escola.com/api/entidades/turmas/
Method: GET

#### Criar
* URL: http://local.escola.com/api/entidades/turmas/
* Method: POST
* Payload: JSON
```json
{
    "codigo": "Codigo",
    "curso": CursoID
}
```

#### Atualizar
* URL: http://local.escola.com/api/entidades/turmas/TurmaID
* Method: PUT
* Payload: JSON
```json
{
    "codigo": "Codigo",
    "curso": CursoID
}
```

#### Deletar
* URL: http://local.escola.com/api/entidades/turmas/TurmaID
* Method: DELETE

## Matrícula
#### Listar
URL: http://local.escola.com/api/entidades/matriculas/
Method: GET

#### Filtrar
URL: http://local.escola.com/api/entidades/matriculas/?aluno=AlunoID&curso=CursoID&turma=TurmaID1,TurmaID2
Method: GET

#### Criar
* URL: http://local.escola.com/api/entidades/matriculas/
* Method: POST
* Payload: JSON
```json
{
    "aluno": AlunoID,
    "curso": CursoID,
    "turma": TurmaID
}
```

#### Atualizar
* URL: http://local.escola.com/api/entidades/matriculas/MatriculaID
* Method: PUT
* Payload: JSON
```json
{
    "aluno": AlunoID,
    "curso": CursoID,
    "turma": TurmaID
}
```

#### Deletar
* URL: http://local.escola.com/api/entidades/matriculas/MatriculaID
* Method: DELETE


## Diagrama de Classes

![Alt text](project/escola-class-diagram.png?raw=true "Diagrama de Classes")


[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)