# Patchnote Alpha 1.3.2
## Main
Les Modules de commandes se retrouvent désormais dans des dossiers différent, ce qui permet une meilleure lisibilité du dépôt. Tricks effectué par une commande générée par ChatGPT (checkez le fichier `Veronica.py`).

Donc les modules sont indexés dans une variable avant même leur chargement.

> /!\ A noter avec le deplacement des modules

Les modules sont correctement importés par le bot, mais aucun tests du bon fonctionnement de l'importation de ressources depuis ces modules n'a été réalisé. Donc il se peux que le fait qu'ils aient changés de place entraine des erreurs.

> Gestion des erreurs

Une gestion des erreurs en overall est affiché dans le print ainsi que sur Discord via `on_command_error`. Une gestion des exceptions lors de chargement de module a aussi été fait.

Le seul problème de cette méthode, c'est qu'il m'est impossible de savoir à quelle ligne l'erreur s'est produise.

## Jeu : 0.2
Ajout d'un affichage graphique dynamique des statistiques des personnages dans la commande `smasher_info`. Il est prévu qu'une imprémentation des artwork des personnages soient mis tout comme Akuma.

## Dossier Tests
Dossier dédié à mes tests, au lieu de trainer un peu partout..

## RPS
Création du dossier **rps** dédié au jeu 1v1 du RPS

Suite à une requête envoyé, un thread d'une durée de vie de 60 minutes (normalement) est créé, où la majorité de l'affrontement se fera dans ce channel. Ce système sera la base du fonctionnement du jeu avec les persos de Smash Bros là.

Les fonctions Python nécessaires au bon fonctionnement du module `rps.py` sont stockées dans le fichier `rpsFunctions.py`