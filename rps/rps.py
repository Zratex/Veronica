import discord
from discord.ext import commands
from discord import app_commands

from random import randint
from rpsFunctions import * #Importation des fonctions nécessaires au bout fonctionnement du RPS

class RPS(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #TEST COMMAND
    @commands.hybrid_command(name="rps",description="Jouez à Pierre Feuille Ciseaux !")
    @app_commands.describe(user="Utilisateur à sélectionner. Si aucun utilisateur de sélectionnée, cela reviendra à affronter Véronica")
    async def rps(self,ctx: commands.Context,user: discord.Member=None):
        if user==None or user.id!=ctx.author.id:
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text="Véronica Alpha 1.3")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
            if user==None or user.id==752958545758126082: #L'ID de Véronica
                embedVar.add_field(name="Veronica VS Human",value="Azy, je te laisse faire ta sélection en premier. Prends juste en considération que ta défaite est évidente <:ZeldaMenacing:1099801907658248323>", inline=False)
                BUTTONS=rpsSOLO(ctx=ctx)
                await ctx.send(embed=embedVar,view=BUTTONS)
                await BUTTONS.wait() #On attends la réponse de l'utilisateur
                if not BUTTONS.value: #Si la valeure de la classe du bouton est à false, cela veut dire que la commande a été annulée
                    await ctx.send("Très bien. A une prochaine fois alors ^^")
                else:
                    #On regénère une nouvelle embed : Le résultat du match
                    embedVar = discord.Embed(color=discord.Color.blue())
                    embedVar.set_footer(text="Véronica Alpha 1.3")
                    choice=randint(1,3)
                    embedVar.add_field(name=f"{ctx.author.name} VS. Veronica",value=f"{ctx.author.name} the human VS. the best Discord bot, according to an objective opinion from: Veronica", inline=False)
                    embedVar.add_field(name=f"Selection of {ctx.author.name} :",value=f"{RPSintTOstr(BUTTONS.value)}", inline=True)
                    embedVar.add_field(name=f"Selection of Veronica (the cooler one fr, ong, no cap) :",value=f"{RPSintTOstr(choice)}", inline=True)
                    result= RPSwinner(BUTTONS.value,choice)
                    if result==1:
                        embedVar.add_field(name=f"{ctx.author.name}..WINS !",value="Bien joué, t'as été meilleur pour le coup..",inline=False)
                    elif result==2:
                        embedVar.add_field(name="Veronica won !!!",value="T'es pas nul et loin de là, mais c'est juste que je suis meilleur pour le coup",inline=False)
                    elif result==3:
                        embedVar.add_field(name="Tie !",value="Egalité ?! Hmm..je m'attendais pas à cela. Bien joué sur ce coup.",inline=False)
                    await ctx.send(embed=embedVar)
            else:
                BUTTONS=request(user.id)
                await ctx.send(f"```1V1 RPS Battle request```\n{ctx.author.mention} veux vous affronter en duel de **Pierre Feuille Ciseaux** {user.mention} ! Acceptez vous sa requête ?",view=BUTTONS)
                await BUTTONS.wait() #On attends la réponse de l'utilisateur
                if BUTTONS.value: #Si l'utilisateur a accepté la requête
                    embedVar.add_field(name="Selection phase",value="Veuillez réaliser vos choix. Que le meilleur gagne !",inline=False)
                    #Pour une raison que j'ignore :
                    newMSG=self.bot.get_channel(ctx.channel.id) #je suis obligé de faire en sorte de re-récupérer le channel pour faire un nouveau message
                    #Afin de pouvoir faire un thread correctement :
                    init_message = await newMSG.send(f"RPS 1V1 Battle\n```{ctx.author} VS. {user}```") #Message de création du thread
                    thread = await init_message.create_thread(name=f"RPS : {ctx.author} VS. {user} | {currenttime()}",auto_archive_duration=60,reason="1v1 RPS of {ctx.author} VS. {user}") #Création du thread
                    message = self.bot.get_channel(thread.id) #Acquisition de la capacité à écrire dans le thread
                    BUTTONS=rpsVersus(ctx,user,message) #On met les boutons pour sélectionner le stuff
                    await message.send(f"```diff\n- Let the battle begins !```\n{ctx.author.mention} VS. {user.mention}",embed=embedVar,view=BUTTONS)
                    await BUTTONS.wait() #On attends la réponse des utilisateurs
                    if not BUTTONS.value: #Si l'intéraction a été annulée
                        await ctx.send("Le combat a été interrompu")
                    else:
                        #Traitement du résultat des sélections
                        result=RPSwinner(BUTTONS.p1select,BUTTONS.p2select)
                        #On regénère une nouvelle embed : Le résultat du match
                        embedVar = discord.Embed(color=discord.Color.blue())
                        embedVar.set_footer(text="Véronica Alpha 1.3")
                        embedVar.set_author(name=f"{ctx.author} VS. {user}")
                        embedVar.add_field(name=f"Selection of {ctx.author.name} :",value=f"{RPSintTOstr(BUTTONS.p1select)}", inline=True)
                        embedVar.add_field(name=f"Selection of {user} :",value=f"{RPSintTOstr(BUTTONS.p2select)}", inline=True)
                        if result==1:
                            embedVar.add_field(name=f"{ctx.author} WINS !!!",value=f"Bien essayé {user}, mais {ctx.author} a été meilleur pour le coup",inline=False)
                        elif result==2:
                            embedVar.add_field(name=f"{user} WINS !!!",value=f"Bien essayé {ctx.author}, mais {user} a été meilleur pour le coup",inline=False)
                        elif result==3:
                            embedVar.add_field(name=f"TIE !",value=f"Egalité ?! Il n'y a pas avoir un esprit aussi connecté..",inline=False)
                        await message.send(embed=embedVar)
                        await message.send(f"Le combat est terminé ! Ce thread sera automatiquement archivé d'ici une heure.\nJe vous invite donc à retourner discuter au moins dans le salon d'origine : <#{ctx.channel.id}>")
                        await ctx.send(f"Résultat de l'affrontement entre {ctx.author.mention} et {user.mention}",embed=embedVar)
                else:
                    await ctx.send(f"Votre adversaire a refusé votre invitation à la bagarre {ctx.author.mention}")
            
        else:
            await ctx.send("Vous ne pouvez pas vous affronter vous même !")

