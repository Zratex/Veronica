from logging import info
import sqlite3
import datetime
from sqlite3.dbapi2 import register_converter
import time
from random import randint

con = sqlite3.connect(f'D:\\Documents\\Véronica\\Veronica.db')
cur = con.cursor()

def testuser(id):
    cur = con.cursor()
    Recup = 'SELECT COUNT(*) FROM cpu_user WHERE ID_DISCORD={}'.format(id)
    cur.execute(Recup)
    Verif = cur.fetchone()[0]
    if Verif == 0:
        print("{} n'a pas de rig".format(id))
        return 0
    else:
        return 1

#--- DEFINITIONS CPU --
def getcpu(id,tier):
    cur = con.cursor()
    try:
        insertdata = """INSERT INTO cpu_user VALUES (?,?,0);"""
        cur.execute(insertdata,(id,tier))
        con.commit()
        return 1
    except:
        return 0

def usercpu(id,plugged): #plugged est pour déterminer si il faut trier parce ce qui est branché ou non, donc =0 ou =1
    if plugged:
        cur = con.cursor()
        Recup = 'SELECT CPU FROM cpu_user WHERE ID_DISCORD={} ORDER BY PLUGGED DESC'.format(id) #Desc pour l'ordre décroissant
        cur.execute(Recup)
        info=cur.fetchone()[0]
        if info ==1:
            return ["Altaïr v1",1]
        elif info==2:
            return ["Ryzen 5 3600",2]
        elif info==3:
            return ["i9-10900K",3]
        elif info==4:
            return ["Ryzen 9 5950X",4]
        elif info==8:
            return ["Threadripper",8]
    else:
        cur = con.cursor()
        Recup="SELECT CPU FROM cpu_user WHERE ID_DISCORD={}".format(id)
        cur.execute(Recup)
        info=cur.fetchall() #Retourne la liste entière des CPUs
        result=[]
        for elt in info:
            if int(elt[0]) ==1:
                result.append(["Altaïr v1",1])
            elif int(elt[0]) ==2:
                result.append(["Ryzen 5 3600",2])
            elif int(elt[0]) ==3:
                result.append(["i9-10900K",3])
            elif int(elt[0]) ==4:
                result.append(["Ryzen 9 5950X",4])
            elif int(elt[0]) ==8:
                result.append(["Threadripper",8])
        return result

def cpupower(tier):
    cur=con.cursor()
    Recup="SELECT CONSOMMATION FROM cpu_mining WHERE CPU_TIER={}".format(tier)
    cur.execute(Recup)
    info=cur.fetchone()[0]
    return info

#--- DEFINITIONS ALIMENTATION ---
def newalim(id,power): #Modifie l'alimentation de l'utilisateur
    cur=con.cursor()
    try:
        if alim(id):
            select_query="""UPDATE alim_user SET power=? WHERE id_discord=?"""
            cur.execute(select_query,(power,id))
            con.commit()
            return 1
        else:
            insertdata = """INSERT INTO alim_user VALUES (?,?);"""
            cur.execute(insertdata(id,power))
            con.commit()
            return 1
    except:
        return 0

def useralim(id):
    cur = con.cursor()
    Recup = "SELECT power FROM alim_user WHERE ID_DISCORD={}".format(id)
    cur.execute(Recup)
    info=cur.fetchone()[0]
    return info

def alim(id): #Vérifie que l'utilisateur a une alim
    cur = con.cursor()
    Recup = 'SELECT COUNT(*) FROM alim_user WHERE ID_DISCORD={}'.format(id)
    cur.execute(Recup)
    Verif = cur.fetchone()[0]
    if Verif == 0:
        print("{} n'a pas d'alim'".format(id))
        return 0
    else:
        return 1

#--- DEFINITIONS GPU ---
def usergpu(id,plugged): #plugged est pour déterminer si il faut trier parce ce qui est branché ou non, donc =0 ou =1
    if plugged:
        cur = con.cursor()
        Recup = 'SELECT gpu FROM gpu_user WHERE ID_DISCORD={} ORDER BY PLUGGED DESC'.format(id) #Desc pour l'ordre décroissant
        cur.execute(Recup)
        info=cur.fetchall()
        return list(info)
    else:
        cur = con.cursor()
        Recup="SELECT CPU FROM cpu_user WHERE ID_DISCORD={}".format(id)
        cur.execute(Recup)
        info=cur.fetchall() #Retourne la liste entière des CPUs
        return list(info)

def rentgpu(name):
    cur = con.cursor()
    Recup = "SELECT rent FROM gpu WHERE NAME='{}'".format(name)
    cur.execute(Recup)
    info=cur.fetchone()[0]
    return info

def gpupower(name):
    cur=con.cursor()
    Recup="SELECT CONSOMMATION FROM gpu WHERE NAME='{}'".format(name)
    print(Recup)
    cur.execute(Recup)
    info=cur.fetchone()[0]
    return info