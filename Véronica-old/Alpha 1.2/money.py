import discord
from discord.ext import commands
import Database

def verification(id):
    #vérifie dans la base de donnée
    test=Database.testUser(id)
    if test == 2 :
        #Le compte existe
        return True
    else :
        #Le compte n'existe pas
        return False

def setup(bot):
    bot.add_cog(ModerationCommandes(bot))

class ModerationCommandes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def daily(self,ctx): 
        test=verification(ctx.author.id)
        if test:
            info = Database.daily(ctx.author.id)
            if info == 0:
                await ctx.channel.send("Cela ne fait pas 24h que vous avez effectué la commande. Veuillez patienter")
            else:
                await ctx.channel.send("Votre argent a été créditer. Votre solde actuel est de {}<:coquillette:802972160364249119>".format(info))
        else : 
            await ctx.channel.send("Merci de faire un v.setup pour créer un compte")

    @commands.command()
    async def shop(self,ctx):
        """Shop de Véronica"""
        await ctx.channel.send("Bienvenue dans le shop ! Veuillez sélectionner quelque chose à acheter en répondant à mon message par le numéro qui correspond à votre achat.")
        embedVar = discord.Embed(title="Véronica's shop !", description="Le shop de Véronica si vous avez du mal avec l'anglais <:Zeldahihi:905815541342691388>", color=discord.Color.blue())
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Shop Hardware", value="Executez la commande v.rigshop pour le shop de pièces de PC !", inline=False)
        embedVar.add_field(name=":one: Rôle personnalisé", value="Coût : 15000<:coquillette:802972160364249119>", inline=True)
        embedVar.set_footer(text="Véronica Alpha 1.2")
        untest = await ctx.send(embed=embedVar)
        await untest.add_reaction("1\ufe0f\N{COMBINING ENCLOSING KEYCAP}")
        #Pour éviter que le bot se détecte parmis les personnes qui ont réagis au message
        def check(reaction,emoji): #Définition pour check si c'est bien le bon message
            return reaction.message.id == untest.id
        reaction, reaction_bot = await self.bot.wait_for('reaction_add', check=check, timeout=60)
        if reaction_bot.id == untest.author.id: #Attente d'une réaction
            reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=60)
            if user.id == ctx.author.id: #Vérifie que c'est la bonne personne qui a réagit au message
                print(reaction)
                if str(reaction) == "1️⃣": #Check si l'utilisateur a réagis à la réaction n°1
                    perso = Database.depense(ctx.author.id,15000)
                    if perso == 1: #assez d'argent > Attribution du role
                        await ctx.send("Vous avez reçu la permission d'avoir un rôle personnalité {} ! Veuillez contacter un membre de la modération en lui montrant ce message en guise de preuve. Ensuite, précisez lui la couleur, ainsi que le nom de ce role.".format(ctx.author.mention))
                    else:
                        await ctx.send("Vous n'avez pas assez de <:coquillette:802972160364249119> pour vous procurer ce rôle !")
                else: #Erreur parmis les propositions
                    await ctx.send("Erreur dans la boutique <@!323147727779397632>")
            else: #mauvaise personne qui répond
                await ctx.send("Ce n'est pas à vous {} de réagir au message ! La commande a été annulé, {} réeffectuez la commande pour la réinitialiser".format(user.mention,ctx.author.mention))
