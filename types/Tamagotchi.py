from random import randint

class Tamagotchi:
    lifeTime=10
    def __init__(self,name : str="nom",age: int=0, maxEnergy: int=randint(5,9), energy: int=randint(3,7), maxiFun: int=randint(5,9), fun: int=randint(3,7)):
        self.age=age
        self.maxEnergy=maxEnergy
        self.energy=energy #stat bouffe
        self.maxiFun=maxiFun
        self.fun=fun #stat bonheur
        self.name=name
    def parle(self) -> int:
        """Indique comment va le Tamagotchi
        0 : il chill
        1 : il a faim
        2 : il s'ennuie
        """
        if self.energy > 4 and self.fun > 4:
            return 0
        else:
            if self.energy <= 4:
                return 1
            if self.fun <= 4:
                return 2
    def mange(self) -> bool:
        """Retourne vrai si il a mangé, faux si il n'a pas faim"""
        if self.energy<self.maxEnergy:
            self.energy+=randint(1,3)
            print("Cheers")
            return True
        else:
            print("Je n'ai pas faim !")
            return False
    def joue(self) -> bool:
        """Retourne vrai si il a joué, faux si il n'a pas envie de jouer"""
        if self.fun<self.maxiFun:
            self.fun+=randint(1,3)
            print("Cheers")
            return True
        else:
            print("Je n'ai pas envie de jouer !")
            return False
    def consommeEnergie(self) -> bool:
        """Retourne faux si le passage de tour tue, vrai sinon"""
        self.energy-=randint(1,3)
        self.fun-=randint(1,3)
        if self.energy <= 0 or self.fun <= 0:
            print("Ah gars c'est ciao")
            return False
        else:
            return True
    def estMortVieillesse(self) -> bool:
        """Retourne vrai si mort de vieillesse"""
        return self.age >= Tamagotchi.lifeTime