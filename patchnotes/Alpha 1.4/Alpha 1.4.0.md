# Patchnote Alpha 1.4.0
Le backend du bot se retrouve entièrement refait. En effet, une API sous API Platform a été mise en place dans le dossier `/back/`, et le précédent code a été mis dans le dossier `/Véronica/` pour une meilleure lisibilité sur le dépôt Github.
## Structuration des dossiers back
Le dossier `/back/process` est rempli de fichiers markdown pour expliquer les étapes qui ont été réalisées. L'idée est de plus facilement les reproduire si il y a besoin de les reproduire pour plus tard.

> Ce qu'il fait que le vrai contenu du back est dans `/back/veronica-api/`
## Serveur
Un serveur va être prévu qui va hoster toute l'API. Pour plus d'informations sur sa structure, voir la note de [structuration du serveur](/back/README.md#structure-réseau-du-serveur).

Le début du développement de cette Alpha 1.4.0 était plus centré sur la mise en place du serveur, mais désormais l'objectif va être de mettre en place une API fonctionnelle avant de s'occuper du serveur et des dockerfiles.