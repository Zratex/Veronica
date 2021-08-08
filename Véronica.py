from datetime import date
import discord
from random import randint
import calendar
from discord.ext import commands
from discord.utils import get
import time
import os
import random
import Database
client = commands.Bot(command_prefix = 'v.')

@client.event
async def on_ready():
    print('Connectée')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="moi ! Je ne fais office que de présence 😎"))
async def on_message(message):
    #Le bot ajoute une réaction saluant la personne qui dit bonjour
    if "Bonjour" in message.content or "Coucou" in message.content or "bonjour" in message.content or "bvn" in message.content or "slt" in message.content or "Salut" in message.content or "salut" in message.content or "Slt" in message.content or "Bienvenue" in message.content or "bienvenue" in message.content or "Hi" in message.content or "hi" in message.content or "Hello" in message.content or "hello" in message.content:
        await message.add_reaction("<:Coucou:865883301814599681>")

class MyClient(discord.Client):
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return





    
@client.command()
async def here(ctx):
    """Le check in du bot"""
    if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
        role = discord.utils.get(ctx.guild.roles, name="Inscrit")
        checkin = discord.utils.get(ctx.guild.roles, name="Checked In")
        if checkin in ctx.author.roles:
            await ctx.send("Vous avez déjà confirmé votre présence !")
        else:
            if role in ctx.author.roles:
                await ctx.send("Merci d'avoir vérifié votre présence pour l'événement de la semaine <@!{}> !".format(ctx.author.id))
                await ctx.author.add_roles(checkin)
            else:
                await ctx.send("Soyez sur d'être inscrit avant de confirmer votre présence. Pour vous inscrire, effectuez la commande ``v.inscription``")
            

@client.command()
async def inscription(ctx):
    """S'inscrit à un certain event"""
    if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
        role = discord.utils.get(ctx.guild.roles, name="Inscrit")
        if role in ctx.author.roles:
            await ctx.send("Vous vous êtes déjà inscrit <@!{}> !".format(ctx.author.id))
        else:
            await ctx.send("Vous êtes désormais inscrit à l'événement de la semaine <@!{}> !".format(ctx.author.id))
            await ctx.author.add_roles(role)

@client.command()
async def test(ctx):
    """Commande de test de Zratey"""
    if ctx.author.id == 323147727779397632: #Check if it's Zratey
        untest = await ctx.send("test")
        await untest.add_reaction('👍')
        def check(reaction,emoji):
            return reaction.message.id == untest.id and str(reaction.emoji) == '👍'
        reaction, reaction_bot = await client.wait_for('reaction_add', check=check, timeout=60)
        if reaction_bot.id == untest.author.id:
            try:
                reaction, user = await client.wait_for('reaction_add', check=check, timeout=60)
                await ctx.send("Complete")
            except:
                await ctx.send("Commande interrompu. Vous avez pris trop de temps pour répondre")
    else:
        await ctx.send("Seul Zratey est autorisé à utiliser cette commande")

@client.command()
async def clear(ctx, nombre : int):
    """Supprime un certain nombre de messages selon le nombre indiqué. Cette commande est accessible seulement par les membres de la modération"""
    role = discord.utils.get(ctx.guild.roles, name="Chefs cuisiniers 🍴")
    if role in ctx.author.roles:
        messages = await ctx.channel.history(limit = nombre + 1).flatten()
        for message in messages :
            await message.delete()
        clear_done = await ctx.send("{} messages ont été effacés avec succès".format(nombre))
        time.sleep(10)
        await clear_done.delete()
    else:
        await ctx.send("Vous n'avez pas les permissions pour executer cette commande")

@client.command()
async def event(ctx):
    """Permet d'être notifié quand une information est transmise à propos d'un event organisé sur le serveur"""
    if ctx.channel.id == 397378707960102922 or ctx.channel.id == 397367943769358338:
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role in ctx.author.roles:
            await ctx.send("Vous avez déjà le role !")
        else:
            await ctx.send("Vous avez obtenu le role event <@!{}> ! Vous serez ping à chaque fois qu'un nouvel event se déroulera :)".format(ctx.author.id))
            await ctx.author.add_roles(role)

@client.command()
async def kick(ctx, userName: discord.Member, raison):
    """Commande accessible seulement à la modération de BDN permettant de kick une personne"""
    role = discord.utils.get(ctx.guild.roles, name="Chefs cuisiniers 🍴")
    if role in ctx.author.roles:
        await kick(userName, reason=raison)
        await client.channel.send("{userName} a été kick du serveur")
        
    else:
        raison="A essayé de faire son malin en voulant tester la commande de kick"
        await ctx.author.send("{0.author.mention}, Merci de ta contribution dans la 'science' voici le lien pour revenir : https://discord.gg/Pds2TyRr ")
        await kick(ctx.author, reason=raison)
        await ctx.channel.send("Vous n'avez normalement pas l'authorisation de kick quelqu'un. Donc je vous ait kick :) Ca vous apprendra")

@client.command()
async def ball(ctx):
    """Littéralement un 8ball"""
    eightballrandom = randint(1,8)
    if eightballrandom == 1:
        await ctx.send("Oui")
    elif eightballrandom == 2:
        await ctx.send("Non")
    elif eightballrandom == 3:
        await ctx.send("Peut être")
    elif eightballrandom == 4:
        await ctx.send("Surement")
    elif eightballrandom == 5:
        await ctx.send("Laisse moi réfléchir...")
        time.sleep(5)
        await ctx.send("Un peu débile comme question non ?")
    elif eightballrandom == 6:
        await ctx.send("Je n'ai pas l'autorisation de répondre à une tel question")
    elif eightballrandom == 7:
        await ctx.send("Je n'en suis pas si sûre...")
    elif eightballrandom == 8:
        await ctx.send("Pour le savoir, essais de le résoudre par toi même !")
        time.sleep(10)
        tentative_don = await ctx.send("Tu peux me payer 10$ sinon pour répondre à cette question ")
        time.sleep(2)
        await tentative_don.delete()

