# Ce fichier contiendra toutes les fonctions pour communiquer avec la base de donnée
import sqlite3
import datetime

import os
# Obtenir le chemin absolu du répertoire contenant database.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Construire le chemin relatif vers le fichier de base de données
db_path = os.path.join(current_dir, '..', 'Database', 'Veronica.db')
# Établir une connexion à la base de données
con = sqlite3.connect(db_path)
"""
Ici, os.path.abspath(__file__) renvoie le chemin absolu complet du fichier database.py.
os.path.dirname extrait le chemin absolu du répertoire contenant database.py, qui est Veronica/Database dans ce cas.
os.path.join est utilisé pour construire un chemin relatif en utilisant les deux points (..) pour remonter d'un répertoire et atteindre le fichier de base de données.
"""

# --- Fonctions basiques de communication avec la base de donnée ---
def createUser(id:int)->int:
    """Créer le profile d'un utilisateur"""
    if not UserExist(id):
        cur = con.cursor()
        today = datetime.datetime.now()
        insertdata = """INSERT INTO user VALUES (?,0,NULL,?,0,10,0,0);"""
        cur.execute(insertdata,(id,today))
        con.commit()

def UserExist(id:int)->bool:
    """Vérifie si l'utilisateur existe dans la base de donnée"""
    cur = con.cursor()
    Recup = 'SELECT COUNT(*) FROM user WHERE ID_Discord={}'.format(id)
    cur.execute(Recup)
    Verif = cur.fetchone()[0]
    if not Verif:
        return False
    return True

def DayBetween(time1,time2)->int:
    """Retourne le nombre de jours entre 2 dates"""
    temp=time1-time2
    return temp.days

def getCreationDate(id):
    """Retourne la date de création du profile"""
    cur = con.cursor()
    cur.execute("SELECT creation_date FROM user WHERE ID_Discord={}".format(id))
    result=cur.fetchall()
    return result[-1][0]

# --- Fonctions communiquant les rôles à propos des niveaux d'un utilisateur ---
# Méthodes get (roles lvl)
def getListeRoles():
    """Récupère une liste sous forme de liste de tuples, contenant le niveau et le nom du rôle lié au niveau de l'utilisateur"""
    cur = con.cursor()
    cur.execute("SELECT Niveau, Role FROM Levels WHERE Role IS NOT NULL")
    result=cur.fetchall()
    return result
def getSpecXPRole(lvl:int):
    """Retourne le nom d'un rôle spécifique et le niveau requis (en tuple) en fonction d'un rôle entré. Arrondi en dessous"""
    liste=getListeRoles()
    if liste[-1][0]>lvl:
        for i in range(len(liste)):
            if liste[i][0]==lvl or (liste[i][0]<lvl and liste[i+1][0]>lvl):
                return liste[i]
    else:
        return liste[-1]


# --- Fonctions communiquant avec l'expérience et les niveaux d'un utilisateur ---
# Méthodes get (xp)

def getUserLvl(id:int)->int:
    """Sélectionne le niveau du joueur. Je récupère la liste des niveaux dont l'xp requis est en dessous de ce qu'il a, et le dernier de la liste défini son niveau"""
    if UserExist(id):
        cur = con.cursor()
        cur.execute("SELECT Level FROM user WHERE id_discord={}".format(id))
        result=cur.fetchall()
        return result[-1][0]

def getRequireXPLvl(lvl:int)->int:
    """Retourne l'xp requis depuis un niveau entré en paramètre, pour passer au prochain niveau"""
    cur = con.cursor()
    cur.execute("SELECT Xp_requise FROM Levels WHERE Niveau={}".format(lvl))
    result=cur.fetchall()
    return result[0][0]

def getUserXPPourcentage(id)->float:
    """Donne l'avancement du niveau de l'utilisateur à propos de son xp, sous forme de pourcentage"""
    if UserExist(id):
        curXP=getUserXP(id)
        return (curXP / getRequireXPLvl(getUserLvl(id)))*100

def getUserXP(id)->int:
    """Retourne l'expérience actuelle de l'utilisateur entré en paramètre"""
    if UserExist(id):
        cur = con.cursor()
        cur.execute("SELECT xp FROM user WHERE id_discord = {}".format(id))
        curXP=cur.fetchall()
        return curXP[0][0]
