FROM python:3.12-slim

# Installation de git pour cloner le repo
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Clone spécifiquement la branche alpha-1.5
RUN git clone -b alpha-1.5 https://github.com/Zratex/Veronica.git .

# Installation des dépendances (assurez-vous d'avoir un requirements.txt dans votre repo)
# S'il n'y en a pas, listez les packages manuellement ex: RUN pip install discord.py asyncpg
RUN pip install -r requirements.txt
RUN pip install asyncpg 

# Remplacer "main.py" par le nom réel de votre fichier de lancement
CMD ["python", "main.py"]