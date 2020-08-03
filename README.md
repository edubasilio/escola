# Escola
Pequena API REST para cadastro de _aluno_, _curso_, _turma_ e _sala_

# Tecnologias
* Python
* Django
* Django Rest Framework
* Jason Web Token
* Docker
* Docker Composer

# Instalação
1. Instale o Docker e Docker-Compose;
2. Em um local de sua preferência, crie três diretórios
    - `data` - para guardar os registro do banco de dados;
    - `staticfiles` - para guardar os arquivos estáticos do projeto;
    - `media` - para guardar os arquivos dos usuários do projeto.
3. Faça o download deste repositório git;
5. No diretório `escola/escola` (diretório que contém o arquivo `manage.py`), crie um arquivo `.env` para guardar as variáveis de ambiente utilizadas por este projeto como no exemplo abaixo:
```env
MULTISTAGE=LOCAL
ALLOWED_HOSTS=local.escola.com
STATICFILES_PATH=/home/eduardo/Sistemas/Escola/staticfiles
STATIC_URL=/static/
MEDIA_PATH=/home/eduardo/Sistemas/Escola/media
MEDIA_URL=/media/
SECRET_KEY=+p1-v2)-1mgln%m2&_3bxkszjx^89g3jbonf(kz1o605n=b7-&

DB_DATA_PATH=/home/eduardo/Sistemas/Escola/data
DB_ENGINE=django.db.backends.postgresql
DB_NAME=escola
DB_USER=escola_user
DB_PASSWORD=3bxkszjx
DB_HOST=db
DB_PORT=5432

HOST_HTTP_PORT=80
GUNICORN_WORKERS=2
```
Onde:
* MULTISTAGE
* ALLOWED_HOSTS
* STATICFILES_PATH
* STATIC_URL
* MEDIA_PATH
* MEDIA_URL
* SECRET_KEY
* DB_DATA_PATH
* DB_ENGINE
* DB_NAME
* DB_USER
* DB_PASSWORD
* DB_HOST
* DB_PORT
* HOST_HTTP_PORT
* GUNICORN_WORKERS

# Como Usar

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)