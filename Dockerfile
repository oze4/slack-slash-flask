FROM python:3.7-slim

ARG PORT
ARG SLACK_VALIDATOR_URL

ENV PORT=${PORT}
ENV SLACK_VALIDATOR_URL=${SLACK_VALIDATOR_URL}

WORKDIR /
COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv
RUN pipenv install --system --clear

COPY . .

EXPOSE ${PORT}

CMD ["python", "app.py"]