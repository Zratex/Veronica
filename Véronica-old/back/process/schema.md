# Schema
## Maj des schéma
Si la [connexion](/back/process/postgre-connexion.md) est correcte, cette commande permet de mettre à jour la base de données en fonction de la structure du projet Symfony :
```bash
/back/veronica-api/$ php bin/console doctrine:schema:update --force
```