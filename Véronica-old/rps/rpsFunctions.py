#Ce fichier est fait pour alléger le fichier rps.py
#Toutes les fonctions Python (et non Discord.py) dédiés au bon fonctionnement du module sont stockées ici
def RPSintTOstr(input:int):
    """Transforme un nombre entré en ce qu'il est censé représenter. Si non inclus dans la liste, il retourne simplement ce nombre"""
    if input == 1:
        return "🪨Pierre"
    elif input==2:
        return "🧻Papier"
    elif input==3:
        return "️️️✂️Ciseaux"
    else:
        return input
    
def RPSwinner(p1:int,p2:int):
    """Calcul le gagnant avec p1 représentant celui qui a demandé le 1v1, et p2 celui qui représente l'autre joueur.
    Retourne 1 si le joueur 1 a gagné
            2 si le joueur 2 a gagné
            3 si c'est une égalité
    """
    RPSliste=[1,2,3]
    if p1==p2:
        return 3
    elif RPSliste[(p1-1)-1]==p2: #Si la sélection du joueur 2 correspond à la une option de défaite face au joueur 1
        #soit celle qui précède la sélection du joueur 1 dans la liste
        return 1
    else: #Normalement la seule option restante est si le joueur 2 gagne
        return 2

def currenttime():
    """Retourne le temps actuelle en chaîne de caractères sous cette forme : "DD/MM/YYYY-HH:mm" """
    from datetime import datetime
    temp=datetime.now()
    return str(temp.day)+"/"+str(temp.month)+"/"+str(temp.year)+"-"+str(temp.hour)+":"+str(temp.minute)