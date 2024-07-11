import discord
from discord.ext import commands

#Importation des fonctions pour communiquer avec la base de donnée
from Database import database

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        from Version import version
        self.version=version()
    @commands.hybrid_command(name="shop",description="Shop de Véronica !! :D")
    async def shop(self,ctx):
        """Retourne l'affichage graphique du shop du bot"""
        if database.UserExist(ctx.author.id):
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
            embedVar.add_field(name="Veronica's Shop",value="Bienvenue dans mon shop ! Ici vous pouvez acheter divers produit ou services que je peux vous fournir. Il vous suffit de clicker sur un des bouttons si dessous.",inline=True)
            embedVar.add_field(name="Informations relatives à votre compte en banque :",
                            value=f"- <:coquillette:802972160364249119> en solde : {database.getUserMoney(ctx.author.id)}\n- <:Conchiglie:1074283153658740737> en stock : {database.getUserJeton(ctx.author.id)}\n- <:lootbox:828330747416281128> en inventaire : {database.getUserLootbox(ctx.author.id)}",
                            inline=False)
            embedVar.add_field(name="--- Items en vente ---",value="",inline=False)
            #On doit actualiser de nouveau le prix du jeton dans notre variable
            itemlist["<:Conchiglie:1074283153658740737> Conchiglie"]=database.getCoursJeton()
            #Ajout de tout les items en vente :
            for title in itemlist.keys():
                embedVar.add_field(name=f"{title}",value=f"{format_number_with_spaces(itemlist[title])}<:coquillette:802972160364249119>",inline=True)
            BUTTONS=ShopButtons(ctx=ctx)
            await ctx.send(embed=embedVar,view=BUTTONS)
        else:
            await ctx.send("Vous n'avez pas de compte ! Laissez moi vous en créer un...")
            try:   
                database.createUser(ctx.author.id)
            except Exception as E:
                await ctx.send("Une erreure est survenue. Veuillez contacter Zratey de l'erreur. L'erreur en question : {E}")
            else:
                await ctx.send("Le compte a bel et bien été créer !")

async def setup(bot):
    await bot.add_cog(Shop(bot))

# --- Liste des items à acheter ---
#Nom (et emoji qui va avec) de l'item en clé, sa valeur en coquillettes en value
itemlist={"<:lootbox:828330747416281128> Lootbox":5000,"<:Conchiglie:1074283153658740737> Conchiglie":database.getCoursJeton()}

def format_number_with_spaces(number:int)->str:
    """Ajoute des espaces à chaque miliers pour ce que ce soit + lisible.
    Donc l'entré est un entier mais la sortie une chaine de caractères."""
    number = list(str(number))
    number.reverse()
    temp=[]
    for i in range(len(number)):
        if i!=0 and not i%3:
            temp.append(" ")
        temp.append(number[i])
    temp.reverse()
    result=""
    for i in range(len(temp)):
        result+=temp[i]
    return result

# --- Boutons d'intéraction ---

class ShopButtons(discord.ui.View):
    #Boutons pour le shop
    def __init__(self,ctx):
        super().__init__()
        self.value = None
        self.ctx=ctx
    
    @discord.ui.button(label='Achat de Lootbox',style=discord.ButtonStyle.blurple,emoji='<:lootbox:828330747416281128>')
    async def lootbox(self,interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id:
            button.style=discord.ButtonStyle.green
            self.value=True
            button.disabled=True
            await interaction.response.edit_message(view=self) #On actualise l'affichage
            if database.getUserMoney(self.ctx.author.id)>=itemlist["<:lootbox:828330747416281128> Lootbox"]:
                #On retire l'argent de l'utilisateur
                database.setUserMoney(id=self.ctx.author.id,x=-(itemlist["<:lootbox:828330747416281128> Lootbox"]))
                #On l'ajoute dans la banque
                database.setBankStocks(itemlist["<:lootbox:828330747416281128> Lootbox"])
                #On donne à l'utilisateur sa lootbox
                database.setUserLootbox(id=self.ctx.author.id,x=1)
                await self.ctx.send("Vous venez de faire l'acquisition d'une **lootbox** ! Pour intéragir avec, effectuez la commande </lootbox:1108384275679694858>")
            else:
                await self.ctx.send("Vous n'avez pas assez d'argent pour acheter ceci")
        else:
            await self.ctx.send(f"{interaction.user.mention} c'est pas à vous de réagir ! Non mais oh, on s'est cru où là >:o")
        self.stop()
        
    
    @discord.ui.button(label='Achat de Conchiglie',style=discord.ButtonStyle.blurple,emoji='<:Conchiglie:1074283153658740737>')
    async def jeton(self,interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id:
            button.style=discord.ButtonStyle.green
            self.value=True
            button.disabled=True
            await interaction.response.edit_message(view=self) #On actualise l'affichage
            #On doit actualiser de nouveau le prix du jeton dans notre variable
            itemlist["<:Conchiglie:1074283153658740737> Conchiglie"]=database.getCoursJeton()
            if database.getUserMoney(self.ctx.author.id)>=itemlist["<:Conchiglie:1074283153658740737> Conchiglie"]:
                if database.getJetonCirculation()>=1:
                    #On retire l'argent de l'utilisateur
                    database.setUserMoney(id=self.ctx.author.id,x=-(itemlist["<:Conchiglie:1074283153658740737> Conchiglie"]))
                    #On l'ajoute dans la banque
                    database.setBankStocks(itemlist["<:Conchiglie:1074283153658740737> Conchiglie"])
                    #On donne à l'utilisateur son jeton
                    database.setUserJeton(id=self.ctx.author.id,x=1)
                    await self.ctx.send("Vous avez acquis un **Conchiglie**<:Conchiglie:1074283153658740737> !!")
                else:
                    await self.ctx.send("Il ne reste qu'un seul jeton en circulation ! Pour des raisons politiques (càd c'est moi qui l'ai décidé) et économiques, il ne peux vous être déservi.")
            else:
                await self.ctx.send("Vous n'avez pas assez d'argent pour acheter ceci")
        else:
            await self.ctx.send(f"{interaction.user.mention} c'est pas à vous de réagir ! Non mais oh, on s'est cru où là >:o")
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey,emoji='❌')
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        if interaction.user.id==self.ctx.author.id:
            button.style = discord.ButtonStyle.red
            self.value = False
            button.disabled=True
            await interaction.response.edit_message(view=self) #On actualise l'affichage
            await self.ctx.send("Interaction belle et bien annulée")
        else:
            await self.ctx.send(f"{interaction.user.mention} c'est pas à vous de réagir ! Non mais oh, on s'est cru où là >:o")
        self.stop()