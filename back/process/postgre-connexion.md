# Accéder à Postgre
Il faut tout d'abord que Postgre soit [installé](/back/process/postgre-install.md)
## Console de commande
Pour accéder à la console postgre, il faut entrer la commande :
```bash
$ psql -U postgres
```
Le mot de passe de l'utilisateur `postgre` sera demandé, défini lors de l'étape [repo-init.md](/back/process/repo-init.md)
## .env.local
En premier lieu, il faut créer le fichier `.env.local` qui est une copie de `.env` dans la racine de l'API, càd dans le dossier `/back/veronica-api/`.

Ensuite, il faut remplacer le contenu du `DATABASE_URL` :
```
DATABASE_URL="postgresql://app:!ChangeMe!@127.0.0.1:5432/app?serverVersion=16&charset=utf8"
```
A savoir que :
- `//app` est le **nom** de l'utilisateur (`//` est à garder)
- `!ChangeMe!` est le **mot de passe** de l'utilisateur (`!` ne sont **pas à garder**)
- `127.0.0.1` est l'**adresse** ip du serveur PostgreSQL (127.0.0.1 est l'ip par défaut quand il est en localhost)
- `5432` est le **port** défini lors de l'[installation](/back/process/postgre-install.md) du serveur Postgre
- `app?` est le nom de la **base de données** (`?` est à garder)
    - Si aucune bases de données existent, il faut se connecter manuellement à la console de commande Postgre. Une fois fait, il faut executer cette commande :
    ```sql
    CREATE DATABASE veronica;
    ```
    - `veronica` sera le nom de la base de données **par défaut** pour ce projet
- `serverVersion=15` est la **version** de Postgre. Le projet sera sous la **version 15** car les autres ne sont pas disponibles par défaut sur Debian
    - Probablement voué à changer dans le futur