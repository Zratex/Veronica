from discord.ext import commands
from discord import Member, Embed, Color
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
        if user==None:
            user = ctx.author
        result = await db_tamagotchi.get_or_create_user(self.bot.pool,user.id)
        embedVar = Embed(color=Color.blue())
        embedVar.set_footer(text=self.bot.version,icon_url=f"{self.bot.user.avatar}")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
        # Affichage du profile de l'utilisateur
        for key, value in result.items():
            if key == "id":
                embedVar.add_field(name="Id Discord :",value="`{}`".format(value), inline=True)
                embedVar.add_field(name="Pseudo du serveur :",value="{}".format(user.name), inline=True)
                embedVar.add_field(name="Pseudo global :",value="{}".format(user.global_name), inline=True)
            elif key == "A EDITER":
                embedVar.add_field(name="Coquillettes :",value="{} <:coquillette:802972160364249119>".format(value), inline=False)
            else:
                embedVar.add_field(name="{}".format(key),value="{}".format(value), inline=False)
        await ctx.send(embed=embedVar)

async def setup(bot):
    await bot.add_cog(profile(bot))