from os import name
import discord
from discord import embeds
from discord.embeds import Embed
from discord.ext import commands
import Database
import rig_sql

def setup(bot):
    bot.add_cog(CommandesBasiques(bot))

class CommandesBasiques(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=['pc'])
    async def rig(self,ctx,arg=None):
        """Affiche les éléments dans le rig de l'utilisateur."""
        if str(arg).lower() == "cpu": #Affiche le menu relatif au CPU
            if rig_sql.testuser(ctx.author.id): #Vérifie que l'utilisateur a un CPU
                embedVar=discord.Embed(title="CPUs de {} !".format(ctx.author), description="Gestionnaire des CPUs du stock de {}".format(ctx.author), color=discord.Color.blue())
                embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
                embedVar.set_footer(text="Véronica Alpha 1.2")
                embedVar.add_field(name="CPU actuel", value="Nom : {} | Tier : {}".format(rig_sql.usercpu(ctx.author.id,1)[0],rig_sql.usercpu(ctx.author.id,1)[1]),inline=False)
                embedVar.add_field(name="CPUs en stock :", value="{}".format(len(rig_sql.usercpu(ctx.author.id,0))),inline=False)
                for i in range(len(rig_sql.usercpu(ctx.author.id,0))): #Répétition selon le nombre de CPUs
                    embedVar.add_field(name="Stocked CPU n°{} :".format(i+1), value="Nom : {} | Tier : {}".format(rig_sql.usercpu(ctx.author.id,0)[i][0],rig_sql.usercpu(ctx.author.id,0)[i][1]),inline=True)
                await ctx.send(embed=embedVar)
            else:
                await ctx.send("Vous n'avez pas acheté de processeur !")
        elif str(arg).lower() in ["alim","alimentation","power","consommation"]: #Affiche le menu relatif à l'alim
            if rig_sql.alim(ctx.author.id): #Vérifie que l'utilisateur a une alim
                embedVar=discord.Embed(title="Alimentation de {} !".format(ctx.author), description="Gestionnaire de l'alimentation électrique de {}".format(ctx.author),color=discord.Color.blue())
                embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
                embedVar.set_footer(text="Véronica Alpha 1.2")
                embedVar.add_field(name="Alimentation",value="{}W".format(rig_sql.useralim(ctx.author.id)),inline=False)
                embedVar.add_field(name="Consommation totale",value="{}W".format(rig_sql.cpupower(rig_sql.usercpu(ctx.author.id,1)[1])),inline=True)
                embedVar.add_field(name="Consommation CPU",value="{}W".format(rig_sql.cpupower(rig_sql.usercpu(ctx.author.id,1)[1])),inline=True)
                embedVar.add_field(name="Consommation GPU",value="0W",inline=True)
                await ctx.send(embed=embedVar)
            else:
                await ctx.send("Vous n'avez pas acheté d'alimentation' !")
        elif str(arg).lower() == "gpu": #Affiche le menu relatif au GPU
            try:
                if rig_sql.testuser(ctx.author.id): #Vérifie que l'utilisateur a un CPU
                    embedVar=discord.Embed(title="GPUs de {} !".format(ctx.author), description="Gestionnaire des GPUs du stock de {}".format(ctx.author), color=discord.Color.blue())
                    embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
                    embedVar.set_footer(text="Véronica Alpha 1.2")
                    for i in range(rig_sql.usercpu(ctx.author.id,1)[1]):
                        embedVar.add_field(name="GPU n°{} :".format(i),value="Nom : {} | Consommation : {}W | Rentabilité : {}".format(rig_sql.usergpu(ctx.author.id,1)[i][0],rig_sql.gpupower(rig_sql.usergpu(ctx.author.id,1)[i][0]),rig_sql.rentgpu(rig_sql.usergpu(ctx.author.id,1)[i][0])),inline=True)
                    embedVar.add_field(name="GPUs en stock :", value="{}".format(len(rig_sql.usergpu(ctx.author.id,0))),inline=False)
                    for i in range(len(rig_sql.usergpu(ctx.author.id,0))):
                        embedVar.add_field(name="Stocked GPU n°{} :".format(i+1),value="Nom : {} | Consommation : {}W | Rentabilité : {}".format(rig_sql.usergpu(ctx.author.id,1)[i][0],rig_sql.gpupower(rig_sql.usergpu(ctx.author.id,1)[i][0]),rig_sql.rentgpu(rig_sql.usergpu(ctx.author.id,1)[i][0])),inline=True)
                    await ctx.send(embed=embedVar)
                else:
                    await ctx.send("Vous n'avez pas acheté de processeur !")
            except:
                await ctx.send("Il y a une erreur lors de l'execution de cette commande. Peut être vous n'avez pas de GPU <:Zeldapose:905816408267571200> ")
        elif arg==None:
            if rig_sql.testuser(ctx.author.id):
                embedVar=discord.Embed(title="PC de {} !".format(ctx.author), description="Gestionnaire du rig de {}".format(ctx.author), color=discord.Color.blue())
                embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
                embedVar.set_footer(text="Véronica Alpha 1.2")
                embedVar.add_field(name="CPU actuel", value="Nom : {} | Tier : {}".format(rig_sql.usercpu(ctx.author.id,1)[0],rig_sql.usercpu(ctx.author.id,1)[1]),inline=False)
                embedVar.add_field(name="CPUs en stock :", value="{}".format(len(rig_sql.usercpu(ctx.author.id,0))),inline=True)
                embedVar.add_field(name="Alimentation",value="{}W".format(rig_sql.useralim(ctx.author.id)),inline=True)
                embedVar.add_field(name="Consommation",value="{}W".format(rig_sql.cpupower(rig_sql.usercpu(ctx.author.id,1)[1])),inline=True)
                if rig_sql.usercpu(ctx.author.id,1)[1] ==0:
                    for i in range(rig_sql.usercpu(ctx.author.id,1)[1]):
                        embedVar.add_field(name="GPU n°{} :".format(i+1),value="{}".format(rig_sql.usergpu(ctx.author.id,1)[i][0]),inline=True)
                    embedVar.add_field(name="GPUs en stock :", value="{}".format(len(rig_sql.usergpu(ctx.author.id,0))),inline=True)
                await ctx.send(embed=embedVar)
            else:
                await ctx.send("Vous n'avez pas acheté de processeur !")

    @commands.command()
    async def rigshop(self,ctx):
        """Shop de la partie cryptomonnaie du Bot !"""
        embedVar = discord.Embed(title="Véronica's rigs shop !", description="Le shop de Véronica dédié à l'achat de matériel pour les PC !", color=discord.Color.blue())
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.set_footer(text="Véronica Alpha 1.2")
        if rig_sql.testuser(ctx.author.id): #test que l'utilisateur ait bien un rig pour poursuivre
            await ctx.send(embed=embedVar)
            await ctx.send("Faut que la suite soit programmée !")
        else:
            embedVar.add_field(name="Aucun rig détecté",value="Vous n'avez pas encore de rig. Vous devez en avoir un pour pouvoir utiliser cette commande. Voulez vous payer 1150<:coquillette:802972160364249119> pour avoir une base ?",inline=True)
            embedVar.add_field(name="Détails du rig par défaut :", value="CPU : Altaïr | Carte mètre : Intel 4th gen | Alimentation: 330W",inline=True)
            embedVar.add_field(name=":white_check_mark:", value="Oui",inline=False)
            embedVar.add_field(name=":x:",value="Non",inline=False)
            untest = await ctx.send(embed=embedVar)
            await untest.add_reaction("✅")
            await untest.add_reaction("❌")
            def check(reaction,emoji): #Définition pour check si c'est bien le bon message
                return reaction.message.id == untest.id
            reaction, reaction_bot=await self.bot.wait_for('reaction_add',check=check, timeout=60)
            if reaction_bot.id == untest.author.id: #Permet d'ignorer Véronica. Attente d'une réaction
                reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=60)
                if user.id == ctx.author.id: #Vérifie que c'est la bonne personne qui a réagit au message
                    if str(reaction)=="✅": #L'utilsateur accepte l'achat
                        perso = Database.depense(ctx.author.id,1150)
                        if perso ==1: #assez d'argent pour le CPU
                            if rig_sql.getcpu(ctx.author.id,1):
                                if rig_sql.newalim(ctx.author.id,330):
                                    await ctx.send("La transaction s'est effectué avec succès. Vous avez désormais un PC !")
                                else:
                                    await ctx.send("Erreur lors de l'acquisition de l'alim. Veuillez contacter l'owner")
                            else:
                                await ctx.send("Erreur lors d'acquisition du processeur. Veuillez contacter l'owner.")
                        else:
                            await ctx.send("Vous n'avez pas assez de <:coquillette:802972160364249119> !")
                    elif str(reaction)=="❌": #L'utilsateur n'accepte pas l'achat
                        await ctx.send("A bientôt !")
                else: #mauvaise personne qui répond
                    await ctx.send("Ce n'est pas à vous {} de réagir au message ! La commande a été annulé, {} réeffectuez la commande pour la réinitialiser".format(user.mention,ctx.author.mention))
