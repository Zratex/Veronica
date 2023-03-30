# Patchnote Alpha 1.3.1
Création d'un dossier permettant d'avoir un suivi des mises à jour du bot, utile principalement pour les ajouts dans le mode de jeu qui sera intégré à Véronica.

Dû au fait que ça fait un moment que le projet n'a pas été commit, cette mise à jour est plutôt assez massive en réalité. Mais les prochaines le seront bien moins.
## Economie
Début d'implémentation de l'économie au niveau de la base de donnée. Pour le moment les seules choses qui ont été implémentées sont :
- Le fait qu'un utilisateur puisse **retirer** de l'argent auprès de la banque et qu'elle le comptabilise, notamment auprès de la commande `/daily` qui est fonctionnelle
- Le fait que la banque centrale **existe**
- Le calcul du jeton (**Fiori**) est fait dynamiquement
La commande `/economy_graph` est fonctionnelle, mais l'affichage du graphe en lui même est à revoir : l'indication des dates est mal fait.

## Profile
Le profile affiche désormais les informations relatives au système économique, ainsi qu'une barre de progression dynamique de l'xp de l'utilisateur. Pour le moment le fichier dédié à la génération de l'image se nomme `Media/test.py`, donc il est à renommer et prograblement à remanier.

De ce fait, techniquement le système d'xp devrait être fonctionnel grâce au module `xp.py`.

A propos de la **génération d'images**, vu que le programme est executé depuis la racine du dépôt, les images sont générés dans la racine. Ce qu'il fait que tout est stocké au même endroit et ça fait un peu moche. Ce sera probablement fixé lors de la prochaine mise à jour.

## Jeu : 0.1
Début d'implémentation du jeu. Pour le moment il y a que la commande `/smash_info` qui est disponible, permettant de voir les attributs ainsi que les attaques des personnages avec leurs icônes (stockées sous format png dans `Smash/Media/Stock Icons/`)

La conception des personnages et des attaques sont construites dans les fichier `Smash/smasher.py` et `Smash/attacks.py` depuis l'importation d'informations de la base de données.

-> plus de précisions dans le fichier `Smash/game.md`.

Pour le moment seul les personnages présent au départ de la fiction Ultimate Brawl : The Universe of Light sont disponibles dans le jeu.

## Prévu pour le patchnote Alpha 1.3.2
### Jeu : 0.2
Ce qui est prévu prochainement est d'ajouter les données relatives à propos des combos d'attaques, puis programmer un début de jeu en lui même. Il n'y a toujours pas de solution permettant de faire de façon intuitive et dynamique un système de **1vs1 via Discord.py**. En attendant, le jeu en lui même sera programmé pour tester si le principe fonctionne bien ou non.

Au niveau de l'affichage des informations en elles mêmes, il y en a trop dans un seul embed alors que ça rend déjà très mal sur mobile. Donc ce qui est prévu c'est une génération d'image au moins pour les statistiques des personnages.