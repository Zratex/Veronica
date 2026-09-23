# Véronica
Ce dépôt Github sera le code public de Véronica, que je mettrais de temps en temps à jour pour les curieux d'entre vous qui seraient intéressés par le développement du Bot.

Il utilise :
- `discord.py 2.0` pour fonctionner
- back-end : (encore à définir)
- `PostgreSQL` en base de données
## Déploiement
Le déploiement se réalise via conteneur Docker. Personnellement j'utilise Portainer en tant qu'orchestrateur.

- Créez une stack Docker en mode Github :
  - Pointez le dépôt Github (https://github.com/Zratex/Veronica.git)
  - Pointez la branche de votre choix (pour `main` ce serait `refs/heads/main`)
  - Pointez le chemin du docker compose (ici puisse qu'on est à la racine, ce sera simplement `docker-compose.yml`)
- Définissez les variables d'environnement :
  - `DISCORD_TOKEN`
  - `POSTGRE_PASSWORD`
## Mises à jour majeures :
### - [Current]  Alpha 1.5
- Reprise du projet pour que ce soit plus propre, en particulier sur l'aspect déploiement (je n'avais pas d'infrastructures jusque là)
- Ajout de tests unitaires, avec des Github Actions
- Ajout du jeu du Tamagotchi (pour le moment n'a pas d'intérêt)
- Ajout des git tags

Objectif : mettre en place un environnement de développement et déploiement sain avant de commencer un développement plus profond des fonctionnalités complexes prévues pour ce bot Discord.

> L'API Symfony a pour le moment été abandonné. L'implémentation d'une vrai API se fera plus tard
### - Alpha 1.4
Réagencement des dossiers pour que ce soit plus lisibles sur Github, mais surtout début de l'implémentation d'un back-end en API platform.
### - Alpha 1.3
Contrairement à l'`Alpha 1.2` qui était sous `Discord.py 1.0`, l'`Alpha 1.3` est sous `Discord.py 2.0`, ce qu'il fait qu'il y a l'intégration des commandes `/`, des boutons et autre.
### - Alpha 1.2
L'Alpha 1.2 du bot était sous `Discord.py 1.0`.

Tout les fichiers de cette version sont localisés dans le dossier du même nom que la mise à jour, car celle ci n'est plus à jour.

## Documentation (out-dated)
Documentation du bot : (`à développer`)

Cette documentation est la liste des commandes/projets prévus avec ce bot Discord.
## 🍜Bol De Nouilles 🍲
Si vous tombez par pur hasard sur ce projet sans savoir ce que c'est, c'est parce que c'est un Bot Discord personnalisé que je créé. Donc si vous n'êtes pas sur le server Discord en question, je vous invite à le rejoindre : https://discord.gg/s6dGnVH

Puisse que ce serveur est "Bol de Nouilles", c'est la raison pour laquelle les coquillettes sont la monnaie du server, et les Fioris sont les jetons (monnaie spéciale).