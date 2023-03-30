#Importation des fonctions pour communiquer avec la base de donnée
from Database import database

#Concept de Smasher (personnage du jeu de Véronica)
class Smasher:
    """Classe représentation un personnage du jeu. Ses stats sont importées de la base de donnée"""
    def __init__(self,number):
        stats=database.getCharacterStat(number)
        self.number=stats[0]
        self.name=stats[1]
        self.PV=stats[2]
        self.attack=stats[3]
        self.defense=stats[4]
        self.speed=stats[5]
        self.dexterity=stats[6]
        self.reach=stats[7]
        self.altDMG=stats[8]
        self.description=stats[9]
    # --- Définition des méthodes get :
    def getStats(self):
        """Retourne les statistiques du personnage sous forme de dictionnaire"""
        return self.__dict__
    def getName(self):
        """Retourne le nom du personnage"""
        return self.getStats()['name']
    def getNumber(self):
        """Retourne le nombre du personnage"""
        return self.getStats()['number']
    def getPV(self):
        """Retourne les PV actuel du personnage"""
        return self.getStats()['PV']
    def getAttack(self):
        """Retourne l'attaque du personnage"""
        return self.getStats()['attack']
    def getDefense(self):
        """Retourne la défense du personnage"""
        return self.getStats()['defense']
    def getSpeed(self):
        """Retourne la vitesse du personnage"""
        return self.getStats()['speed']
    def getDexterity(self):
        """Retourne la dextérité du personnage"""
        return self.getStats()['dexterity']
    def getReach(self):
        """Retourne la portée du personnage"""
        return self.getStats()['reach']
    def getAltDMG(self):
        """Retourne la valeure de la statistique des dégâts alternatifs (projo/combo) du personnage"""
        return self.getStats()['altDMG']
    def getDescription(self):
        """Retourne la description du personnage"""
        return self.getStats()['description']