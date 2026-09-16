import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #MP
    @commands.hybrid_command(name="mp",description="Permet d'envoyer un MP à quelqu'un")
    @app_commands.describe(content="Contenu du message à envoyer")
    async def mp(self,ctx: commands.Context, member: discord.Member,content: str):
        if ctx.author.id == 323147727779397632: #Check if it's Zratey
            channel = await member.create_dm()
            await channel.send(content)
            await ctx.send("Le message a bien été envoyé")
        else:
            await ctx.send("Non !")
            await ctx.send("<:veropillow:909029139682562108><:veropillow2:909029164240232468>")
    
    #JAIL
    @commands.hybrid_command(name="jail",description="Met/retire quelqu'un de la jail")
    async def jail(self,ctx,user: discord.Member):
        """Permet de mettre ou faire ressortir quelqu'un de prison"""
        role = discord.utils.get(ctx.guild.roles, name="Cuisiniers🍴")
        if role in ctx.author.roles:
            if role in user.roles:
                await ctx.send("Vous ne pouvez pas mettre un membre de la modération en prison !")
            else:
                jail = discord.utils.get(ctx.guild.roles, name="Jail")
                fan_de_nouilles = discord.utils.get(ctx.guild.roles, name="Fan de nouilles 🍜")
                if fan_de_nouilles in user.roles:
                    await user.add_roles(jail)
                    await user.remove_roles(fan_de_nouilles)
                    await ctx.send("{} est désormais en prison !".format(user))
                elif jail in user.roles:
                    await user.add_roles(fan_de_nouilles)
                    await user.remove_roles(jail)
                    await ctx.send("{} est sorti de prison !".format(user))
        else:
            await ctx.send("Vous n'avez pas la permission pour executer cette commande")

async def setup(bot):
    await bot.add_cog(Moderation(bot))