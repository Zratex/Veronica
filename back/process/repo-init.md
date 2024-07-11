# Repo-init
Ce fichier markdown explique comment est ce que ce projet a été initialisé.
## Pré-requis
Sur mon PC, `Composer`, `PHP` et `Symfony CLI` avaient déjà été correctement installés. Pour la suite de ce document, il faut bien évidemment les avoir d'installés.

Ne pas oublier de mettre à jour composer :
```bash
$ composer self-update
```
## Initialisation Symfony
Une fois placé dans le dossier cherché avec la console de commande, il faut executer celle ci :
```bash
$ symfony new NOMDUPROJET
```
## Installation d'API Platform
Une fois le projet Symfony fait, il faut se placer à l'endroit du projet :
```bash
$ cd NOMDUPROJET/
```

Puis installer API Platform avec cette commande :
```bash
NOMDUPROJET/$ composer require api
```

Durant l'installation, il va demander si il doit inclure une configuration **Docker**. Pour le moment je n'en ait pas besoin, donc j'ai simplement mis non.