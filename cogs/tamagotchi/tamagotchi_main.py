from discord.ext import commands
#Importation des fonctions nécessaires au bout fonctionnement du Tamagotchi.
from .db_tamagotchi import *  #Le . devant le nom de la fonction est pour indiquer que l'importation se fait dans le dossier locale
from ..confirmationView import confirmationView
from ..embedInit import embedInit

class tamagotchi_main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if self.bot.poolConnected == False:
            raise Exception("La connexion à la base de donnée a échouée lors de l'initialisation du bot. Par conséquent ce module ne peut être chargé")
    
    @commands.hybrid_command(name="tamagotchis",description="Liste des tamagotchis en votre possession")
    async def tamagotchis(self,ctx: commands.Context):
        tamasList = await get_tamagotchis_ids_by_user(self.bot.pool,ctx.author.id)
        if len(tamasList) == 0:
            await ctx.send("Vous n'avez aucun Tamagochi en votre possession. Veuillez vous en acheter un !", ephemeral=True)
        else:
            for i in range(tamasList):
                embed = embedInit(ctx.author,self.bot)
                embed.add_field(name="# {}".format(tamasList[i]),value="Tamagochi appartenant à {}".format(ctx.author.name), inline=False)
                await ctx.send(embed=embed)

    @commands.hybrid_command(name="buy-tamagotchi",description="Achat d'un nouveau tamagotchi")
    async def buyTamagotchi(self,ctx: commands.Context, name: str):
        # Vérification que l'utilisateur a assez d'argent
        usermoney = await get_user_money(self.bot.pool,ctx.author.id)
        tamaPrice = await get_base_price_to_buy_tamagotchi(self.bot.pool)
        if usermoney < tamaPrice:
            await ctx.send("Vous n'avez pas assez pour acheter un tamagotchi. Votre solde : {}<:coquillette:802972160364249119> ; Prix d'un tamagotchi : {}<:coquillette:802972160364249119>".format(usermoney,tamaPrice),
                           ephemeral=True)
        else:
            # Module demande achat
            CONFIRMATION=confirmationView()
            await ctx.send("Souhaitez vous acheter un tamagotchi ? Votre solde : {}<:coquillette:802972160364249119> ; Prix d'un tamagotchi : {}<:coquillette:802972160364249119>".format(usermoney,tamaPrice),
                           view=CONFIRMATION)
            await CONFIRMATION.wait()
            if not CONFIRMATION.value:
                await ctx.send("Votre achat a été annulé")
            else:
                await ctx.send("Achat du tamagotchi en cours...",ephemeral=True)
                await update_money(self.bot.pool,ctx.author.id,-tamaPrice)
                await create_tamagotchi(self.bot.pool,ctx.author.id,name)
                await ctx.send("Votre tamagotchi a été créé !")

async def setup(bot):
    await bot.add_cog(tamagotchi_main(bot))