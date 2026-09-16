FROM python:3.12-slim

WORKDIR /app

# Installation des outils nécessaires
RUN apt-get update && \
    apt-get install -y \
        git \
        gcc \
        build-essential \
        libffi-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install asyncpg

COPY . .

CMD ["./start.sh"]