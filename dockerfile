FROM python:3.12-slim
WORKDIR /app

# Installation des outils nécessaires pour compiler certaines librairies Python
RUN apt-get update && \
    apt-get install -y gcc build-essential libffi-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install asyncpg

COPY . .

# Remplacez par le nom de votre fichier principal si nécessaire
CMD ["python", "veronica.py"]