# Méthodes set (xp)
def setUserXp(id,amont:int=None,x:int=0):
    """Définie l'xp de l'utilisateur. Amont correspond à l'xp à définir, par défaut à None. x correspond à de l'xp à additionner. Le cas du lvl up est pris en compte et retourne -1"""
    if UserExist(id):
        if amont==None:
            amont=getUserXP(id)
        if amont+x >= getRequireXPLvl(getUserLvl(id)):
            setUserLvl(id,None,1)
            cur=con.cursor()
            cur.execute("UPDATE user SET xp=0 WHERE id_discord={}".format(id))
            con.commit()
            return -1
        else:
            cur = con.cursor()
            cur.execute("UPDATE user SET xp = {} WHERE id_discord={}".format(amont+x,id))
            con.commit()
            return getUserXP(id)

def setUserLvl(id,amont:int=None,x:int=0):
    """Défini le niveau d'un utilisateur. x est pour additionner mais pas obligatoire"""
    if UserExist(id):
        if amont==None:
            amont=getUserLvl(id)
        cur=con.cursor()
        cur.execute("UPDATE user SET Level = {} WHERE id_discord={}".format(amont+x,id))
        con.commit()
        return getUserLvl(id)

# --- Fonctions communiquant avec la quantité de monnaie d'un utilisateur ---
#Méthodes get (monnaie)
def getUserMoney(id:int)->int:
    """Retourne la quantité d'argent de l'utilisateur"""
    if UserExist(id):
        cur = con.cursor()
        cur.execute("SELECT money FROM user WHERE id_discord={}".format(id))
        result=cur.fetchone()[0]
        return result

def getUserJeton(id:int)->int:
    """Retourne la quantité de jeton qu'un utilisateur a en stock"""
    if UserExist(id):
        cur = con.cursor()
        cur.execute("SELECT stock_jeton FROM user WHERE id_discord={}".format(id))
        result=cur.fetchone()[0]
        return result

def getDailyCooldown(id)->datetime:
    """Permet d'obtenir la date du cooldown pour la commande du daily"""
    cur = con.cursor()
    cur.execute("SELECT daily_cooldown FROM user WHERE id_discord={}".format(id))
    temp=cur.fetchall()[0][0]
    temp=datetime.datetime.strptime(temp,"%y-%m-%d %H:%M:%S")
    return temp

def DailyCooldownNone(id)->bool:
    """Vérifie si le cooldown du Daily est nul ou non"""
    if UserExist(id):
        cur = con.cursor()
        cur.execute("SELECT daily_cooldown FROM user WHERE id_discord={}".format(id))
        temp=cur.fetchall()[0][0]
        if temp==None:
            return True
        else:
            return False
    else:
        return False
#Méthodes set (monnaie)
def setUserMoney(id,amont:int=None,x:int=0)->int:
    """Définie l'argent de l'utilisateur. Amont correspond à l'argent à définir, par défaut à None. x correspond à de l'argent à additionner"""
    if UserExist(id):
        if amont==None:
            amont = getUserMoney(id)
        cur = con.cursor()
        cur.execute("UPDATE user SET money = {} WHERE id_discord={}".format(amont+x,id))
        con.commit()
    return getUserMoney(id)

def setUserJeton(id,amont:int=None,x:int=0)->int:
    """Définie la quantité de jetons de l'utilisateur. Amont correpond à l'argent à définir, par défaut à None. x correspond à de l'argent à additionner.
    Retourne -1 si l'utilisateur n'a pas assez d'argent pour en acheter. Retourne la quantité qu'avait l'utilisateur avant l'achat si la limite de jetons disponible est atteinte."""
    if UserExist(id):
        if amont == None:
            amont=getUserJeton(id)
        if getJetonCirculation()>amont+x or getJetonCirculation()>1:
            cur = con.cursor()
            cur.execute("UPDATE user SET stock_jeton={} WHERE id_discord={}".format(amont+x,id))
            con.commit()
            setJetonStock(None,-x)
    return getUserJeton(id)

