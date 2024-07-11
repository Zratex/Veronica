# Smash Game
Pour l'instant il n'y a pas de nom au jeu en lui même, donc ce sera Smash Game pour le moment.

Ce fichier markdown est présent pour expliquer les règles du jeu en soit, et comment est ce qu'est agencé ce dossier dédié au jeu.

## Smash.py
Le fichier `Smash.py` est le fichier où se trouve les commandes Discord à propos du jeu.

## Base de donnée
Toute la base de donnée relative au bon fonctionnement du jeu est stocké sur la base de donnée générale du bot. Il y a 2 tables prévues pour le moment :
- `smash` : Table dédié aux statistiques des personnages. Pour plus d'informations sur son contenu, il faut check la partie du doc dédié aux **Smasher**
- `smash_attacks` : Table où sont stockées les données relatives aux attaques. Pour plus d'informations sur son contenu, il faut check la partie du doc dédié aux **Attaques**

De celles ci découles des tables de relation :
- `smashAttacksLink` : Table indiquant quel personnage a la capacité d'utiliser un attaque précise. Lien réalisé entre la relation entre la clé attaque et la clé du smasher.
- `smash_combos` : Table où sont stockées les données relatives aux combos que peuvent faire les personnages. Cette table sera probablement une suite de relation de clés entre les attaques  et le personnage

## Smasher
Représentation du personnage en lui même. Défini dans la classe `Smasher` présent dans le fichier **smasher.py**. 

> Construction

Sa construction fait suite à son importation directe dans la base de donnée. De ce fait ses valeures correspondent à ce qu'il y a dans la base de donnée, mais voici tout de même une description de ces éléments :
### Elements de la classe Smasher
> Identification
- `number` : Numéro identifiant le personnage. Clé primaire du concept dans la base de donnée. Correspond au nombre attribué dans le jeu Super Smash Brothers. Ultimate (2018 Nintendo, Sora | Bandai Namco), soit par ordre d'apparition dans la license. Cependant ce nombre sera trié d'une certaine manière :
```
10010

Explication du code
1) pour éviter que Python fasse des erreurs bizarres
2-3-4) numéro identifiant le personnage. Dans cet exemple ça correspondrait à Mario
5) Si c'est un 1 c'est un echo fighter, si c'est autre qu'un 0 ce sera un skin
```
- `name` : Nom du personnage. L'utilisateur se référa plus facilement au nom qu'à son nombre.
> Statistiques
- `PV` : Point de vie du personnage
- `attack` : Défini en général le nombre de dégâts que mettra le personnage lors d'une attaque
- `defense` : Défini à quel point le personnage tankera l'attaque adverse
- `speed` : Défini la priorité de tour par rapport à son adversaire (le plus haut joue en premier)
- `dexterity` : Défini le pourcentage de chance que le personnage réussisse un combo entre chaque coup
- `reach` : Portée du personnage. Quand le combat est en mode "*à distance*", c'est le pourcentage de chance que le personnage touche son adversaire
- `altDMG` : Défini les dégâts que font des attaques de type projectile, ou ceux d'une attaque lors de l'execution d'un combo
### Méthodes
> Getters
- `getStats(self)` : Transforme l'objet en une instance sous forme de dictionnaire

A partir de ce trick, toutes les fonctions **get** pour obtenir les informations des statistiques du personnages retournent juste le contenu de `getStats(self)` avec comme indice de dictionnaire le nom de la statistique.

Exemple :
```
#Syntaxe :
perso.getStats(self)[nom de notre statistique en string]
#Pour obtenir les PV :
perso.getStats(self)['PV']
```
J'aurais pu me tenir à garder cette syntaxe, mais c'est plus simple de faire des fonctions get pour absolumentes tout les éléments.

## Attaques
Représentation des attaques en elles mêmes. Défini dans la classe `Move` présent dans le fichier **attacks.py**. 

> Construction

Sa construction fait suite à son importation directe dans la base de donnée. De ce fait ses valeures correspondent à ce qu'il y a dans la base de donnée, mais voici tout de même une description de ces éléments :
### Elements de la classe Move
- `num` (**int**) : Identifiant de l'attaque
- `name` (**str**) : Nom de l'attaque
- `type` (**int**) : Type de l'attaque, pouvant varié entre 1,2 et 3.
    <u>Description des types :</u>
    - 1 : Attaque physique classique
    - 2 : Projectile
    - 3 : Passif. Donc cette attaque ne peux pas vraiment être choisi par le joueur, elle s'activera automatiquement
- `stunPOURCENTAGE` (**int**) : Valeur sur 100 parce que c'est un pourcentage. Pourcentage de chance que l'adversaire soit sous état de stun, donc qu'il ne puisse pas agir le prochain tour
- `pushingPOURCENTAGE` (**int**) : Valeur sur 100 parce que c'est un pourcentage. Pourcentage de chance que l'adversaire soit éjecté, donc que le combat passe en mode à distance
- `spikePOURCENTAGE` (**int**) : Valeur sur 100 parce que c'est un pourcentage. Pourcentage de chance que le coup ait l'effet de spike durant un combo. Pour rappel cet effet augmente de 10 dégâts
- `loading` (**int**) : Nombre de tour que prends l'attaque pour se charger
- `savable` (**bool**) (mais int parce que euh ouais) : Censé être un booléen mais est sauvegardé comme un int dans le SGBD parce que pourquoi pas je suppose ?
    - 0 : Le coup ne peut pas être "sauvegardé"
    - 1 : Le coup peut être sauvegardé pour être réutilisé plus tard
- `Accuracy` (**int**) : L'accuracy se stack sur le pourcentage de chance de toucher via la portée. Valeur sur 100 parce que c'est un pourcentage
    
    Si c'est de 0, l'attaque n'est pas affecté par cette règle, donc seul la portée détermine si elle va toucher ou non
    
    Si la valeur est de 100, le coup touche dans tout les cas
- `Description` (**str**) : Description du coup
- `setDMG` (**int**) : Si NULL : l'attaque fera le même nombre de dégâts que les statistiques du perso. Si c'est un projectile, il fera le nombre de dégâts que la statistique altDMG
    
    Si non NULL : l'attaque fera le nombre de dégâts indiqué
- `armor` (**int**) : Nombre de tour selon laquelle le personnage sera invincible. Commence dès le tour où l'attaque est employé.
    
    Donc si une attaque a un tour d'armor, pendant le tour où le joueur va sélectionner l'attaque il sera invincible.

### Méthodes
- `getStats(self)` : Transforme l'objet en une instance sous forme de dictionnaire

Pour toutes les autres méthodes **get**, le trick est le même que pour la classe `Smasher`. Si référé pour comprendre le fonctionnement.