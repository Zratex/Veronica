from random import randint

class Tamagotchi:
    lifeTime=10
    def __init__(self, id:int=0,user_id:int=0,name : str="nom",age: int=0, max_energy: int=randint(5,9), current_energy: int=randint(3,7), max_fun: int=randint(5,9), current_fun: int=randint(3,7)):
        self.id=id
        self.userid=user_id
        self.age=age
        self.maxEnergy=max_energy
        self.current_energy=current_energy #stat bouffe
        self.maxiFun=max_fun
        self.currentFun=current_fun #stat bonheur
        self.name=name
    def parle(self) -> int:
        """Indique comment va le Tamagotchi
        0 : il chill
        1 : il a faim
        2 : il s'ennuie
        """
        if self.current_energy > 4 and self.currentFun > 4:
            return 0
        else:
            if self.current_energy <= 4:
                return 1
            if self.currentFun <= 4:
                return 2
    def mange(self) -> bool:
        """Retourne vrai si il a mangé, faux si il n'a pas faim"""
        if self.current_energy<self.maxEnergy:
            self.current_energy+=randint(1,3)
            print("Cheers")
            return True
        else:
            print("Je n'ai pas faim !")
            return False
    def joue(self) -> bool:
        """Retourne vrai si il a joué, faux si il n'a pas envie de jouer"""
        if self.currentFun<self.maxiFun:
            self.currentFun+=randint(1,3)
            return True
        else:
            return False
    def consommeEnergie(self) -> bool:
        """Retourne faux si le passage de tour tue, vrai si meurt suite au passage de tour"""
        self.current_energy-=randint(1,3)
        self.currentFun-=randint(1,3)
        return not (self.current_energy <= 0 or self.currentFun <= 0)
    def estMortVieillesse(self) -> bool:
        """Retourne vrai si il est mort de vieillesse"""
        return self.age >= Tamagotchi.lifeTime