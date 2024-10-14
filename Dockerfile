FROM python:latest

WORKDIR /app

COPY SalesTransactions.py .

CMD python SalesTransactions.py