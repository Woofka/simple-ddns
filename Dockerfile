FROM python:3.8.5-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir flask

COPY ./ddns-server.py .

ENTRYPOINT ["python3", "ddns-server.py"]