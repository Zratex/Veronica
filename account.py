import discord
from discord.ext import commands
from discord import app_commands

#Importation des fonctions pour communiquer avec la base de donnée
from Database import database

class Graph(discord.ui.View):
    def __init__(self,ctx):
        super().__init__()
        self.value = None
        self.ctx=ctx

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
        embedVar.set_footer(text="Véronica Alpha 1.3")
        embedVar.set_author(name="Commande réalisée par {}".format(self.ctx.author), icon_url="{}".format(self.ctx.author.avatar))
        embedVar.add_field(name="Coquillettes<:coquillette:802972160364249119> Stock",value="Voici un graphique représentant le stock de Coquillettes<:coquillette:802972160364249119> dans la **Banque centrale**, en fonction du temps",inline=True)
        # Récupération du graphe de la banque
        database.ShowStockGraph()
        file = discord.File("MoneyStockGraph.png", filename="MoneyStockGraph.png")
        embedVar.set_image(url="attachment://MoneyStockGraph.png")
        await self.ctx.send(file=file,embed=embedVar)
    
    @discord.ui.button(label='Bourse du Conchiglie',style=discord.ButtonStyle.blurple,emoji='<:Conchiglie:1074283153658740737>')
    async def jetonVal(self,interaction: discord.Interaction, button: discord.ui.Button):
        button.style = discord.ButtonStyle.green
        self.value=True
        button.disabled=True
        self.stop()
        await interaction.response.edit_message(view=self)
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.3")
        embedVar.set_author(name="Commande réalisée par {}".format(self.ctx.author), icon_url="{}".format(self.ctx.author.avatar))
        embedVar.add_field(name="Conchiglie<:Conchiglie:1074283153658740737> Currency",value="Voici un graphique représentant le cours du Conchiglie<:Conchiglie:1074283153658740737> en fonction du temps",inline=True)
        # Récupération de l'affichage du graphe des jetons
        database.ShowJetonGraph()
        file = discord.File("graph_jeton.png", filename="graph_jeton.png")
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

