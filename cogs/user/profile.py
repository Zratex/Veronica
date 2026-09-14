from discord.ext import commands
from discord import Member
from ..tamagochi import db_tamagochi

class profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #TEST COMMAND
    @commands.hybrid_command(name="profile",description="Récupérez les informations sur vous même ou un autre utilisateur")
    async def profile(self,ctx: commands.Context, user: Member=None):
        if user!=None:
            userid=user.id 
        else:
            userid = ctx.author.id
        await ctx.send(f"Retour DB : {db_tamagochi.get_or_create_user(self.bot.pool,userid)}")

async def setup(bot):
    await bot.add_cog(profile(bot))