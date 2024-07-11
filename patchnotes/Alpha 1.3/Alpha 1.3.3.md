# Patchnote Alpha 1.3.3
## Main
Les problèmes que j'ai eut avec la création des threads sur le module RPS (plus d'infos dans le code en lui même) ont réalisé pas mal de réaction sur le serveur Discord de Discord.py. 

Parmis les manipulations pour comprendre le problème que j'avais (qui n'a toujours pas été résolu donc je garde mon trick), j'ai ajouté une ligne qui affiche le traçage des erreurs dans la console de commande.

## Base de donnée
> importation de la base de donnée

Le fichier `database.py` fonctionne désormais avec les chemins relatifs. Plus besoin de changé le chemin d'importation de la base de donnée.

Les chemins relatifs par défaut de Python ne fonctionnaient pas pour une raison dont j'ignore, donc j'ai dû m'être obligé de changer à chaque fois manuellement leur chemin.

Ce problème a été réglé avec la librairie`os` de Python.

> Graphes économiques

Des modifications aux fonctions dédiés à la génération des graphes économiques ont été réalisées. Plus d'informations dans la sous-catégorie **graphes économiques** de la catégorie **économie**
## Account
> Déplacement d'account.py

Le fichier a été déplacé dans `/account/account.py` pour une meilleure lisibilité

> Suppression de /shop

La commande shop a été retranscrise dans le fichier `/economy/shop.py` pour des raisons qui sont évoqués dans sa catégorie dédié de ce patchnote.

## Economie
Tout ce qui sera lié à l'économie sera stocké dans ce dossier pour le futur. C'est plus clair d'avoir un fichier par commande au vu de leur complexité, que de tout d'avoir de réunir dans un fichier comme `account.py`. Donc pour le moment son contenu contient les résidus de ce que faisait déjà `account.py`.
### Shop
> account.py

La fonction du shop a été mise à part du fichier `account.py`, qui est placé dans le dossier **economy**.

### Graphes économiques
> account.py

La commande `/economy_graph` a été tirée du fichier `account.py` pour être placé dans le fichier `/economy/economy_graph.py`.

> Stockage des graphiques

Quand une image est générée avec **MatPlotLib** ou **PIL**, si on ne spécifie pas l'emplacement où elle doit être stockée, elle se retrouve enregistré à l'endroit où le fichier de base qui est executé, est stocké. Comme le fichier de base qui execute tout ceci est `Veronica.py`, les images se retrouvaient dans la racine du dépôt.

```
L'objectif depuis la dernière mise à jour est à long terme répartir de plus en plus les fonctions afin que ce l'arboraissance du dépôt soit plus lisible. Ceci permet de suivre cette démarche, en permettant de retirer l'encombrement présent à la racine du dépôt.

La prochaine état serait de pouvoir rediriger le fichier output.png autre part
```

Ce problème a été réglé exactement de la même manière que celui de l'importation de la base de donnée : via la librairie `os` de Python. Le changement a été réalisé à la fois au niveau de la génération de l'image (dans `/database/database.py`) mais aussi dans son importation pour l'affichage sur Discord (`/economy/economy_graph.py`)

- A noter que les graphiques sont toujours à retravailler, donc des changements sont à prévoir pour les prochaines mises à jours
## RPS
> nom des threads

Inversion entre le temps et l'indication des noms de joueurs, pour le nom de création du thread dédié à une partie.