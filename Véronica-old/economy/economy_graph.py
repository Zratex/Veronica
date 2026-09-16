import discord
from discord.ext import commands
import os

#Importation des fonctions pour communiquer avec la base de donnée
from Database import database

class EcoGraph(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        from Version import version
        self.version=version()
    
    @commands.hybrid_command(name="economy_graph",description="Affichage graphique économique au choix")
    async def economygraph(self,ctx):
        """Retourne l'affichage graphique du stock de coquillettes ou du cours des Conchiglie"""
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
        embedVar.add_field(name="Economy graph",value="Depuis ce menu, vous pouvez sélectionner l'affichage de graphiques. \n- :one: Stocks de **Coquilletes**<:coquillette:802972160364249119> dans la **Banque Centrale**\n- :two: Stocks de **Conchiglies**<:Conchiglie:1074283153658740737> libre\n- :three: Cours en bourse des **Conchiglies**<:Conchiglie:1074283153658740737>")
        BUTTONS=Graph(ctx=ctx,bot=self.bot)
        await ctx.send(embed=embedVar,view=BUTTONS)

    @commands.hybrid_command(name="economy_refresh",description="Force l'actualisation du cours de la banque")
    async def economy_refresh(self,ctx):
        """Force l'actualisation du cours de la banque"""
        database.setBankStocks()
        database.setJetonStock()
        await ctx.send("Stock de la banque correctement actualisé ! Constatez par vous même le résultat avec la commande </economy_graph:1108400200923488386>")
async def setup(bot):
    await bot.add_cog(EcoGraph(bot))

# --- Boutons d'intéraction ---

class Graph(discord.ui.View):
    def __init__(self,ctx,bot):
        super().__init__()
        self.value = None
        self.ctx=ctx
        self.bot=bot
        from Version import version
        self.version=version()

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Stocks de la banque', style=discord.ButtonStyle.blurple,emoji='<:coquillette:802972160364249119>')
    async def bankStocks(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.style = discord.ButtonStyle.green
        self.value = True
        button.disabled=True
        self.stop()
        await interaction.response.edit_message(view=self)
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
        embedVar.set_author(name="Commande réalisée par {}".format(self.ctx.author), icon_url="{}".format(self.ctx.author.avatar))
        embedVar.add_field(name="Coquillettes<:coquillette:802972160364249119> Stock",value="Voici un graphique représentant le stock de Coquillettes<:coquillette:802972160364249119> dans la **Banque centrale**, en fonction du temps",inline=True)
        # Récupération du graphe de la banque
        database.ShowStockGraph()

        import os
        # Chemin relatif de la sortie souhaitée
        output_path = '../economy/MoneyStockGraph.png'
        # Obtenir le chemin absolu du répertoire courant
        current_dir = os.path.abspath(os.path.dirname(__file__))
        # Combiner les chemins pour obtenir le chemin absolu de la sortie souhaitée
        file_full_path = os.path.join(current_dir, output_path)
        # Créer le graphique et enregistrer la sortie au chemin absolu
        file = discord.File(file_full_path, filename="MoneyStockGraph.png")
        embedVar.set_image(url="attachment://MoneyStockGraph.png")
        await self.ctx.send(file=file,embed=embedVar)
    
    @discord.ui.button(label='Stocks du Conchiglie',style=discord.ButtonStyle.blurple,emoji='<:Conchiglie:1074283153658740737>')
    async def jetonStock(self,interaction: discord.Interaction, button: discord.ui.Button):
        button.style = discord.ButtonStyle.green
        self.value=True
        button.disabled=True
        self.stop()
        await interaction.response.edit_message(view=self)
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
        embedVar.set_author(name="Commande réalisée par {}".format(self.ctx.author), icon_url="{}".format(self.ctx.author.avatar))
        embedVar.add_field(name="Conchiglie<:Conchiglie:1074283153658740737> Stocks",value="Voici un graphique représentant le nombre de Conchiglie<:Conchiglie:1074283153658740737> encore achetable",inline=True)
        # Récupération de l'affichage du graphe des jetons
        database.ShowJetonStockGraph()
        # Chemin relatif de la sortie souhaitée
        output_path = '../economy/graph_jetonstock.png'
        # Obtenir le chemin absolu du répertoire courant
        current_dir = os.path.abspath(os.path.dirname(__file__))
        # Combiner les chemins pour obtenir le chemin absolu de la sortie souhaitée
        file_full_path = os.path.join(current_dir, output_path)
        # Créer le graphique et enregistrer la sortie au chemin absolu
        file = discord.File(file_full_path, filename="graph_jetonstock.png")
        embedVar.set_image(url="attachment://graph_jetonstock.png")
        await self.ctx.send(file=file,embed=embedVar)
    
    @discord.ui.button(label='Bourse de Conchiglie',style=discord.ButtonStyle.blurple,emoji='<:Conchiglie:1074283153658740737>')
    async def jetonVal(self,interaction: discord.Interaction, button: discord.ui.Button):
        button.style = discord.ButtonStyle.green
        self.value=True
        button.disabled=True
        self.stop()
        await interaction.response.edit_message(view=self)
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
        embedVar.set_author(name="Commande réalisée par {}".format(self.ctx.author), icon_url="{}".format(self.ctx.author.avatar))
        embedVar.add_field(name="Conchiglie<:Conchiglie:1074283153658740737> Currency",value="Voici un graphique représentant le cours du Conchiglie<:Conchiglie:1074283153658740737> en fonction du temps",inline=True)
        # Récupération de l'affichage du graphe des jetons
        database.ShowJetonGraph()
        # Chemin relatif de la sortie souhaitée
        output_path = '../economy/graph_jeton.png'
        # Obtenir le chemin absolu du répertoire courant
        current_dir = os.path.abspath(os.path.dirname(__file__))
        # Combiner les chemins pour obtenir le chemin absolu de la sortie souhaitée
        file_full_path = os.path.join(current_dir, output_path)
        # Créer le graphique et enregistrer la sortie au chemin absolu
        file = discord.File(file_full_path, filename="graph_jeton.png")
        embedVar.set_image(url="attachment://graph_jeton.png")
        await self.ctx.send(file=file,embed=embedVar)
        

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey,emoji='❌')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.style = discord.ButtonStyle.red
        await interaction.response.send_message('Interaction Belle et bien intérompue', ephemeral=True)
        self.value = False
        button.disabled=True
        self.stop()