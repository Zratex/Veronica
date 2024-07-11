# Symfony first launch
Une fois que PostgreSQL a été correctement configuré avec le `.env.local`, on peut désormais travailler avec Symfony.

Avant cela, cette commande est à executer dans le dépôt :
```bash
/back/veronica-api/$ composer require doctrine/orm doctrine/doctrine-bundle doctrine/doctrine-migrations-bundle
```
## Configuration du driver
Toute action avec la BD ne fonctionnera pas si le driver n'a pas été correctement configuré. Pour cela, il faut trouver le fichier `php.ini` dans l'installation de **PHP**.
> Pour aller plus vite une fois le fichier trouvé, `Ctrl + F` de `;extension=pdo_pgsql`
Une fois la ligne trouvée, il faut retirer le point virgule, puis sauvegarder.
> Sur Linux, cela nécessitera de redémarrer après coup Apache/Nginx/Symfony

Si la commande précédente génère l'erreur `SQLSTATE[42P04]: Duplicate database: 7 ERREUR`, cela veut dire que ça fonctionne correctement.
## Démarrage
Le serveur devrait normalement correctement démarrer avec cette commande :
```bash
/back/veronica-api/$ symfony server
```