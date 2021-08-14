import discord
from discord.ext import commands
from discord import User

def setup(bot):
    bot.add_cog(ModerationCommandes(bot))

class ModerationCommandes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def kick(self,ctx, user: User, arg):
        """Commande accessible seulement à la modération de BDN permettant de kick une personne"""
        role = discord.utils.get(ctx.guild.roles, name="Chefs cuisiniers 🍴")
        if role in ctx.author.roles:
            if role in user.roles:
                await ctx.send("Vous ne pouvez pas kick un membre de la modération !")
            else:
                await user.kick(reason=arg)
                leave = self.bot.get_channel(397334148710400000)
                await leave.channel.send("{} a été kick du serveur".format(user))
                await ctx.send("Raison du kick : {arg}")
        else:
            arg="Il/Elle voulait juste voir comment la commande de kick fonctionnait :D"
            mp = await ctx.author.create_dm()
            await mp.send("{}, Merci de ta contribution dans la 'science' ! Voici le lien pour revenir parce que je suis quand même une gentille fille : https://discord.gg/s6dGnVH ".format(ctx.author.mention))
            await ctx.author.kick(reason=arg)
            await ctx.channel.send("Vous n'avez normalement pas l'authorisation de kick quelqu'un. Donc je vous ait kick :) Au moins vous savez à quoi sert cette commande héhé")

    @commands.command()
    async def jail(self,ctx,user: User):
        """Permet de mettre ou faire ressortir quelqu'un de prison"""
        role = discord.utils.get(ctx.guild.roles, name="Chefs cuisiniers 🍴")
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