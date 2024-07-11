from datetime import date
import discord
from discord.ext import commands
import Database
client = commands.Bot(command_prefix = 'v.')
client.remove_command("help") #la suppression de la commande help permet de ne plus avoir la commande par défaut de Discord.py, mais la personnalisée de l'extension help.py

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
        if auteur.id==329554825907798019: #Réponds feur à Kamlox
            if message.content[-4:].lower() == "quoi" or message.content[-3:].lower() == "koi":
                await message.channel.send("FEUR")
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
        try:
            if name=="all": #charge tout les modules
                client.load_extension("basics")
                client.load_extension("mod")
                client.load_extension("money")
                client.load_extension("data")
                client.load_extension("rig")
                client.load_extension("help")
                await ctx.send("Tout les modules ont été chargés.")
            elif name: 
                client.load_extension(name)
                await ctx.send("Le fichier d'extension `{}.py` a bel et bien été chargé.".format(name))
        except:
            await ctx.send("Une erreur est survenue lors du chargement de l'extension")
    else:
        await ctx.send("Je n'autorise pas n'importe qui à me toucher !")

@client.command()
async def unload(ctx, name=None):
    """Permet de décharger une extension de commandes"""
    if ctx.author.id == 323147727779397632:
        try:
            if name:
                client.unload_extension(name)
                await ctx.send("Le fichier d'extension `{}.py` a bel et bien été déchargé.".format(name))
        except:
            await ctx.send("Le fichier d'extension `{}.py` n'a pas pu être déchargé (ou il n'existe pas).".format(name))
    else:
        await ctx.send("Je n'autorise pas n'importe qui à me toucher !")


@client.command()
async def reload(ctx, name=None):
    if ctx.author.id == 323147727779397632:
        try:
            if name=="all": #recharge tout les modules
                client.reload_extension("basics")
                client.reload_extension("mod")
                client.reload_extension("money")
                client.reload_extension("data")
                client.reload_extension("rig")
                client.reload_extension("help")
            elif name:
                try:
                    client.reload_extension(name)
                    await ctx.send("Le fichier d'extension `{}.py` a bel et bien été rechargé.".format(name))
                except: #Erreur si l'extension en question n'est pas déjà chargée
                    try:
                        client.load_extension(name)
                        await ctx.send("Le fichier d'extension `{}.py` a bel et bien été chargé.".format(name))
                    except: #erreur chargement fichier d'extension
                        await ctx.send("Le fichier d'extension `{}.py` n'a pas pu être rechargé (ou il n'existe pas).".format(name))
        except: #Erreur lors du chargement avec l'argument 'all' si les fichiers ne sont pas déjà chargés
            try:
                if name=="all": #charge tout les modules
                    client.load_extension("basics")
                    client.load_extension("mod")
                    client.load_extension("money")
                    client.load_extension("data")
                    client.load_extension("rig")
                    client.load_extension("help")
                    await ctx.send("Tout les modules ont été chargés.")
            except:
                await ctx.send("Une erreur est survenue lors du chargement des extensions")
    else:
        await ctx.send("Je n'autorise pas n'importe qui à me toucher !")

filetoken = open(f"D:\\Documents\\Véronica\\token.txt", "r")
for x in filetoken:
    token=x
filetoken.close()
client.run(token)