def setJetonStock(amont:int=None,x:int=0):
    """Définie au niveau de la banque le nombre de Jetons qui sont en circulation"""
    if amont==None:
        amont=getJetonCirculation()
    jeton=amont+x
    stock=getBankStocks()
    cur=con.cursor()
    today = datetime.datetime.now()
    today=today.strftime("%y-%m-%d %H:%M:%S")
    inserdate="""INSERT INTO bank VALUES (?,?,?,?)"""
    cur.execute(inserdate,(stock,jeton,round(stock/jeton),today))
    con.commit()
    return getJetonCirculation()
def dailyMoney(id)->int:
    """Fonction gérant le daily pour un utilisateur"""
    if UserExist(id):
        today = datetime.datetime.now()
        if DailyCooldownNone(id) or DayBetween(today,getDailyCooldown(id)) >= 1:
            cur = con.cursor()
            today=today.strftime("%y-%m-%d %H:%M:%S")
            cur.execute("UPDATE user SET daily_cooldown='{}' WHERE id_discord={};".format(today,id))
            con.commit()
            setUserMoney(id,None,150)
            setBankStocks(-150)
    return getUserMoney(id)

# --- RESUETE ECONOMIE ---
def getBankStocks()->int:
    cur=con.cursor()
    cur.execute("SELECT bank_stocks FROM bank")
    result=cur.fetchall()[-1][0]
    return result
def setBankStocks(amont:int)->int:
    """Quantité en plus à ajouter"""
    stock=getBankStocks()+amont
    cur=con.cursor()
    today = datetime.datetime.now()
    today=today.strftime("%y-%m-%d %H:%M:%S")
    jeton=getJetonCirculation()
    inserdate="""INSERT INTO bank VALUES (?,?,?,?)"""
    cur.execute(inserdate,(stock,jeton,round(stock/jeton),today))
    con.commit()
    return getBankStocks()
def getJetonCirculation()->int:
    """Retourne le nombre de jetons en circulation"""
    cur=con.cursor()
    cur.execute("SELECT jetons_circulation FROM bank")
    result=cur.fetchall()[-1][0]
    return result
def getCoursJeton()->int:
    cur=con.cursor()
    cur.execute("SELECT cours_conchiglie FROM bank")
    result=cur.fetchall()[-1][0]
    if result==None:
        UpdateCoursJeton()
    return result
def UpdateCoursJeton():
    jeton=getJetonCirculation()
    stock=getBankStocks()
    cur=con.cursor()
    today = datetime.datetime.now()
    today=today.strftime("%y-%m-%d %H:%M:%S")
    inserdate="""INSERT INTO bank VALUES (?,?,?,?)"""
    cur.execute(inserdate,(stock,jeton,round(stock/jeton),today))
    con.commit()
    return getCoursJeton()
def getListeEltBank():
    """Retourne le nombre de ligne présent dans la table pour la base de donnée dédié à la banque"""
    cur=con.cursor()
    cur.execute("SELECT * FROM bank")
    result=cur.fetchall()
    return result
def ShowStockGraph():
    import matplotlib.pyplot as plt
    x=[] #Absice du temps
    y=[] #Ordonnée de coquillettes
    liste=getListeEltBank()
    for i in range(len(liste)):
        if not (None in liste[i]):
            x.append(liste[i][3])
            y.append(liste[i][0])
    plt.plot(x,y)
    plt.xlabel('Temps')
    plt.ylabel('Coquillettes de la Banque Centrale')
    plt.title("Stock de coquillettes en fonction du temps")

    # Chemin relatif de la sortie souhaitée
    output_path = '../economy/MoneyStockGraph.png'
    # Obtenir le chemin absolu du répertoire courant
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Combiner les chemins pour obtenir le chemin absolu de la sortie souhaitée
    output_full_path = os.path.join(current_dir, output_path)
    # Créer le graphique et enregistrer la sortie au chemin absolu
    plt.savefig(output_full_path)
def ShowJetonGraph():
    import matplotlib.pyplot as plt
    x=[] #Absice du temps
    y=[] #Ordonnée des conchiglie
    liste=getListeEltBank()
    for i in range(len(liste)):
        if not (None in liste[i]):
            x.append(liste[i][3])
            y.append(liste[i][2])
    plt.plot(x,y)
    plt.xlabel('Temps')
    plt.ylabel('Valeur du Conchiglie')
    plt.title("Valeur du Conchiglie en fonction du temps")

    # Chemin relatif de la sortie souhaitée
    output_path = '../economy/graph_jeton.png'
    # Obtenir le chemin absolu du répertoire courant
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Combiner les chemins pour obtenir le chemin absolu de la sortie souhaitée
    output_full_path = os.path.join(current_dir, output_path)
    # Créer le graphique et enregistrer la sortie au chemin absolu
    plt.savefig(output_full_path)

