import sqlite3
import datetime
from sqlite3.dbapi2 import register_converter
import time


con = sqlite3.connect(f'E:\\Véronica\\Veronica.db')
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
    if Verif == 0 : 
        today = datetime.datetime.now()
        today=today.strftime("%d/%m/%Y, %H:%M:%S")
        insertdata = """INSERT INTO user VALUES (?,0,0,0,0,NULL,?);"""
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
    Recup = 'SELECT COUNT(*) FROM User WHERE ID_Discord={}'.format(id)
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