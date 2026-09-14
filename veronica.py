import discord
from discord import app_commands
from discord.ext import commands
import database_init

zratey_id=323147727779397632
bot=commands.Bot(command_prefix="v.", intents=discord.Intents.all(),owner=zratey_id) # Zratey#0860 :D
# Création de l'indexation des Cogs sous forme de dictionnaire, dédié aux Cogs qui ne sont pas dans le fichier racine du dépôt
listOfCogs={"cogs.tamagotchi.tamagotchi_main": ["tamagochi, tamagotchi, tamagoshi"],
            "cogs.user.profile": ["profile"]}

@bot.event
async def on_ready():
    bot.pool = await database_init.create_db_pool() #Connexion à la BD
    await database_init.init_db(bot.pool) #Initialise la BD si elle est vide
    print("Connectée !")
    try:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="moi ! Je ne fais office que de présence 😎"))
    except Exception as a:
        print(a)

@bot.tree.command(name="load",description="Charge un module de commandes. Cette commande n'est utilisable que par Zratey")
@app_commands.describe(module="Module à charger")
async def load(interaction: discord.Interaction, module: str):
    if interaction.user.id==zratey_id:
        try:
            module = [k for k, v in listOfCogs.items() if module.lower() in v][0] #One liner fait fait ChatGPT permettant d'avoir la clé à partir d'une valeur
            await bot.load_extension(module)
            await interaction.response.send_message(f"L'extension `{module}` a bel et bien été chargée !",ephemeral=False)
        except Exception as a:
            if type(a) == IndexError:
                await interaction.response.send_message(f"Le module **{module}** n'existe pas, ou n'a pas été trouvé")
            else:
                await print(a) 
                await interaction.response.send_message(f"Une erreur est survenue en essayant de charger le module **{module}** : `{a}`",ephemeral=False)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

@bot.tree.command(name="reload",description="Recharge un module de commandes. Cette commande n'est utilisable que par Zratey")
@app_commands.describe(module="Module à recharger")
async def reload(interaction: discord.Interaction, module: str):
    if interaction.user.id==zratey_id:
        try:
            module = [k for k, v in listOfCogs.items() if module.lower() in v][0] #One liner fait fait ChatGPT permettant d'avoir la clé à partir d'une valeur
            await bot.reload_extension(module)
            await interaction.response.send_message(f"L'extension `{module}` a bel et bien été rechargée !",ephemeral=False)
        except Exception as a:
            if type(a) == IndexError:
                await interaction.response.send_message(f"Le module **{module}** n'existe pas, ou n'a pas été trouvé")
            else:
                await interaction.response.send_message(f"Une erreur est survenue en essayant de charger le module {module} : `{a}`",ephemeral=False)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

@bot.tree.command(name="unload",description="Décharge un module de commandes. Cette commande n'est utilisable que par Zratey")
@app_commands.describe(module="Module à décharger")
async def unload(interaction: discord.Interaction, module: str):
    if interaction.user.id==zratey_id:
        try:
            module = [k for k, v in listOfCogs.items() if module.lower() in v][0] #One liner fait fait ChatGPT permettant d'avoir la clé à partir d'une valeur
            await bot.unload_extension(module)
            await interaction.response.send_message(f"L'extension `{module}` a bel et bien été déchargée !",ephemeral=False)
        except Exception as a:
            if type(a) == IndexError:
                await interaction.response.send_message(f"Le module **{module}** n'existe pas, ou n'a pas été trouvé")
            else:
                await interaction.response.send_message(f"Une erreur est survenue en essayant de décharger le module {module} : `{a}`",ephemeral=False)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

@bot.event
async def on_command_error(ctx,error):
    import traceback
    import sys
    erreur=getattr(error,'original',error)
    if isinstance(erreur,commands.CommandNotFound):
        await ctx.send("La commande que vous avez essayé d'entrer **n'existe pas**, ou le module associé n'a pas été chargé <:zeldashrug:914140291802464258>")
    elif isinstance(erreur,commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument à la commande, essayez de nouveau peut être ?")
    else:
        await print("Erreur dans le channel {} par {} :\n{}".format(ctx.channel,ctx.author,erreur))
        await ctx.send("Une erreur est survenue lors de votre tentative d'execution de la commande. Veuillez faire un report de bug dans le salon <#836700382138859540>\n__Voici l'erreur en question :__\n```{}```".format(erreur))
        traceback.print_exception(type(erreur), erreur, erreur.__traceback__, file=sys.stderr)

# --- Commande de synchronysation des commandes '/' ---
@bot.command() #Commande sans '/'
@commands.guild_only()
@commands.is_owner()
async def sync(ctx) -> None:
    await ctx.bot.tree.sync()
    await ctx.send("Commandes resynchronisées")
    print("Commandes resynchronisées")

""" === Méthode connexion bot avec fichier
filetoken = open(f"token.txt", "r")
for x in filetoken:
    token=x
filetoken.close()
bot.run(token)
"""

""" === Méthode connexion bot avec dockerfile (à tester) ==="""
import os
token = os.environ.get("DISCORD_TOKEN")
if not token:
    raise ValueError("Le token Discord n'est pas défini dans les variables d'environnement (DISCORD_TOKEN).")
bot.run(token)