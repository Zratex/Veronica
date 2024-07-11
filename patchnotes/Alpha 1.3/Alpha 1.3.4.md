# Patchnote Alpha 1.3.4
En vrai je suis même pas sur d'avoir tout détaillé dans cette mise à jour. Mais ouais voilà ce qui a été modifié :
# Main
Création d'une fonction qui permet d'avoir le numéro de version du bot. Il est stocké dans `/Version.txt`. Le fichier `/Version.py` contient une fonction permettant d'extraire directement le contenu du fichier `Version.txt`. Normalement tout les fichiers ont été mis à jour pour supporter cette fonctionnalité.

Le fichier `liste_inscrits.json` s'est retrouvé dans la racine, sinon il ne fonctionnait pas pour une raison que j'ignore.

# RPS
Changements dans la manière dont le bot réponds, ce qui évite d'afficher des erreurs à l'utilisateur alors qu'il n'y en a pas. C'est assez technique donc je vous invite à regarder les modifications entre les 2 versions.

# Economy
## Changement économique
> Conchiglie

Il y a une volonté de baisser les prix des **conchiglie**, parce qu'autrement l'ouverture d'une lootbox reviendrait à très chère.

Voici les résultats de recherches obtenues sur la quantité d'argent requis pour l'ouverture d'une lootbox, dans le cas où l'argent de la banque centrale soit par défaut (càd à 1M) avant de le début de l'opération, et que personne d'autre ne dédienne de **conchiglie** :
| Nombre de Jetons en circulation | Prix de base | Prix de l'ouverture d'une lootbox |
| :-: | :-: | :-: |
| 100 | 10 000 | **35 305** (système prévu de base)|
| 200 | 5 000 | 5k+5050+5101`+5000`= **20 151** |
| 500 | 2 000 | 2k+2183+2193`+5000`= **11 376** |
| 1 000 | 1 000 | 1k+1002+1004`+5000` = **8 006** |

Le `+5000` représente le prix d'une lootbox.

On a donc décidé de repenser le **calcul du conchiglie** :
- Il y aura **200** Conchiglie disponibles par défaut
- Il faudra désormais **qu'un seul** conchiglie pour ouvrir une `lootbox`
- Un système de "péremption" sera réalisé. C'est à dire qu'un utilisateur ne pourra pas garder définitivement un conchiglie dans son inventaire, pour éviter que le marché soit bloquer par quelqu'un ayant décidé d'acheter tout les jetons

Mis à part pour le système de "péremption", ces fonctionnalités ont été intégré à cette version **Alpha 1.3.4**.

L'ouverture d'une lootbox reviendrait simplement à acheter une box + un **Conchiglie**, ce qui est plus simple à calculer auprès de l'utilisateur. Dans les mêmes conditions que le tableau précédent, la première lootbox coûterait `5k+5k=`**10 000 coquilettes**.
## Commandes ajoutées/modifiées
> economy_refresh

Cette commande permet d'actualiser manuellement le cours de la bourse

> economy_graph

Petites corrections dans les programmes par rapport au système économique, ainsi que l'ajout de la fonction `ShowJetonStockGraph` pour générer l'affichage des stocks de jetons.

**Le fonctionnement des fonctions de génération de graphiques a été changé :**

Elles font toutes appel à la fonction `Economy_graph` qui va s'occuper de générer le graph en selon la fonction. Elle est identifiée grâce à la fonction `typeGraphe`. Ce qu'il fait qu'au lieu d'avoir 3 programmes similaires, tout est réuni en un seul. Il se base donc sur ce qui existait déjà, mais avec certaines modifications :
- La notation des ordonnées n'est désormais plus scientifique
- L'affichage des dates a été réglé en les transformant en objet **date**
- Seulement certaines dates sont affichées, pas toutes contrairement à avant
- Les graphes ne se supperposent plus comme avant. Càd que de temps en temps une courbe se créait juste sur la précédente, ce qui cosait des bugs visuels

Fix de bug : de temps en temps un graphique généré se supperposait sur un autre déjà existant, ce qui faisait bugger l'affichage. C'est normalement régler avec l'ouverture et la fermeture d'une figure avec matplolib.

Exemple de graph :
![graph_example.png](../Database/graph_jeton.png)
# Shop
2 items ont été mis : achat de **lootbox** ou de **conchiglie**. Leur achat actualise en temps réel le cours économique, tout comme le prix du **conchiglie**
# Lootbox
Création d'un module dédié à la commande `/lootbox`. Elle affiche les informations de l'utilsateur à propos de la lootbox, et c'est via ce menu qu'il peux décider d'en ouvrir une.

Une fois une box ouverte, les jetons redeviennent libre en circulation. Cette actualisation est faite automatiquement.

## Changements sur l'ouverture d'une lootbox
Certains changements ont été fait par rapport au nombre de **Conchiglie** requis pour l'ouverture d'une lootbox. Pour plus d'informations, veuillez lire le segment de ce patchnote dédié aux **Conchiglie**.

## Répartition des loots de la lootbox
A savoir que pour le second jet, ça n'a pas encore été implémenté. C'est prévu pour la **Alpha 1.3.5**
> Premier jet : argent

| Pourcentage de chance | Argent remporté |
| :-: | :-: |
| 1% | 100 000 |
| 4% | 50 000 |
| 5% | 30 000 |
| 10% | 20 000 |
| 15% | 10 000 |
| 30% | 5 000 |
| 35% | 1 000 |
> Second jet : récompenses (pas encore implémentée)

| Pourcentage de chance | Récompense remportée |
| :-: | :-: |
| 30% | 1 Lootbox |
| 25% | 1 Conchiglie |
| 20% | Autorisation d'avoir un rôle perso (Ou de le modifier). Autorisation ayant 48h avant d'être épuisée |
| 10% | Obtention du `drip role` (Si déjà acquis, +20k coquillettes) |
| 10% | Obtention d'un fond de profile aléatoire (Si déjà acquis, +25k coquillettes) |
| 3% | Obtention d'un GPU aléatoire de la génération suivante (Si nous sommes déjà à la dernière génération, meilleur GPU du marché remporté) |
| 2% | Obtention d'un personnage aléatoire (Si déjà acquis, +100k coquilletes) |