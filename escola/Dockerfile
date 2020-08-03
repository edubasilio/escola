FROM basiliocode/python3-alpine3

# create project directory
WORKDIR /app/escola
COPY . /app/escola

RUN chmod +x entrypoint.sh
RUN chmod 777 entrypoint.sh

# install requeriments
RUN pipenv install
