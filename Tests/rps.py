import discord
from discord.ext import commands
from discord import app_commands

from random import randint

class RPSbuttons(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = "temp"
    
    @discord.ui.button(label='Rock 🪨', style=discord.ButtonStyle.grey)
    async def rock(self, interaction: discord.Interaction, rock_button: discord.ui.Button):
        rock_button.style = discord.ButtonStyle.green
        rock_button.disabled=True
        self.value="Rock"
        await interaction.response.edit_message(view=self) #Actualise le bouton
        self.stop()
    @discord.ui.button(label='Paper 🧻', style=discord.ButtonStyle.grey)
    async def paper(self, interaction: discord.Interaction, paper_button: discord.ui.Button):
        paper_button.style = discord.ButtonStyle.green
        paper_button.disabled=True
        self.value="Paper"
        await interaction.response.edit_message(view=self) #Actualise le bouton
        self.stop()
    @discord.ui.button(label='Scissors ✂️', style=discord.ButtonStyle.grey)
    async def scissors(self, interaction: discord.Interaction, scissors_button: discord.ui.Button):
        scissors_button.style = discord.ButtonStyle.green
        scissors_button.disabled=True
        self.value="Scissors"
        await interaction.response.edit_message(view=self) #Actualise le bouton
        self.stop()
    @discord.ui.button(label='Cancel ❌', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, cancel_button: discord.ui.Button):
        cancel_button.style = discord.ButtonStyle.red
        self.value=False
        cancel_button.disabled=True
        await interaction.response.edit_message(view=self) #Actualise le bouton
        self.stop()

class Temp(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #TEST COMMAND
    @commands.hybrid_command(name="rps",description="Jouez à Pierre Feuille Ciseaux contre moi !")
    @app_commands.describe(user="Utilisateur à sélectionner")
    async def rps(self,ctx: commands.Context,user: discord.Member=None):
        if user==None or user.id==752958545758126082: #752958545758126082 est l'id de Véronica
            BOUTTONS=RPSbuttons()
            await ctx.reply("Choisissez une option :",view=BOUTTONS,ephemeral=True)
            await BOUTTONS.wait() #On attends que l'intéraction du bouton soit terminée avant d'executer la suite
            initiation=initiation_convertion(BOUTTONS.value) #réponse de l'utilisateur en int
            if initiation==4:
                await ctx.reply("Vous n'avez pas mis le bon argument !")
            else:
                embedVar = discord.Embed(color=discord.Color.blue())
                embedVar.set_footer(text="Véronica Alpha 1.3")
                embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
                embedVar.add_field(name="Vous avez choisi :",value="{}".format(str_rps(initiation)), inline=True)
                reply_rps=randint(1,3) #choix aléatoire de la réponse de Véronica
                embedVar.add_field(name="Véronica a choisi :",value="{}".format(str_rps(reply_rps)), inline=True)
                result=rps_win(initiation,reply_rps)
                if result == "Tie":
                    embedVar.add_field(name="Egalité !",value="{} Vs {}".format(str_rps(initiation),str_rps(reply_rps)), inline=False)
                elif result:
                    embedVar.add_field(name="J'ai gagné !",value="{} Vs **{}**".format(str_rps(initiation),str_rps(reply_rps)), inline=False)
                else:
                    embedVar.add_field(name="Félicitation ! Vous avez gagné !",value="**{}** Vs {}".format(str_rps(initiation),str_rps(reply_rps)), inline=False)
                await ctx.reply(embed=embedVar)
        else:
            await ctx.reply("Ouais le 1v1 là ouais")
        

async def setup(bot):
    await bot.add_cog(Temp(bot))


# ----- Définitions pour le RPS -----
def initiation_convertion(arg):
    """Détermine la réponse de l'utilisateur et la convertie en un nombre entier"""
    if "rock" in arg.lower() or "pierre" in arg.lower() or "🪨" in arg:
        return 1
    elif "paper" in arg.lower() or "sheet" in arg.lower() or "papier" in arg.lower() or "feuille" in arg.lower() or "🧻" in arg:
        return 2
    elif "scissors" in arg.lower() or "ciseaux" in arg.lower() or "✂️" in arg:
        return 3
    else:
        return 4

def str_rps(reply):
    if reply == 1:
        return "🪨Pierre"
    elif reply==2:
        return "🧻Papier"
    elif reply==3:
        return "️️️✂️Ciseaux"

def rps_win(init,reply):
    """Si 0 retourné, le joueur a gagné, si 1 retourné, Véronica a gagné, sinon c'est une égalité"""
    liste3=[1,2,3]
    for i in range(len(liste3)):
        if liste3[i]==init:
            if liste3[i-1]==reply: #condition de victoire
                return 0
            elif init==reply: #condition d'égalité
                return "Tie"
            else: #Aucune des autres conditions sont replies, donc condition de défaite
                return 1