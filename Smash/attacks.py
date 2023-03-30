#Importation des fonctions pour communiquer avec la base de donnée
from Database import database

#Concept des attaques des Smasher (personnage du jeu de Véronica)
class Move:
    """Classe représentation un personnage du jeu. Ses stats sont importées de la base de donnée"""
    def __init__(self,number):
        stats=database.getAttackFromID(number)
        self.num=stats[0]
        self.name=stats[1]
        self.type=stats[2]
        self.stunPourcentage=stats[3]
        self.pushingPourcentage=stats[4]
        self.spikePourcentage=stats[5]
        self.loading=stats[6]
        if stats[7]:
            self.savable=True
        else:
            self.savable=False
        self.accuracy=stats[8]
        self.description=stats[9]
        self.setDMG=stats[10]
    def getStats(self):
        """Retourne les statistiques de l'attaque sous forme de dictionnaire"""
        return self.__dict__
    def getName(self):
        """Retourne le nom de l'attaque"""
        return self.getStats()['name']
    def getDescription(self):
        """Retourne la description de l'attaque"""
        return self.getStats()['description']
    def getType(self):
        """Retourne le type de l'attaque"""
        return self.getStats()['type']
    
# Description du concept d'attaque :
#  - num : int
# Identifiant de l'attaque
#
# - name : str
# Nom de l'attaque
#
# - type : int
# Type de l'attaque, pouvant varié entre 1,2 et 3. Description des types :
#   - 1 : Attaque physique classique
#   - 2 : Projectile
#   - 3 : Passif. Donc cette attaque ne peux pas vraiment être choisi par le joueur, elle s'activera automatiquement
#
# - stunPOURCENTAGE : int
# Valeur sur 100 parce que c'est un pourcentage. Pourcentage de chance que l'adversaire soit sous état de stun, donc qu'il ne puisse pas agir le prochain tour
#
# - pushingPOURCENTAGE : int
# Valeur sur 100 parce que c'est un pourcentage. Pourcentage de chance que l'adversaire soit éjecté, donc que le combat passe en mode à distance
#
# - spikePOURCENTAGE : int
# Valeur sur 100 parce que c'est un pourcentage. Pourcentage de chance que le coup ait l'effet de spike durant un combo. Pour rappel cet effet augmente de 10 dégâts
#
# - loading : int
# Nombre de tour que prends l'attaque pour se charger
#
# - savable : bool (mais int parce que euh ouais)
# Censé être un booléen mais est sauvegardé comme un int dans le SGBD parce que pourquoi pas je suppose ?
#   - 0 : Le coup ne peut pas être "sauvegardé"
#   - 1 : Le coup peut être sauvegardé pour être réutilisé plus tard
#
# - Accuracy : int
# L'accuracy se stack sur le pourcentage de chance de toucher via la portée. Valeur sur 100 parce que c'est un pourcentage
# Si c'est de 0, l'attaque n'est pas affecté par cette règle, donc seul la portée détermine si elle va toucher ou non
# Si la valeur est de 100, le coup touche dans tout les cas
#
# - Description : str
# Description du coup
#
# - setDMG : int
# Si NULL : l'attaque fera le même nombre de dégâts que les statistiques du perso. Si c'est un projectile, il fera le nombre de dégâts que la statistique altDMG
# Si non NULL : l'attaque fera le nombre de dégâts indiqué
#
# - armor : int
# Nombre de tour selon laquelle le personnage sera invincible. Commence dès le tour où l'attaque est employé.
# Donc si une attaque a un tour d'armor, pendant le tour où le joueur va sélectionner l'attaque il sera invincible.