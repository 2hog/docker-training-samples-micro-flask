FROM python:3.7

RUN pip install pipenv==2018.11.26

ENV FLASK_APP=app
WORKDIR /usr/src/app

COPY Pipfile Pipfile.lock ./

ARG pipenv_mode=deploy
RUN pipenv install --system --${pipenv_mode:-deploy}

COPY . .

CMD ["flask", "run", "--host", "0.0.0.0"]