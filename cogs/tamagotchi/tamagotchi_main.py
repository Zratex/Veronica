from discord.ext import commands
#Importation des fonctions nécessaires au bout fonctionnement du Tamagotchi.
from .db_tamagotchi import *  #Le . devant le nom de la fonction est pour indiquer que l'importation se fait dans le dossier locale

class tamagotchi_main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        if self.bot.poolConnected == False:
            raise Exception("La connexion à la base de donnée a échouée lors de l'initialisation du bot. Par conséquent ce module ne peut être chargé")
    
    @commands.hybrid_command(name="tamagotchis",description="Liste des tamagotchis")
    async def tamagotchis(self,ctx: commands.Context):
        nbTamas = await count_user_tamagotchis(self.bot.pool,ctx.author.id)
        if nbTamas == 0:
            await ctx.send("Tamagotchi à créer")
        else:
            await ctx.send("(à développer)")

async def setup(bot):
    await bot.add_cog(tamagotchi_main(bot))