# --- Autres fonctions de communication avec la table user ---
def getUserLootbox(id:int)->int:
    """Retourne la quantité de lootbox qu'a un utilisateur en stock"""
    if UserExist(id):
        cur = con.cursor()
        cur.execute("SELECT stock_lootbox FROM user WHERE id_discord={}".format(id))
        result=cur.fetchone()[0]
        return result
def setUserLootbox(id,amont:int=None,x:int=0)->int:
    """Définie le nombre de lootbox qu'a un utilisateur. Amont correspond à un nombre de lootboxs à définir à définir, par défaut à None. x correspond au nombre de lootbox à additionner"""
    if UserExist(id):
        if amont==None:
            amont = getUserLootbox(id)
        cur = con.cursor()
        cur.execute("UPDATE user SET stock_lootbox = {} WHERE id_discord={}".format(amont+x,id))
        con.commit()
    return getUserLootbox(id)
"""
createUser(323147727779397632)
print(getUserMoney(323147727779397632))
print(getUserLvl(323147727779397632))
print(setUserMoney(323147727779397632,1000))
print(setUserMoney(323147727779397632,None,10))
print(dailyMoney(323147727779397632))
print("Xp requis pour lvl up : {}".format(getRequireXPLvl(getUserLvl(323147727779397632)+1)))
print(getUserXPPourcentage(323147727779397632))
print(setUserXp(323147727779397632,50))
print(setUserLvl(323147727779397632,10))
print(getRequireXPLvl(getUserLvl(323147727779397632)))
print(setUserXp(323147727779397632,1255))
print(setUserXp(323147727779397632,None,10))
print(getSpecXPRole(67))

print(getBankStocks())
print(setBankStocks(-150))
print(getJetonCirculation())
print(getCoursJeton())
print(UpdateCoursJeton())
print(getListeEltBank())

from random import randint
temp=0
for i in range(10000):
    #import time
    #time.sleep(0.5)
    temp=randint(-10000,10000)
    while temp==0:
        temp=randint(-10000,10000)
    print(setBankStocks(temp))
print(ShowJetonGraph())
"""

# --- FONCTIONS A PROPOS DU JEU SMASH ---
def getCharacterStat(num:int)->tuple:
    """Retourne les stats d'un personnage entré sous forme de tuple"""
    cur = con.cursor()
    cur.execute("SELECT * FROM smash WHERE num={};".format(num))
    result=cur.fetchall()[0]
    return result
def getListCharacter()->list:
    """Retourne la liste des numéros des personnages qui sont présent dans la base de donnée"""
    cur = con.cursor()
    cur.execute("SELECT num FROM smash;")
    temp=cur.fetchall()
    result=[]
    for elt in temp:
        result.append(elt[0])
    return result
def getListNameCharacter()->list:
    """Retourne la liste des noms des personnages qui sont présent dans la base de donnée"""
    cur = con.cursor()
    cur.execute("SELECT nom FROM smash;")
    temp=cur.fetchall()
    result=[]
    for elt in temp:
        result.append(elt[0])
    return result
def NameToIndexCharacter(name:str)->int:
    """Retourne l'index du personnage qui correspond au nom entré"""
    cur = con.cursor()
    cur.execute("SELECT num FROM smash WHERE nom='{}';".format(name))
    temp=cur.fetchall()[0]
    return temp[0]
def getListMovesCharacter(id:int)->list:
    """Retourne une liste des IDs des moves qu'un personnage d'id entré, peux utiliser"""
    cur = con.cursor()
    cur.execute("SELECT attackID FROM smashAttacksLink WHERE smasher={};".format(id))
    temp=cur.fetchall()
    result=[]
    for elt in temp:
        result.append(elt[0])
    return result
def getAttackFromID(id:int)->tuple:
    """Retourne les stats d'un personnage entré sous forme de tuple"""
    cur = con.cursor()
    cur.execute("SELECT * FROM smash_attacks WHERE num={};".format(id))
    result=cur.fetchall()[0]
    return result