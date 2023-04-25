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
                    image_generator(perso)
                    file.append(discord.File("Smash/Media/Stats.png",filename='Stats.png'))
                    embedVar.set_image(url="attachment://Stats.png")
                    await ctx.send(files=file,embed=embedVar)
                    break
                else:
                    await ctx.send("Le personnage que vous avez entré n'existe pas. Veuillez réessayer.")
                    break

async def setup(bot):
    await bot.add_cog(Smash(bot))

#Enregistrement dans une variable de la version actuelle du jeu
version = "0.2"

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

def image_generator(perso):
    """Ajoute l'icône du personnage sur un fond"""
    from PIL import Image, ImageDraw, ImageFont
    fond=Image.open("Smash\\Media\\killingmoonfontinfo.png")
    Stock=Image.open("Smash\\Media\\Stock Icons\\{}.png".format(perso.getName()))
    width1, height1 = fond.size
    Stock=Stock.resize((128,128))
    result=Image.new("RGBA",(width1,height1),(255,255,255,0))
    result.paste(fond,(0,0))

    if perso.getName() == "Akuma":
        temp=Image.open("Smash\\Media\\Akuma\\AkumaShunGokuTatsu.gif").convert("RGBA")
        temp=temp.resize((int(temp.size[0]*4.5),int(temp.size[1]*4.5)))
        result.alpha_composite(temp,(400,0))

    font = ImageFont.truetype("arial.ttf", size=55)
    draw = ImageDraw.Draw(result)
    temp=perso.getName()
    if temp[0].lower() in ["a","e","i","o","u"]:
        temp="d'"+temp
    else:
        temp="de "+temp
    text="Statistiques {}".format(temp)
    text_width, text_height = draw.textsize(text, font=font)
    draw.text((10,100),text,fill=(255,255,255),font=font)
    draw.line([10+text_width+5,100+text_height, 10, 100+text_height],fill=(255,255,255),width=2)

    result.paste(Stock,(width1-200,50),mask=Stock)

    font = ImageFont.truetype("arial.ttf", size=40)
    draw.text((5,200),"PV :",fill=(255,255,255),font=font)
    draw_stat((perso.getPV()/150)*100,result,(200,200))
    draw.text((675,200),"{}".format(perso.getPV()),fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw.text((5,300),"ATK :",fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw_stat(perso.getAttack(),result,(200,300))
    draw.text((675,300),"{}".format(perso.getAttack()),fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw.text((5,400),"DEF :",fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw_stat(perso.getDefense(),result,(200,400))
    draw.text((675,400),"{}".format(perso.getDefense()),fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw.text((5,500),"SPE :",fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw_stat(perso.getSpeed(),result,(200,500))
    draw.text((675,500),"{}".format(perso.getSpeed()),fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw.text((5,600),"DEX :",fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw_stat(perso.getDexterity(),result,(200,600))
    draw.text((675,600),"{}".format(perso.getDexterity()),fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw.text((5,700),"Reach :",fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw_stat(perso.getReach()*10,result,(200,700))
    draw.text((675,700),"{}".format(perso.getReach()),fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw.text((5,800),"Alt Dmg :",fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")
    draw_stat(perso.getAltDMG()*2,result,(200,800))
    draw.text((675,800),"{}".format(perso.getAltDMG()),fill=(255,255,255),font=font,stroke_width=2, stroke_fill="black")

    result.save("Smash/Media/Stats.png","PNG")


# Génération des barres de progression :
def drawProgressBar(d,x,y,w,h,progress,bg="gray"):
    #draw background
    d.ellipse((x+w,y,x+h+w,y+h),fill=bg)
    d.ellipse((x, y, x+h, y+h), fill=bg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h), fill=bg)

    # draw progress bar
    if progress<=30:
        fg=(255,0,0)
    elif progress<=49:
        fg=(242,159,11)
    elif progress<=65:
        fg=(150,255,150)
    elif progress<=80:
        fg=(0,255,0)
    elif progress<=99:
        fg=(0,0,255)
    else: #Donc au delà de 100
        fg=(255,255,255)
    w *= (progress/100)
    d.ellipse((x+w, y, x+h+w, y+h),fill=fg)
    d.ellipse((x, y, x+h, y+h),fill=fg)
    d.rectangle((x+(h/2), y, x+w+(h/2), y+h),fill=fg)

    return d

def draw_stat(pourcentage:float,out,co:tuple):
    """Permet de faire une barre de stat"""
    from PIL import Image, ImageDraw
    # create image or load your existing image with out=Image.open(path)
    d = ImageDraw.Draw(out) #out est l'image actuelle

    # draw the progress bar to given location, width, progress and color
    d = drawProgressBar(d, co[0], co[1], 500, 50, pourcentage)