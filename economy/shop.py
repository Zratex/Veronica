import discord
from discord.ext import commands

#Importation des fonctions pour communiquer avec la base de donnée
from Database import database

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name="shop",description="Shop de Véronica !! :D")
    async def shop(self,ctx):
        """Retourne l'affichage graphique du shop du bot"""
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.3")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
        embedVar.add_field(name="Veronica's Shop",value="Bienvenue dans mon shop ! Ici vous pouvez acheter divers produit ou services que je peux vous fournir. Il vous suffit de clicker sur un des bouttons si dessous.",inline=True)
        embedVar.add_field(name="Informations relatives à votre compte en banque :",
                           value=f"- <:coquillette:802972160364249119> en solde : {database.getUserMoney(ctx.author.id)}\n- <:Conchiglie:1074283153658740737> en stock : {database.getUserJeton(ctx.author.id)}\n- <:lootbox:828330747416281128> en inventaire : {database.getUserLootbox(ctx.author.id)}",
                           inline=False)
        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(Shop(bot))

# --- Boutons d'intéraction ---

class ShopButtons(discord.ui.View):
    #Bouttons pour le shop
    def __init__(self,ctx):
        super().__init__()
        self.value = None
        self.ctx=ctx
    
    @discord.ui.button(label='Achat de Lootbox',style=discord.ButtonStyle.blurple,emoji='<:lootbox:828330747416281128>')
    async def lootbox(self,interaction: discord.Interaction, button: discord.ui.Button):
        button.style=discord.ButtonStyle.green
        await interaction.response.send_message("Still working on it lol",ephemeral=True)
        self.value=True
        button.disabled=True
        self.stop()
    
    @discord.ui.button(label='Achat de Conchiglie',style=discord.ButtonStyle.blurple,emoji='<:Conchiglie:1074283153658740737>')
    async def jeton(self,interaction: discord.Interaction, button: discord.ui.Button):
        button.style=discord.ButtonStyle.green
        await interaction.response.send_message("Still working on it lol",ephemeral=True)
        self.value=True
        button.disabled=True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey,emoji='❌')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.style = discord.ButtonStyle.red
        await interaction.response.send_message('Interaction Belle et bien intérompue', ephemeral=True)
        self.value = False
        button.disabled=True
        self.stop()
