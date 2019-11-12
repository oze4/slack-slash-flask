FROM python:3.7-slim

ARG PORT
ENV PORT=${PORT}

WORKDIR /
COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --clear

COPY . .

EXPOSE ${PORT}

CMD ["python", "app.py"]