# Entity
Une entité est une représentation dans le système de Symfony d'un objet (bien souvent une table) qui est stocké dans la base de données. C'est pratique car au lieu de faire des requêtes SQL en Postgre pour intéragir avec la base de données, on va juste faire des actions sur une classe PHP.
> Il faut donc que la base de données soit correctement mise en place : étape d'[installation](/back/process/postgre-install.md) et étape de [connexion](/back/process/postgre-connexion.md)
## Installation d'entity
Pour installer le concept des entités, il faut executer cette commande :
```bash
/back/veronica-api/$ composer require --dev symfony/maker-bundle
```
## Création d'une entité
Pour créer une entité (donc créer une table), il suffit d'executer cette commande :
```bash
/back/veronica-api/$ php bin/console make:entity
```
A noter qu'une fois que la commande sera éxécutée, un questionnaire se fera dans la console. C'est pour générer chaque champ de la table, donc il faut au préalable savoir ce que l'on créer.

Quelques directives pour les champs :
- Je sais que c'est pas opti, mais on va dire que tout les `string` seront de type `text`
- Les `int` sont des `integer`
- Toutes les dates seront de types `datetime`

Une fois l'entitée de créer, il faut l'implémenter dans la base de données en faisant une [migration](/back/process/migration.md)