class Account(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Profile
    @commands.hybrid_command(name="profile",description="Affiche le profile d'utilisateur",user="Utilasteur à afficher (ne rien mettre affiche VOTRE profile)")
    async def profile(self,ctx,user:discord.Member=None):
        """Affiche le profile d'un utilisateur"""
        if user!=None:
            identifiant=user.id
        else:
            identifiant=ctx.author.id
            user=ctx.author
        if database.UserExist(identifiant):
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text="Véronica Alpha 1.3")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
            embedVar.add_field(name="Id Discord de {}".format(user),value="{}".format(identifiant),inline=False)
            embedVar.add_field(name="Date de création du profile (date américaine)",value="{}".format(database.getCreationDate(identifiant)),inline=False)
            embedVar.add_field(name="<:coquillette:802972160364249119>en solde",value="{}".format(database.getUserMoney(identifiant)),inline=True)
            embedVar.add_field(name="<:Conchiglie:1074283153658740737> en stock",value="{}".format(database.getUserJeton(identifiant)),inline=True)
            embedVar.add_field(name="Lootbox <:lootbox:828330747416281128> dans l'inventaire",value="{}".format(database.getUserLootbox(identifiant)),inline=True)
            #Photo de profile de l'utilisateur sélectionnée
            embedVar.set_thumbnail(url="{}".format(user.avatar.url))
            # Essais d'afficher le rôle d'xp lié
            role = database.getSpecXPRole(database.getUserLvl(identifiant))
            print(role)
            try:
                role = discord.utils.get(ctx.guild.roles, name="{} - Lvl {}".format(role[1],role[0]))
                if role!=None:
                    embedVar.add_field(name="Rôle d'Xp",value="{}".format(role.mention), inline=False)
                else:
                    embedVar.add_field(name="Rôle d'Xp",value="Inexistant", inline=False)
            except Exception as E:
                embedVar.add_field(name="Rôle d'Xp",value="`{}`".format(E),inline=False)
            #Reste de tout ce qui est lié au module d'xp
            embedVar.add_field(name="Niveau",value="{}".format(database.getUserLvl(identifiant)),inline=True)
            embedVar.add_field(name="Xp actuelle",value="{}".format(database.getUserXP(identifiant)),inline=True)
            embedVar.add_field(name="Complémention du niveau {}".format(database.getUserLvl(identifiant)),value="{}%".format(round(database.getUserXPPourcentage(identifiant))),inline=False)
            
            # Récupération de l'affichage de la bare d'xp
            from Media import test
            test.test(database.getUserXPPourcentage(identifiant))
            file = discord.File("output.png", filename="output.png")
            embedVar.set_image(url="attachment://output.png")

            #réponse
            await ctx.reply(file=file,embed=embedVar)
        else:
            if identifiant==ctx.author.id:
                await ctx.send("Vous n'êtes pas inscrit dans la base de donnée ! Laissez moi vous créer un profile..")
            else:
                await ctx.send("{} n'a pas de profile ! Laissez moi lui en créer un...".format(user))
            try:   
                database.createUser(identifiant)
            except Exception as E:
                await ctx.send("Une erreure est survenue. Veuillez contacter Zratey de l'erreur. L'erreur en question : {E}")
            else:
                await ctx.send("Le compte a bel et bien été créer !")
    
    @commands.hybrid_command(name="daily",description="Récupération journalière de coquillettes")
    async def daily(self,ctx):
        """Récupération journalière de coquillettes"""
        if database.UserExist(ctx.author.id):
            import datetime
            today=datetime.datetime.now()
            today=today.strftime("%y-%m-%d %H:%M:%S")
            today=datetime.datetime.strptime(today,"%y-%m-%d %H:%M:%S")
            if database.DailyCooldownNone(ctx.author.id) or database.DayBetween(today,database.getDailyCooldown(ctx.author.id)) >= 1:
                await ctx.send("Vous avez reçu vos 150<:coquillette:802972160364249119> journalier. Votre solde s'élève à {}<:coquillette:802972160364249119>".format(database.dailyMoney(ctx.author.id)))
            else:
                await ctx.send("Vous avez déjà réclamer ce qu'il vous est dû ! Votre cooldown s'élève à `{}s`".format(database.getDailyCooldown(ctx.author.id)-today))
        else:
            await ctx.send("Vous n'avez pas de compte enregistré dans la base de donnée ? Faite la commande `/profile` pour l'initialiser.")
    
    @commands.hybrid_command(name="economy_graph",description="Affichage graphique économique au choix")
    async def economygraph(self,ctx):
        """Retourne l'affichage graphique du stock de coquillettes ou du cours des Conchiglie"""
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.3")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
        embedVar.add_field(name="Economy graph",value="Depuis ce menu, vous pouvez sélectionner l'affichage de graphiques. \n- :one: Stocks de **Coquilletes**<:coquillette:802972160364249119> dans la **Banque Centrale**\n- :two: Cours des **Conchiglies**<:Conchiglie:1074283153658740737>.")
        BUTTONS=Graph(ctx)
        await ctx.send(embed=embedVar,view=BUTTONS)
    
    @commands.hybrid_command(name="shop",description="Shop de Véronica !! :D")
    async def shop(self,ctx):
        """Retourne l'affichage graphique du shop du bot"""
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.3")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
        embedVar.add_field(name="Veronica's Shop",value="Bienvenue dans mon shop ! Ici vous pouvez acheter divers produit ou services que je peux vous fournir. Il vous suffit de clicker sur un des bouttons si dessous.",inline=True)
        embedVar.add_field(name="Information relative à votre compte en banque :",value="- <:coquillette:802972160364249119> en solde : {}\n- <:Conchiglie:1074283153658740737> en stock : {}".format(database.getUserMoney(ctx.author.id),database.getUserJeton(ctx.author.id)),inline=False)
        BUTTONS=ShopButtons(ctx)
        await ctx.send(embed=embedVar,view=BUTTONS)


async def setup(bot):
    await bot.add_cog(Account(bot))