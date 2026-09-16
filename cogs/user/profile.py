from discord.ext import commands
from discord import Member
from ..tamagotchi import db_tamagotchi

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        """# Commentaire à retirer
        if self.bot.poolConnected == False:
            raise Exception("La connexion à la base de donnée a échouée lors de l'initialisation du bot. Par conséquent ce module ne peut être chargé")
        """
    
    #TEST COMMAND
    @commands.hybrid_command(name="profile",description="Récupérez les informations sur vous même ou un autre utilisateur")
    async def profile(self,ctx: commands.Context, user: Member=None):
        if user!=None:
            userid=user.id 
        else:
            userid = ctx.author.id
        """#Commentaire temporaire :
        result = await db_tamagotchi.get_or_create_user(self.bot.pool,userid)
        await ctx.send(f"Retour DB : {result}")
        """
        await ctx.send("a") #A retirer, et retirer le commentaire
        await ctx.send(f"`Véronica {self.bot.version}`")

async def setup(bot):
    await bot.add_cog(profile(bot))