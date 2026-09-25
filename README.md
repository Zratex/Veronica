<div align="center">

  # Véronica

  Bot Discord ayant pour objectif (à l'origine) de répondre aux besoins du serveur Discord Bol de Nouilles.

  [![Python Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fveronica.jabneel.fr%2Fstatus&label=&query=%24.versions.python&logo=python&logoColor=white&labelColor=green&color=gray)](https://www.python.org/)
  [![discord.py](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fveronica.jabneel.fr%2Fstatus&label=discord.py&query=%24.versions%5B%22discord.py%22%5D&color=gray&labelColor=blue)](https://github.com/Rapptz/discord.py)
  [![dPyStatus](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fveronica.jabneel.fr%2Fstatus&label=dPyStatus&query=%24.versions.dPyStatus&color=gray&labelColor=orange)](https://github.com/PaulBayfield/dPyStatus)
</div>

# 🗃️Sommaire
- [🖥️Déploiement du bot](#déploiement)
- [📋Liste des mises à jours majeures](#liste-des-mises-à-jour-majeures)
- [📚Documentation (encore à rédiger)](#documentation)
- [🍜Le serveur Discord Bol de Nouilles](#bol-de-nouilles-)


# 🖥️Déploiement
Le déploiement se réalise via conteneur Docker. Personnellement j'utilise Portainer en tant qu'orchestrateur.

- Créez une stack Docker en mode Github :
  - Pointez le dépôt Github (https://github.com/Zratex/Veronica.git)
  - Pointez la branche de votre choix (pour `main` ce serait `refs/heads/main`)
  - Pointez le chemin du docker compose (ici puisse qu'on est à la racine, ce sera simplement `docker-compose.yml`)
- Définissez les variables d'environnement :
  - `DISCORD_TOKEN`
  - `POSTGRE_PASSWORD`
# 📋Liste des mises à jour majeures
## - [Current]  Alpha 1.5
- Reprise du projet pour que ce soit plus propre, en particulier sur l'aspect déploiement (je n'avais pas d'infrastructures jusque là)
- Ajout de tests unitaires, avec des Github Actions
- Ajout du jeu du Tamagotchi (pour le moment n'a pas d'intérêt)
- Ajout des git tags

Objectif : mettre en place un environnement de développement et déploiement sain avant de commencer un développement plus profond des fonctionnalités complexes prévues pour ce bot Discord.

> L'API Symfony a pour le moment été abandonné. L'implémentation d'une vrai API se fera plus tard
## - Alpha 1.4
Réagencement des dossiers pour que ce soit plus lisibles sur Github, mais surtout début de l'implémentation d'un back-end en API platform.
## - Alpha 1.3
Contrairement à l'`Alpha 1.2` qui était sous `Discord.py 1.0`, l'`Alpha 1.3` est sous `Discord.py 2.0`, ce qu'il fait qu'il y a l'intégration des commandes `/`, des boutons et autre.
## - Alpha 1.2
L'Alpha 1.2 du bot était sous `Discord.py 1.0`.

Tout les fichiers de cette version sont localisés dans le dossier du même nom que la mise à jour, car celle ci n'est plus à jour.

# 📚Documentation
Cette documentation est la liste des commandes/projets prévus avec ce bot Discord.

Documentation du bot : (`documentation encore à rédiger`)
# 🍜Bol De Nouilles 🍲
Si vous tombez par pur hasard sur ce projet sans savoir ce que c'est, c'est parce que c'est un Bot Discord personnalisé pour mon serveur discord du nom de Bol de Nouilles.

Donc si vous n'êtes pas sur le server Discord en question, je vous invite à le rejoindre : https://discord.gg/s6dGnVH

> Puisse que ce serveur est "Bol de Nouilles", **c'est la raison pour laquelle les coquillettes sont la monnaie du server, et les Fioris sont la monnaie spéciale**.