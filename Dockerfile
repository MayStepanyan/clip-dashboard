FROM python:3.10.13-slim-bullseye

RUN apt upgrade -y && apt update -y

RUN pip install poetry

COPY . .

RUN poetry install

ENTRYPOINT python -m streamlit run dashboard/main.py