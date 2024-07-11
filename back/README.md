# Veronica API
API dédié pour les actions qui seront executées sur le système de Véronica. L'idée est que le système permettant de connecter le site web ainsi que Véronica soient les mêmes.

## Description des dossiers
> `/veronica-api`

Ce dossier contient tout le code de l'API

> `/process`

Ce dossier documente les actions qui ont été réalisées pour la mise en place de certaines choses au travers de ce projet. Il sert simplement d'index pour les développeurs.
## Struture de la BD
Voici une sorte de MCD/MLD mais en markdown de la structure de la base de données qui sera utilisée par **Véronica**.

A noter qu'un diagramme de classe mermaid est utilisé pour plus facilement se visualier la structure BD, donc les fonctions ne sont pas des fonctions mais plutôt des **clés étrangères**. Les fléches signifient que leur clé primaire est utilisée en tant que clé étrangère dans une autre table. Les flèches vides ont comme restriction `ON DELETE CASCADE`
```mermaid
---
title : Structuration de la BD
---
classDiagram
    class user {
        -int id_discord PK
        -int money
        -date creation_date
        -date daily_cooldown
        -int xp
        +int level()
        -int stock_conchiglie
        -int stock_lootbox
    }
    class bank {
        -int bank_id PK
        -int coquilette_stocks
        -int conchiglie_stocks
        -int cours_conchiglie
        -date temps
    }
    class levels {
        -int level PK
        -int xp_required
        -string role_name
    }
    class apilogs {
        -int apilogs_id PK
        -string origin
        -string method
        -string route
        -date time
    }

    levels --> user
```
### Description des tables
Voici la description et les détails de chacunes des tables
#### user
Représente un utilisateur, identifié par son identifiant Discord.
- `money` : Quantité d'argent qu'à en stock un utilisateur
- `creation_date` : Date de création du compte de l'utilisateur dans la base de données de Véronica
- `daily_cooldown` : Date du dernier `/daily` qu'a réalisé l'utilisateur. Permet de calculer depuis combien de temps il n'a pas fait de commande `/daily`
- `xp` : quantité d'xp accumulée par l'utilisateur
    - 0 est la valeur par défaut et minimum
- `level` : représente le niveau actuel du joueur. C'est une clé étrangère, afin de pouvoir facilement obtenir son nom
- `stock_conchiglie` : Nombre de conchiglie qu'a un utilisateur
- `stock_lootbox` : Nombre de lootbox qu'a un utilisateur
#### bank
Représente la banque du système. Chaque ligne est une trace écrite du cours des stocks de la banque en fonction de la date.
- `bank_id` : histoire d'avoir une clé primaire, ça peut toujours être utile
- `coquilette_stocks` : représente le nombre de coquilettes encore en stock
- `conchiglie_stocks` : représente le nombre de conchiglie encore libre d'achat
- `temps` : c'est simplement un chant où la ligne a été écrite
#### apilogs
Journeaux des requêtes qui ont été faites à l'API.
- `apilogs_id` : histoire d'avoir une clé primaire, ça peut toujours être utile
- `origin`: précise l'origine de la requête
    - `web` si ça provient du site qui est basé sur cette API
    - `veronica` si c'est une requête faite par Véronica
    - Autrement ce sera directement l'ip de la requête. Il faudrait faire en sorte que les ip ne soient pas directement retournées par un get
- `method` : Méthode HTTP utilisée pour l'action
- `route` : Ressource demandée par la requête
- `time` : Quand est ce que cette requête a été faite