from discord.ext import commands

class tamagoshi_main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #TEST COMMAND
    @commands.hybrid_command(name="tamagochi",description="Gérez votre tamagoshi")
    async def tamagochi(self,ctx: commands.Context):
        await ctx.send("(à développer)")

async def setup(bot):
    await bot.add_cog(tamagoshi_main(bot))