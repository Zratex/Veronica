import sqlite3
import datetime
from sqlite3.dbapi2 import register_converter
import time
from random import randint


con = sqlite3.connect(f'D:\\Documents\\Véronica\\Veronica.db')
cur = con.cursor()


def getmoney(id,money):
    cur = con.cursor()
    print(id)
    print(money)

def creataccount(id):
    cur = con.cursor()
    Recup = 'SELECT COUNT(*) FROM user WHERE ID_Discord={}'.format(id)
    cur.execute(Recup)
    Verif = cur.fetchone()[0]
    print(Verif)
    if Verif == 0: 
        today = datetime.datetime.now()
        today=today.strftime("%d/%m/%Y, %H:%M:%S")
        insertdata = """INSERT INTO user VALUES (?,1,0,0,0,NULL,?);"""
        cur.execute(insertdata,(id,today))
        con.commit()
        return(1)
    else :
        return(2)

def info(id):
    cur = con.cursor()
    Recup = 'SELECT * FROM User WHERE ID_Discord={}'.format(id)
    cur.execute(Recup)
    Verif = []
    for x in cur.fetchall():
        for item in x:
            Verif.append(item)
    print(Verif)
    return(Verif)

def testUser(id):
    cur = con.cursor()
    Recup = 'SELECT COUNT(*) FROM user WHERE ID_Discord={}'.format(id)
    cur.execute(Recup)
    Verif = cur.fetchone()[0]
    if Verif == 0 : 
        print("le compte n'existe pas")
        return(1)
    else :
        return(2)

def deletecompte(id):
    cur = con.cursor()
    sql_select_query = """update User set Creation = 01/01/2021 where ID_Discord = ?"""
    cur.execute(sql_select_query, (id))
    con.commit()
    id2=id*2
    sql_select_query = """update User set ID_Discord = ? where ID_Discord = ?"""
    cur.execute(sql_select_query, (id2,id))
    con.commit()
    print("L'utilisateur est DELETE")

def daily(id):
    cur = con.cursor()
    Verif =  testdaily(id)
    if Verif == 1 :
        Recup = 'SELECT Money FROM User WHERE ID_Discord={}'.format(id)
        cur.execute(Recup)
        RecupMoney = cur.fetchone()[0]
        Money = RecupMoney+150
        sql_select_query = """update User set Money = ? where ID_Discord = ?"""
        cur.execute(sql_select_query, (Money, id))
        con.commit()
        return(Money)
    elif Verif == 0:
        return(0)

def testdaily(id):
    Recup = "SELECT Daily FROM User WHERE ID_Discord={}".format(id)
    cur.execute(Recup)
    RecupTime = cur.fetchone()[0]
    today = datetime.datetime.now()
    today=int(time.mktime(today.timetuple()))
    if RecupTime is None:
        sql_select_query = """update User set Daily = ? where ID_Discord = ?"""
        cur.execute(sql_select_query, (today, id))
        con.commit()
        return(1)
    if today-RecupTime <= 86400:
        return(0)
    else:
        sql_select_query = """update User set Daily = ? where ID_Discord = ?"""
        cur.execute(sql_select_query, (today, id))
        con.commit()
        return(1)

def exp(id):
    Recup = "SELECT Exp FROM User WHERE ID_Discord={}".format(id)
    cur.execute(Recup)
    expérience=cur.fetchone()[0]
    xp=randint(5,15)
    xp=xp+expérience
    sql_select_query = """update User set Exp = ? where ID_Discord = ?"""
    cur.execute(sql_select_query, (xp, id))
    con.commit()
    #permet de récupérer le niveau actuel de la personne
    Recup = "SELECT Level FROM User WHERE ID_Discord={}".format(id)
    cur.execute(Recup)
    lvl = cur.fetchone()[0]
    #permet de récupérer la valeur de l'xp requise pour lvl up
    Recup = "SELECT Xp_requise FROM Levels WHERE Niveau={}".format(lvl)
    cur.execute(Recup)
    require = cur.fetchone()[0]
    if xp >= require: #vérifie si l'xp dépasse la valeur nécessaire pour un rank up
        #reset d'xp pour le rank up
        sql_select_query = """update User set Exp = ? where ID_Discord = ?"""
        xp=0
        cur.execute(sql_select_query, (xp, id))
        con.commit()
        #fait augmenter le niveau
        sql_select_query = """update User set level = ? where ID_Discord = ?"""
        lvl=lvl+1
        result=[1,lvl] #1 pour signifier que c'est un rank up, et le lvl est là pour pouvoir retirer l'information du nouveau niveau
        cur.execute(sql_select_query, (lvl, id))
        con.commit()
        return(result) 
    else:
        result=[2,0]
        return(result) #2 pour signifier que ce n'est pas un rank up

def depense(id,cout):
    Recup = "SELECT Money FROM user WHERE ID_Discord={}".format(id)
    cur.execute(Recup)
    RecupMoney = cur.fetchone()[0]
    if RecupMoney-cout < 0:
        return(0) #Pour dire que l'achat n'est pas disponible : l'utilisateur n'a pas assez de thunes
    else:
        sql_select_query = """update User set Money = ? where ID_Discord = ?"""
        RecupMoney=RecupMoney-cout
        cur.execute(sql_select_query, (RecupMoney, id))
        con.commit()
        return(1) #Pour dire que l'achat est disponible, et que la différence a été effectué sur le compte
