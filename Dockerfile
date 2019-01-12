FROM python:3.7

RUN pip install pipenv

ENV FLASK_APP=app
WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system --deploy

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]