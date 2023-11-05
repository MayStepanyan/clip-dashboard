FROM python:3.10.13-slim-bullseye

RUN apt upgrade -y && apt update -y

RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY . .

RUN poetry install

ARG PORT

ENTRYPOINT python -m streamlit run dashboard/main.py --server.port $PORT
