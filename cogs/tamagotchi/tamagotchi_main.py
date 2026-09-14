from discord.ext import commands
#Importation des fonctions nécessaires au bout fonctionnement du Tamagotchi.
from .db_tamagotchi import *  #Le . devant le nom de la fonction est pour indiquer que l'importation se fait dans le dossier locale

class tamagotchi_main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.hybrid_command(name="tamagotchi",description="Gérez votre tamagotchi")
    async def tamagotchi(self,ctx: commands.Context):
        if count_user_tamagotchis(self.bot.pool,ctx.author.id) > 0:
            await ctx.send("Tamagotchi à créer")
        else:
            await ctx.send("(à développer)")

async def setup(bot):
    await bot.add_cog(tamagotchi_main(bot))