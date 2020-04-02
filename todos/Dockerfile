FROM python:3.6

WORKDIR /usr/src/app

COPY . /usr/src/app

RUN pip install -r requirements.txt

ENTRYPOINT [ "/usr/src/app/docker-entrypoint.sh" ]

CMD [ "gunicorn", "--bind=0.0.0.0", "todos.wsgi" ]