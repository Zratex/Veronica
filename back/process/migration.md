# Migrations
C'est pour migrer des données en gros. A noter qu'il faut nécéssairement que le module des entity soit installé, si ce n'est pas déjà fait, il faut l'installer comme décrit dans [entity](/back/process/entity.md)
## Création de migrations
Une migration est une requête SQL. Pour vérifier sa validité, il faut executer cette commande :
```bash
/back/veronica-api/$ php bin/console doctrine:schema:update --complete --dump-sql
```
Une fois fait, pour faire la migration il faut éxécuter cette commande :
```bash
/back/veronica-api/$ php bin/console make:migration
```
La migration sera stockée dans le dossier `/back/veronica-api/migrations/`
## Application d'une migration
Une fois qu'une migration est créée, il faut éxécuter cette commande pour l'appliquer à la base de données :
```bash
/back/veronica-api/$ php bin/console doctrine:migrations:migrate
```