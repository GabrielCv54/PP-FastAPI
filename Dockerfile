FROM python:3.11-slim

WORKDIR /finance_api

COPY requirements.txt .

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY . .

EXPOSE 8000

CMD ["uvicorn","main:app","--reload"]