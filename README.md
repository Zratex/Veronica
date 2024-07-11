# Véronica
Ce dépôt Github sera le code public de Véronica, que je mettrais de temps en temps à jour pour les curieux d'entre vous qui seraient intéressés par le développement du Bot. Il utilise `discord.py 2.0` pour fonctionner, avec comme back-end `API-Platform` (Symfony) et `PostgreSQL` en base de données.
## Installation
Ce projet nécessite sur le poste en question, l'installation de :
- `discord.py 2.0`
    - Si pas déjà fait, installer `Python`
- [PostgreSQL](/back/process/postgre-install.md)
- `Symfony`
    - Si pas déjà fait, installer `PHP`
    - Si pas déjà fait, installer `Composer`
- Executer cette commande après l'installation de `Symfony` :
```bash
/back/veronica-api/$ composer install
```
- Créer le fichier [.env.local](/back/process/postgre-connexion.md#envlocal)
- Migrer la structure de la base de données : [migration](/back/process/migration.md#application-dune-migration)
## Mises à jour majeures :
### - Alpha 1.2
L'Alpha 1.2 du bot était sous `Discord.py 1.0`.

Tout les fichiers de cette version sont localisés dans le dossier du même nom que la mise à jour, car celle ci n'est plus à jour.
### - Alpha 1.3
Contrairement à l'`Alpha 1.2` qui était sous `Discord.py 1.0`, l'`Alpha 1.3` est sous `Discord.py 2.0`, ce qu'il fait qu'il y a l'intégration des commandes `/`, des boutons et autre.
### - [Current] Alpha 1.4
Réagencement des dossiers pour que ce soit plus lisibles sur Github, mais surtout début de l'implémentation d'un back-end en API platform.
#### Patchnote
Un suivi de patchnote est présent dans le dossier `/patchnotes/` pour plus d'informations sur chaques mises à jours intermédiaires ou mineures.

## Documentation (probablement out-dated)
Documentation du bot : https://docs.google.com/document/d/1K2y5F9WJhgLeOG6MUtEtADuyp7ijQucl5CjRj1WxIQk/edit?usp=sharing

Cette documentation est la liste des commandes/projets prévus avec ce bot Discord.
## 🍜Bol De Nouilles 🍲
Si vous tombez par pur hasard sur ce projet sans savoir ce que c'est, c'est parce que c'est un Bot Discord personnalisé que je créé. Donc si vous n'êtes pas sur le server Discord en question, je vous invite à le rejoindre : https://discord.gg/s6dGnVH

Ah et je viens de me rappeler qu'il faillait que je précise : les coquillettes sont la monnaie du server ; Les Fioris sont les jetons (monnaie spéciale).