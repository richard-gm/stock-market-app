FROM python:3.9
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN pip install pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install
COPY . /code/
EXPOSE 8000


# (No need to repeat `command:` in `docker-compose.yml`)
CMD python manage.py runserver 0.0.0.0:8000