# Installation de PostgreSQL
Après l'[initialisation du dépôt](/back/process/repo-init.md), une base de données est requise. Pour ce projet PostgreSQL a été choisi pour m'entrainer à son installation et sa prise en main, mais surtout pour des raisons de performances car Véronica risque de faire beaucoup de requêtes en parallèle.
## Windows
Après avoir téléchargé l'installateur sur le site officiel. Une fois l'installation lancé, le chemin d'accès de l'installation sera demandé.

Pendant l'installation, un mot de passe sera demandé pour le superadmin. Puis, un port sera à définir.
> **Caractères spéciaux à éviter** dans le mot de passe. Sinon cela risque de causer des problèmes dans l'URL de connexion à Postgre depuis Symfony

Le port par défaut est **5432**

La langue `French - France` a été choisie.
### Lancement sur Windows
Il faut ajouter le chemin à PostgreSQL, plus précisemment le chemin du dossier `bin` de celui ci, dans les variables d'environnements de `PATH`.

Une fois fait, il faut executer cette commande (dans cet exemple j'ai mis **PostgreSQL** à la racine de `D:\`) :
```bash
pg_ctl start -D "D:\PostgreSQL\data"
```
> Si cette commande ne fonctionne pas, il faut soit redémarrer le PC, soit démarrer manuellement via Task Manager le service qui s'appelle `postgresql-x64-16.exe` (16 est le numéro de version)
## Linux
Il suffit de simplement aller dans la console de commande et de l'installer :
```bash
$ sudo apt install postgresql
```

Il faudra probablement redémarrer ce service avec un `systemctl`
# Accéder à Postgre
Maintenant que Postgre est installé, pour vérifier qu'il est correctement installé, il faut s'y [connecter](/back/process/postgre-connexion.md)