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

@client.event
async def on_message(message):
    #Réaction coucou
    if "Bonjour" in message.content or "Coucou" in message.content or "bonjour" in message.content or "bvn" in message.content or "slt" in message.content or "Salut" in message.content or "salut" in message.content or "Slt" in message.content or "Hello" in message.content or "hello" in message.content:
        #Le bot ajoute une réaction saluant la personne qui dit bonjour
        if "DimiSalut" not in message.content:
            await message.add_reaction("<:Coucou:865883301814599681>")
    
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



# -------------------------------------------------------------- DATABASE ----------------------------------------------------------------

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
        await ctx.channel.send("Merci de faire un v.setup pour créer un compte")
@client.command()
async def delete(ctx):
    test=verification(ctx.author.id)
    if test :
        info = Database.deletecompte(ctx.author.id)
    else : 
        print("je suis dans le false de delete")
        await ctx.channel.send("Merci de faire un v.setup pour créer un compte")



# -------------------------------------------------------------- FIN DATABASE ----------------------------------------------------------------
# -------------------------------------------------------------- ARGENT ----------------------------------------------------------------
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

@client.command()
async def shop(ctx):
    """Shop de Véronica"""
    await ctx.channel.send("Bienvenue dans le shop ! Veuillez sélectionner quelque chose à acheter en répondant à mon message par le numéro qui correspond à votre achat.")
    embedVar = discord.Embed(title="Véronica's shop !", description="Le shop de Véronica si vous avez du mal avec l'anglais <:Wink:608327025098489863>", color=discord.Color.blue())
    embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
    embedVar.add_field(name=":one: Rôle DJ", value="Coût : 500<:coquillette:802972160364249119>", inline=True)
    embedVar.add_field(name=":two: Rôle personnalisé", value="Coût : 15000<:coquillette:802972160364249119>", inline=True)
    embedVar.set_footer(text="Alpha version of Véronica")
    untest = await ctx.send(embed=embedVar)
    await untest.add_reaction("1\ufe0f\N{COMBINING ENCLOSING KEYCAP}")
    await untest.add_reaction("2\ufe0f\N{COMBINING ENCLOSING KEYCAP}")
    #Pour éviter que le bot se détecte parmis les personnes qui ont réagis au message
    def check(reaction,emoji): #Définition pour check si c'est bien le bon message
        return reaction.message.id == untest.id
    reaction, reaction_bot = await client.wait_for('reaction_add', check=check, timeout=60)
    if reaction_bot.id == untest.author.id:
        #Attente d'une réaction
        reaction, user = await client.wait_for('reaction_add', check=check, timeout=60)
        if user.id == ctx.author.id: #Vérifie que c'est la bonne personne qui a réagit au message
            print(reaction)
            if str(reaction) == "1️⃣": #Check si l'utilisateur a réagis au msg n°1
                #initialisation de la commande pour ajouter le role DJ
                role = discord.utils.get(ctx.guild.roles, name="DJ")
                if role in ctx.author.roles:
                    ctx.send("Vous avez déjà le rôle DJ !")
                else:
                    DJ = Database.depense(ctx.author.id,500)
                    #Vérifie si l'utilisateur a assez d'argent
                    if DJ == 1: #assez d'argent > Attribution du role
                        await ctx.author.add_roles(role)
                        await ctx.send("Vous avez obtenu le role DJ !")
                    else: #pas assez d'argent
                        await ctx.send("Vous n'avez pas assez de <:coquillette:802972160364249119> pour vous procurer ce rôle !")
            elif str(reaction) == "2️⃣":
                perso = Database.depense(ctx.author.id,15000)
                if perso == 1: #assez d'argent > Attribution du role
                    await ctx.send("Vous avez reçu la permission d'avoir un rôle personnalité {} ! Veuillez contacter un membre de la modération en lui montrant ce message en guise de preuve. Ensuite, précisez lui la couleur, ainsi que le nom de ce role.".format(ctx.author.mention))
                else:
                    await ctx.send("Vous n'avez pas assez de <:coquillette:802972160364249119> pour vous procurer ce rôle !")
            else: #Erreur parmis les propositions
                await ctx.send("Erreur dans la boutique <@!323147727779397632>")
        else: #mauvaise personne qui répond
            await ctx.send("Ce n'est pas à vous {} de réagir au message ! La commande a été annulé, {} réeffectuez la commande pour la réinitialiser".format(user.mention,ctx.author.mention))
# -------------------------------------------------------------- FIN ARGENT ----------------------------------------------------------------


filetoken = open(f"E:\\Véronica\\token.txt", "r")
for x in filetoken:
    token=x
filetoken.close()
client.run(token)
