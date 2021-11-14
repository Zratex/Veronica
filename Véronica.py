from datetime import date
import discord
from discord.ext import commands
import Database
client = commands.Bot(command_prefix = 'v.')

@client.event
async def on_ready():
    print('Connectée')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="moi ! Je ne fais office que de présence 😎"))

def verification(id):
    #vérifie dans la base de donnée
    test=Database.testUser(id)
    if test == 2 :
        #Le compte existe
        return True
    else :
        #Le compte n'existe pas
        return False

@client.event
async def on_message(message):
    if message.author.id == 752958545758126082:
        return
    else:
        #Réaction coucou
        slt=["bonjour","coucou","bonsoir","bvn","slt","salut","hello"]
        cc=0
        for elt in slt:
            if elt in message.content.lower():
                if "DimiSalut" not in message.content:
                    cc=1
        if cc == 1:
            await message.add_reaction("<:Coucou:865883301814599681>") #Le bot ajoute une réaction saluant la personne qui dit bonjour
            
        auteur = message.author
        if not message.guild:
            channel = await client.fetch_user(323147727779397632)
            await channel.send("Reçu de la part de {}: {}".format(auteur,message.content))
            await client.process_commands(message)
    
    #Xp
    if not message.author.bot:
        if message.channel.id == 397378707960102922:
            test=verification(message.author.id)
            if test: #Vérifie si l'utilisateur a un compte
                xp = Database.exp(message.author.id)
                if xp[0] == 1: #Si il y a un rankup
                    print("{} est passé niveau {}".format(message.author.mention,xp[1]))
                    await message.channel.send("Félicitations {} ! Vous êtes désormais passé niveau {} !".format(message.author.mention,xp[1]))
            else: #Sinon il lui en créer un
                Creation=Database.creataccount(message.author.id)
                await message.channel.send("{} je vous ait automatiquement créé un compte !".format(message.author.mention))
    #Pour "commit" le on_message :
    await client.process_commands(message)

class MyClient(discord.Client):
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

@client.command()
async def load(ctx, name=None):
    """Permet de charger une extension de commandes"""
    if ctx.author.id == 323147727779397632:
            if name:
                client.load_extension(name)
                await ctx.send("Le fichier d'extention `{}.py` a bel et bien été chargé.".format(name))
    else:
        await ctx.send("Je n'autorise pas n'importe qui à me toucher !")

@client.command()
async def unload(ctx, name=None):
    """Permet de décharger une extension de commandes"""
    if ctx.author.id == 323147727779397632:
        try:
            if name:
                client.unload_extension(name)
                await ctx.send("Le fichier d'extention `{}.py` a bel et bien été déchargé.".format(name))
        except:
            await ctx.send("Le fichier d'extension `{}.py` n'a pas pu être déchargé (ou il n'existe pas).".format(name))
    else:
        await ctx.send("Je n'autorise pas n'importe qui à me toucher !")


@client.command()
async def reload(ctx, name=None):
    if ctx.author.id == 323147727779397632:
        if name:
            try:
                client.reload_extension(name)
                await ctx.send("Le fichier d'extention `{}.py` a bel et bien été rechargé.".format(name))
            except:
                try:
                    client.load_extension(name)
                    await ctx.send("Le fichier d'extention `{}.py` a bel et bien été chargé.".format(name))
                except:
                    await ctx.send("Le fichier d'extension `{}.py` n'a pas pu être rechargé (ou il n'existe pas).".format(name))
    else:
        await ctx.send("Je n'autorise pas n'importe qui à me toucher !")

filetoken = open(f"D:\\Documents\\Véronica\\token.txt", "r")
for x in filetoken:
    token=x
filetoken.close()
client.run(token)
