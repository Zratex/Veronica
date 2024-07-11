import discord
from discord.ext import commands

#Importation des fonctions pour communiquer avec la base de donnée
from Database import database

class Lootbox(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        from Version import	version
        self.version=version()
        
    #Lootbox inventory
    @commands.hybrid_command(name="lootbox",description="Retourne l'affichage des actions avec les lootboxs")
    async def lootbox(self,ctx: commands.Context):
        """Retourne l'affichage des actions avec les lootboxs"""
        if database.UserExist(ctx.author.id):
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
            embedVar.set_author(name="Inventaire de Lootboxs de {}".format(ctx.author),icon_url=f"{ctx.author.avatar}")
            embedVar.add_field(name="Informations sur l'ouverture de lootbox :",value="```Ce que l'on peut gagner```\nIl y aura 2 tirages différents mais qui seront fait en simultanés sans influencer sur l'autre :\n- Une certaine quantité de <:coquillette:802972160364249119>\n- Des récompenses diverses et variées\nLe contenu des récompenses, ainsi que la répartition des pourcentages de chance de gain sont indiqués dans la documentation.\n```Comment ouvrir une lootbox```\nIl vous faut au moins :\n- 1 <:lootbox:828330747416281128>Lootbox\n- 1 <:Conchiglie:1074283153658740737>Conchiglie\nPour en obtenir, il faut les acheter dans le shop, avec la commande </shop:1108685477529260042>",inline=False)
            embedVar.add_field(name="Ce que vous avez dans votre inventaire :",value="",inline=False)
            embedVar.add_field(name="<:lootbox:828330747416281128> dans votre inventaire",value=f"{database.getUserLootbox(ctx.author.id)}",inline=True)
            embedVar.add_field(name="<:Conchiglie:1074283153658740737> dans votre inventaire",value=f"{database.getUserJeton(ctx.author.id)}",inline=True)
            BUTTONS=LootboxButtons(ctx=ctx)
            await ctx.send(embed=embedVar,view=BUTTONS)
            await BUTTONS.wait()
            if BUTTONS.transaction: #Si la transaction a été réalisée
                embedVar = discord.Embed(color=discord.Color.blue())
                embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
                embedVar.set_author(name="Résultat d'ouverture de lootbox, par {}".format(ctx.author),icon_url=f"{ctx.author.avatar}")
                #Execution du premier gain
                embedVar.add_field(name="Premier gain",value=f"{firstDraw(ctx.author.id)}",inline=False)
                embedVar.add_field(name="Second gain",value=f"Pas encore développé",inline=True)
                await ctx.send(f"Regarde ce que tu viens de gagner {ctx.author.mention} !",embed=embedVar)
        else:
            await ctx.send("Vous n'êtes pas inscrit dans la base de donnée ! Laissez moi vous créer un profile..")
            try:
                database.createUser(ctx.author.id)
            except Exception as E:
                await ctx.send("Une erreure est survenue. Veuillez contacter Zratey de l'erreur. L'erreur en question : {E}")
            else:
                await ctx.send("Votre compte a bel et bien été créer !")
                await ctx.send("Comme votre compte est nouveau, ça m'étonnerait que vous puissiez faire une action avec les lootboxs..")

async def setup(bot):
    await bot.add_cog(Lootbox(bot))

# --- Bouttons d'intéraction ---
class LootboxButtons(discord.ui.View):
    #Boutons pour les intéractions de l'inventaire en rapport avec les lootbox
    def __init__(self,ctx):
        super().__init__()
        self.value=None
        self.ctx=ctx
        self.transaction=False #Indique si la transaction a été réalisée ou non
    
    @discord.ui.button(label="Ouvrir une lootbox",style=discord.ButtonStyle.blurple,emoji='<:lootbox:828330747416281128>')
    async def lootbox(self,interaction:discord.Interaction,button:discord.ui.Button):
        if interaction.user.id == self.ctx.author.id:
            if database.getUserLootbox(self.ctx.author.id)>=1:
                if database.getUserJeton(self.ctx.author.id)>=1:
                    button.style=discord.ButtonStyle.green
                    #Consommation de l'inventaire :
                    database.setUserJeton(id=self.ctx.author.id,x=-1) #On retire 3 jetons à l'utilisateur
                    database.setUserLootbox(id=self.ctx.author.id,x=-1) #On retire 1 lootbox à l'utilisateur
                    self.transaction=True
                else:
                    button.style=discord.ButtonStyle.red
                    await self.ctx.send("Vous n'avez pas assez de Conchiglie<:Conchiglie:1074283153658740737> pour ouvrir une lootbox. Il vous en faut minimum `1`")
            else:
                button.style=discord.ButtonStyle.red
                await self.ctx.send(f"Mais {self.ctx.author.mention}, comment tu veux sérieusement ouvrir une lootbox..Si t'en a pas ??")
            self.value=False
            button.disabled=True
            await interaction.response.edit_message(view=self) #On actualise l'affichage
            self.stop()
            await interaction.followup.edit_message(message_id=interaction.message.id,view=self)

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey,emoji='❌')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id == self.ctx.author.id:
            button.style = discord.ButtonStyle.red
            self.value = False
            button.disabled=True
            await interaction.response.edit_message(view=self) #On actualise l'affichage
            await self.ctx.send('Interaction belle et bien intérompue', ephemeral=True)
            self.stop()

# --- FONCTIONS ---
# --- DEFINISSANT ---
# --- LES GAINS ---
# --- DES LOOTBOXS ---

# --- TIRAGE 1 : coquillettes ---
def firstDraw(userID:int):
    """Sélectionne aléatoirement un événement remportant de l'argent à l'utilisateur
    Retourne la valeur remportée par l'utilisateur en string"""
    from random import randint
    draw=randint(1,100)
    if 1<=draw<=35: #35% de chance
        database.setUserMoney(id=userID,x=1000)
        return "1 000"
    elif 35<draw<=65: #30% de chance
        database.setUserMoney(id=userID,x=5000)
        return "5 000"
    elif 65<draw<=80: #15% de chance
        database.setUserMoney(id=userID,x=10000)
        return "10 000"
    elif 80<draw<=90: #10% de chance
        database.setUserMoney(id=userID,x=20000)
        return "20 000"
    elif 90<draw<=95: #5% de chance
        database.setUserMoney(id=userID,x=30000)
        return "30 000"
    elif 95<draw<=99:
        database.setUserMoney(id=userID,x=50000)
        return "50 000"
    elif draw==100:
        database.setUserMoney(id=userID,x=100000)
        return "100 000"