@client.command()
#recherche sur Google
async def google(ctx):
    """Permet de faire une recherche rapide sur Google à partir d'une simple commande"""
    txt = ctx.message.content
    txt = txt[9:]
    txt2 =""
    for x in txt:
        if x == " ":
            txt2=txt2+"_"
        else:
            txt2=txt2+x
    await ctx.channel.send("Voilà le résultat de votre recherche via le moteur de recherche Google : https://www.google.com/search?q={}".format(txt2))
    await ctx.channel.send("Peut être que la définition de ce que vous cherchez est sur Urban Dictionay ? Essayez la commande ``v.meaning``")

@client.command()
async def wiki(ctx):
    """Permet de faire une recherche rapide sur Wikipédia à partir d'une simple commande"""
    txt = ctx.message.content
    txt = txt[7:]
    txt2 =""
    for x in txt:
        if x == " ":
            txt2=txt2+"_"
        else:
            txt2=txt2+x
    await ctx.channel.send("Voilà le résultat de votre recherche via Wikipédia : https://fr.wikipedia.org/w/index.php?search={}".format(txt2))
    await ctx.channel.send("Si rien ne s'affiche, cela veux dire que ce que vous avez recherché n'existe pas sur Wikipédia. Essayez une simple recherche internet avec ``v.google``")
@client.command()
async def meaning(ctx):
    """Permet de faire une recherche rapide sur Urban Dictionnary à partir d'une simple commande"""
    txt = ctx.message.content
    txt = txt[10:]
    txt2 =""
    for x in txt:
        if x == " ":
            txt2=txt2+"_"
        else:
            txt2=txt2+x
    await ctx.channel.send("Voilà le résultat de votre recherche via Urban Dictionnary : https://www.urbandictionary.com/define.php?term={}".format(txt2))
    await ctx.channel.send("Sa définition n'existe peut être pas sur Urban Dicrionnary, donc pourquoi pas faire votre propre recherche ? Essayez la commande ``v.google``")

@client.command()
async def gamemode(ctx):
    """Cheat code"""
    await ctx.channel.send("`Java Error occured : Java is not installed in this current system because, man, je suis un Bot Discord pas l'invité de commande MineCraft`")

# -------------------------------------------------------------- DATABASE ----------------------------------------------------------------

def verification(id):
    #vérifie dans la base de donnée
    test=Database.testUser(id)
    if test == 2 :
        #Le compte existe
        return True
    else :
        #Le compte n'existe pas
        return False

@client.command()
async def setup(ctx):
    Creation=Database.creataccount(ctx.author.id)
    if Creation == 1 :
        await ctx.channel.send("Le compte a été ajouté")
    else :
        await ctx.channel.send("Vous avez déjà un compte")
@client.command()
async def profile(ctx):
    """Montre le profile de l'utilisateur, en apportant des éléments d'informations divers et variés"""
    test=verification(ctx.author.id)
    if test :
        info = Database.info(ctx.author.id)
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_author(name="Profile de {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Identifiant Discord", value="{}".format(ctx.author.id), inline=False)
        embedVar.add_field(name="Money en banque", value="{}<:coquillette:802972160364249119>".format(info[4]), inline=True)
        date=ctx.author.created_at
        date=date.strftime("%d/%m/%Y, %H:%M:%S")
        embedVar.add_field(name="Date de création du compte Discord", value="{}".format(date), inline=True)
        date=ctx.author.joined_at
        date=date.strftime("%d/%m/%Y, %H:%M:%S")
        embedVar.add_field(name="Date où vous avez rejoint ce serveur", value="{}".format(date), inline=True)
        embedVar.add_field(name="Role principal", value="{}".format(ctx.author.top_role.mention), inline=True)
        embedVar.add_field(name="Création compte Véronica", value="{}".format(info[6]), inline=True)
        embedVar.add_field(name="Niveau d'experience", value="Niveau {}".format(info[1]), inline=True)
        await ctx.send(embed=embedVar)
    else : 
        print("je suis dans le false de user info")
        await ctx.channel.send("Merci de faire un v.setup pour créer un compte")
@client.command()
async def delete(ctx):
    test=verification(ctx.author.id)
    if test :
        info = Database.deletecompte(ctx.author.id)
    else : 
        print("je suis dans le false de delete")
        await ctx.channel.send("Merci de faire un v.setup pour créer un compte")

@client.command()
async def daily(ctx): 
    test=verification(ctx.author.id)
    if test:
        info = Database.daily(ctx.author.id)
        if info == 0:
            await ctx.channel.send("Cela ne fait pas 24h que vous avez effectué la commande. Veuillez patienter")
        else:
            await ctx.channel.send("Votre argent a été créditer. Votre solde actuel est de {}<:coquillette:802972160364249119>".format(info))
    else : 
        await ctx.channel.send("Merci de faire un v.setup pour créer un compte")

# -------------------------------------------------------------- FIN DATABASE ----------------------------------------------------------------
@client.command()
async def pdp(ctx):
    embedVar = discord.Embed(color=discord.Color.blue())
    embedVar.add_field(name="Commande réalisée par {}".format(ctx.author), value="Voici votre photo de profile", inline=False)
    embedVar.set_image(url="{}".format(ctx.author.avatar_url))
    await ctx.send(embed=embedVar)

filetoken = open(f"E:\\Véronica\\token.txt", "r")
for x in filetoken:
    token=x
filetoken.close()
client.run(token)
