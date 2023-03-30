import discord
from discord.ext import commands
from discord import app_commands

#Importation des fonctions pour communiquer avec la base de donnée
from Database import database
#Importation du concept de personnages
from Smash import smasher
#Importation du concept des attaques
from Smash import attacks

class Smash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name="smasher_info",description="Retourne les informations relatives par rapport à un personnage",num="Index du personnage à rechercher")
    async def smasher_info(self,ctx,num):
        """Retourne les informations relatives par rapport à un personnage"""
        SQLcheck=["SELECT","Select","select","FROM","From","from"]
        for elt in SQLcheck:
            if elt in num:#Cas d'une tentative d'injection SQL
                await ctx.send("T'es un petit malin toi <:you:794903293045899274>")
            else:
                if num in database.getListNameCharacter(): #Dans le cas où l'utilisateur entre le nom du personnage
                    num=database.NameToIndexCharacter(num) #Convertion en index
                num=int(num)
                if num in database.getListCharacter():
                    perso=smasher.Smasher(num)
                    embedVar = discord.Embed(color=discord.Color.brand_red()) #En rouge pour différencier des autres modules du bot
                    embedVar.set_footer(text="Véronica Alpha 1.3 - Game version : {}".format(version))
                    embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
                    #Valeurs de l'embed :
                    embedVar.add_field(name="Nom :",value="{} ({})".format(perso.getName(),properNumber(perso.getNumber())),inline=False)
                    embedVar.add_field(name="Description :",value="{}".format(perso.getDescription()),inline=False)
                    embedVar.add_field(name="--- Statistiques du personnage ---",value="",inline=False)
                    embedVar.add_field(name="PV :",value="{}".format(perso.getPV()),inline=True)
                    embedVar.add_field(name="Attaque :",value="{}".format(perso.getAttack()),inline=True)
                    embedVar.add_field(name="Défense :",value="{}".format(perso.getDefense()),inline=True)
                    embedVar.add_field(name="Vitesse :",value="{}".format(perso.getSpeed()),inline=True)
                    embedVar.add_field(name="Dextérité :",value="{}".format(perso.getDexterity()),inline=True)
                    embedVar.add_field(name="Portée :",value="{}".format(perso.getReach()),inline=True)
                    embedVar.add_field(name="Dégâts en combo ou d'un projectile :",value="{}".format(perso.getAltDMG()),inline=True)
                    embedVar.add_field(name="--- Liste des attaques du personnage ---",value="",inline=False)
                    #Implémentation des attaques du personnages :
                    listeNumMoves=database.getListMovesCharacter(perso.getNumber())
                    listeMoves=[] #On va stocker sous forme d'objet les attaques, à partir de leur IDs
                    temp=[] #Liste temporaire où sera stocké les objets attaques de type passif
                    for i in range(len(listeNumMoves)):
                        moves=attacks.Move(listeNumMoves[i])
                        if moves.getType()==3: #Si c'est un passif
                            temp.append(moves) #On l'ajoute dans la liste temporaire, dédié aux passifs
                        else: #Sinon :
                            listeMoves.append(moves) #On ajoute dans la liste normale
                    for i in range(len(listeMoves)): #Pour chaque moves, on va mettre son affichage
                        embedVar.add_field(name="({}) - {}".format(i+1,listeMoves[i].getName()),value="{}".format(listeMoves[i].getDescription()),inline=True)
                    if temp: #Si la liste des passifs n'est pas vide
                        for move in temp: #On ajoute chaque passif dans l'affichage
                            embedVar.add_field(name="Passif : {}".format(move.getName()),value="{}".format(move.getDescription()),inline=False)
                    #Ajout visuel :
                    file = []
                    file.append(discord.File("E:\\Documents\\Véronica\\Veronica\\Smash\\Media\\Stock Icons\\{}.png".format(perso.getName()),filename='icon.png'))
                    embedVar.set_thumbnail(url="attachment://icon.png")
                    if properNumber(perso.getNumber())==100: #Si c'est Akuma
                        file.append(discord.File("E:\\Documents\\Véronica\\Veronica\\Smash\\Media\\Akuma\\AkumaShunGokuTatsu.gif",filename='Akuma.gif'))
                        embedVar.set_image(url="attachment://Akuma.gif")
                    await ctx.send(files=file,embed=embedVar)
                    break
                else:
                    await ctx.send("Le personnage que vous avez entré n'existe pas. Veuillez réessayer.")
                    break

async def setup(bot):
    await bot.add_cog(Smash(bot))

#Enregistrement dans une variable de la version actuelle du jeu
version = "0.1"

def properNumber(num):
    """Convertie le code identifiant le personnage en quelque chose de plus lisible. E indiquant un echo fighter.
    Plus d'informations sur la signification du code en lui même dans game.md"""
    num=str(num)
    if len(num)==5:
        result=int(num[1:4])
        if num[4]=="1":
            result=str(result)+"ᵋ"
            return result
        else:
            return result
    return num