async def setup(bot):
    await bot.add_cog(RPS(bot))

# --- Boutons utilisés ---
class request(discord.ui.View):
    """Gestion des boutons pour la requête de 1v1"""
    def __init__(self,userid):
        super().__init__()
        self.value = bool
        self.userid=userid
    
    @discord.ui.button(label="Lez go! ✅",style=discord.ButtonStyle.green)
    async def check(self,interaction: discord.Interaction, confirm: discord.ui.Button):
        if interaction.user.id==self.userid: #Si l'utilisateur qui intéragis est bien celui qui est mentionné
            confirm.style=discord.ButtonStyle.blurple #Modifie la couleur du bouton
            confirm.disabled=True
            self.value=True
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop()
    
    @discord.ui.button(label="No ❌",style=discord.ButtonStyle.red)
    async def cross(self,interaction: discord.Interaction, cancel: discord.ui.Button):
        if interaction.user.id==self.userid: #Si l'utilisateur qui intéragis est bien celui qui est mentionné
            cancel.style=discord.ButtonStyle.red #Modifie la couleur du bouton
            cancel.disabled=True
            self.value=False
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop()

class rpsSOLO(discord.ui.View):
    """Gestion des boutons pour jouer au RPS"""
    def __init__(self,ctx):
        super().__init__()
        self.value = "temp"
        self.ctx=ctx
    
    @discord.ui.button(label='Rock 🪨', style=discord.ButtonStyle.grey)
    async def rock(self, interaction: discord.Interaction, rock_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            rock_button.style = discord.ButtonStyle.green
            rock_button.disabled=True
            self.value= 1 #Rock
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop()
    @discord.ui.button(label='Paper 🧻', style=discord.ButtonStyle.grey)
    async def paper(self, interaction: discord.Interaction, paper_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            paper_button.style = discord.ButtonStyle.green
            paper_button.disabled=True
            self.value= 2 #Paper
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop()
    @discord.ui.button(label='Scissors ✂️', style=discord.ButtonStyle.grey)
    async def scissors(self, interaction: discord.Interaction, scissors_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            scissors_button.style = discord.ButtonStyle.green
            scissors_button.disabled=True
            self.value= 3 #Scissors
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop()
    @discord.ui.button(label='Cancel ❌', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, cancel_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            cancel_button.style = discord.ButtonStyle.red
            self.value=False
            cancel_button.disabled=True
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop()

class rpsVersus(discord.ui.View):
    """Gestion des boutons pour un RPS en 1v1"""
    def __init__(self,ctx,user,message):
        super().__init__()
        self.value=True #A false si l'intéraction a été annulée
        self.p1select = None #Sélection du joueur 1
        self.p2select = None #Sélection du joueur 2
        self.ctx=ctx
        self.message=message
        self.p2id=user #On stock l'identifiant du joueur 2
    
    @discord.ui.button(label='Rock 🪨', style=discord.ButtonStyle.grey)
    async def rock(self, interaction: discord.Interaction, rock_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            if self.p1select==None: #Si l'utilisateur n'a pas déjà fait une sélection
                self.p1select= 1 #Rock
                await self.message.send(f"**{self.ctx.author}** a fait son choix !")
            else:
                await self.ctx.send(f"**{self.ctx.author}** vous avez déjà selectionné une option !")
        elif interaction.user.id==self.p2id.id: #Si c'est l'adversaire qui intéragis
            if self.p2select==None: #Si l'utilisateur n'a pas déjà fait une sélection
                self.p2select=1 #Rock
                await self.message.send(f"**{self.p2id}** a fait son choix !")
            else:
                await self.message.send(f"**{self.p2id}** vous avez déjà selectionné une option !")
        #Ne fait rien si aucun des cas est rempli. Cela veut dire que la personne qui a réagis n'a rien à voir avec ce duel
        if None not in [self.p1select,self.p2select]: #Si les 2 utilisateurs ont bien fait leur choix
            rock_button.style = discord.ButtonStyle.green
            rock_button.disabled=True
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop() #On arrête l'intéraction
    @discord.ui.button(label='Paper 🧻', style=discord.ButtonStyle.grey)
    async def paper(self, interaction: discord.Interaction, paper_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            if self.p1select==None: #Si l'utilisateur n'a pas déjà fait une sélection
                self.p1select= 2 #Paper
                await self.message.send(f"**{self.ctx.author}** a fait son choix !")
            else:
                await self.message.send(f"**{self.ctx.author}** vous avez déjà selectionné une option !")
        elif interaction.user.id==self.p2id.id: #Si c'est l'adversaire qui intéragis
            if self.p2select==None: #Si l'utilisateur n'a pas déjà fait une sélection
                self.p2select=2 #Paper
                await self.message.send(f"**{self.p2id}** a fait son choix !")
            else:
                await self.message.send(f"**{self.p2id}** vous avez déjà selectionné une option !")
        #Ne fait rien si aucun des cas est rempli. Cela veut dire que la personne qui a réagis n'a rien à voir avec ce duel
        if None not in [self.p1select,self.p2select]: #Si les 2 utilisateurs ont bien fait leur choix
            paper_button.style = discord.ButtonStyle.green
            paper_button.disabled=True
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop() #On arrête l'intéraction
    @discord.ui.button(label='Scissors ✂️', style=discord.ButtonStyle.grey)
    async def scissors(self, interaction: discord.Interaction, scissors_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            if self.p1select==None: #Si l'utilisateur n'a pas déjà fait une sélection
                self.p1select= 3 #Scissors
                await self.message.send(f"**{self.ctx.author}** a fait son choix !")
            else:
                await self.message.send(f"**{self.ctx.author}** vous avez déjà selectionné une option !")
        elif interaction.user.id==self.p2id.id: #Si c'est l'adversaire qui intéragis
            if self.p2select==None: #Si l'utilisateur n'a pas déjà fait une sélection
                self.p2select=3 #Scissors
                await self.message.send(f"**{self.p2id}** a fait son choix !")
            else:
                await self.message.send(f"**{self.p2id}** vous avez déjà selectionné une option !")
        #Ne fait rien si aucun des cas est rempli. Cela veut dire que la personne qui a réagis n'a rien à voir avec ce duel
        if None not in [self.p1select,self.p2select]: #Si les 2 utilisateurs ont bien fait leur choix
            scissors_button.style = discord.ButtonStyle.green
            scissors_button.disabled=True
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop() #On arrête l'intéraction
    @discord.ui.button(label='Cancel ❌', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, cancel_button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id or interaction.user.id==self.p2id.id: #Compare que l'utilisateur qui réagis est bien le même que celui qui a fait la commande d'origine
            cancel_button.style = discord.ButtonStyle.red
            self.value=False
            cancel_button.disabled=True
            await interaction.response.edit_message(view=self) #Actualise le bouton
            self.stop()