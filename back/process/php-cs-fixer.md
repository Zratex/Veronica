# CS-Fixer
C'est un programme qui permet de vérifier la validiter d'un code, donc ce n'est pas obligatoire à moins que du développement soit réalisé.
## Installation
```bash
composer require --dev friendsofphp/php-cs-fixer
```
L'IDE peut être modifié afin d'utiliser CS-Fixer.
## Scripts Composer
Plusieurs scripts ont été ajoutés dans `composer.json` pour facilier l'utilisation de CS-Fixer :
- `test:cs` qui lance concrètement cette commande : `php-cs-fixer fix --dry-run`
- `fix:cs` qui lance concrètement cette commande : `php-cs-fixer fix`
- `test` qui lance concrètement cette commande : `@test:cs`
    - L'intéret est d'ajouter dans le futur toutes les commandes de tests à celle ci

ça devrait donner ça :
```json
"scripts": {
    "auto-scripts": {
        "cache:clear": "symfony-cmd",
        "assets:install %PUBLIC_DIR%": "symfony-cmd"
    },
    "post-install-cmd": [
        "@auto-scripts"
    ],
    "post-update-cmd": [
        "@auto-scripts"
    ],
    "test:cs": [
        "php-cs-fixer fix --dry-run"
    ],
    "fix:cs": [
        "php-cs-fixer fix"
    ],
    "test": [
        "@test:cs"
    ]
},
```
> `auto-scripts`, `post-install-cmd`, `post-update-cmd` étaient déjà là