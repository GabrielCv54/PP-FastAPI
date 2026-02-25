FROM python:3.11-slim

WORKDIR /finance_api

RUN apt-get update && apt-get install -y libpq-dev gcc

