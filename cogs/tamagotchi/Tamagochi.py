from random import randint

class Tamagotchi:
    lifeTime=10
    def __init__(self,name : str):
        self.age=0
        self.maxEnergy=randint(5,9)
        self.energy=randint(3,7) #stat bouffe
        self.maxiFun=randint(5,9)
        self.fun=randint(3,7) #stat bonheur
        self.name=name
    def parle(self):
        """Indique comment va le Tamagotchi"""
        if self.energy > 4 and self.fun > 4:
            print(f"{self.name} : I'm bing chilling")
        else:
            if self.energy <= 4:
                print(f"{self.name} : j'ai faim")
            if self.fun <= 4:
                print(f"{self.name} : je m'ennuie")
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
    def __str__(self):
        """Retourne les informations du Tamagotchi courant"""
        return "Name : "+self.name+";Age : "+str(self.age)+"; maxEnergy : "+str(self.maxEnergy)+"; Energy : "+str(self.energy)+"; maxiFun : "+str(self.maxiFun)+"; Fun : "+str(self.fun)