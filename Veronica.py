import discord
from discord import app_commands
from discord.ext import commands

bot=commands.Bot(command_prefix="v.", intents=discord.Intents.all(),owner=323147727779397632) # Zratey#0860 :D

@bot.event
async def on_ready():
    print("Connectée !")
    try:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="moi ! Je ne fais office que de présence 😎"))
    except Exception as a:
        print(a)

@bot.tree.command(name="load",description="Charge un module de commandes. Cette commande n'est utilisable que par Zratey")
@app_commands.describe(module="Module à charger")
async def load(interaction: discord.Interaction, module: str):
    if interaction.user.id==323147727779397632:
        try:
            await bot.load_extension(module)
            await interaction.response.send_message(f"L'extension {module} a bel et bien été chargée !",ephemeral=False)
        except Exception as a:
            await interaction.response.send_message(f"Une erreur est survenue en essayant de charger le module {module} : `{a}`",ephemeral=False)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

@bot.tree.command(name="reload",description="Recharge un module de commandes. Cette commande n'est utilisable que par Zratey")
@app_commands.describe(module="Module à recharger")
async def reload(interaction: discord.Interaction, module: str):
    if interaction.user.id==323147727779397632:
        try:
            await bot.reload_extension(module)
            await interaction.response.send_message(f"L'extension {module} a bel et bien été rechargée !",ephemeral=False)
        except Exception as a:
            await interaction.response.send_message(f"Une erreur est survenue en essayant de charger le module {module} : `{a}`",ephemeral=False)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

@bot.tree.command(name="unload",description="Décharge un module de commandes. Cette commande n'est utilisable que par Zratey")
@app_commands.describe(module="Module à décharger")
async def unload(interaction: discord.Interaction, module: str):
    if interaction.user.id==323147727779397632:
        try:
            await bot.unload_extension(module)
            await interaction.response.send_message(f"L'extension {module} a bel et bien été déchargée !",ephemeral=False)
        except Exception as a:
            await interaction.response.send_message(f"Une erreur est survenue en essayant de décharger le module {module} : `{a}`",ephemeral=False)
    else:
        await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

# --- Commande de synchronysation des commandes '/' ---
@bot.command() #Commande sans '/'
@commands.guild_only()
@commands.is_owner() #Utilisable que par Zratey, the last knight pour une raison que j'ignore
async def sync(ctx) -> None:
    await ctx.bot.tree.sync()
    await ctx.send("Commandes resynchronisées")
    print("Commandes resynchronisées")

filetoken = open(f"E:\\Documents\\Véronica\\token.txt", "r")
for x in filetoken:
    token=x
filetoken.close()
bot.run(token)
