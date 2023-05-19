import discord
from discord.ext import commands

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        button.disabled=True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Canceling', ephemeral=True)
        self.value = False
        button.disabled=True
        self.stop()

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        from Version import	version
        self.version=version()
#TEST COMMAND
    @commands.hybrid_command(name="test",description="Commande de test pour le développeur du bot")
    async def test(self,ctx: commands.Context):
        if ctx.author.id==323147727779397632 or ctx.author.id==376321007583232002:
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author),icon_url=f"{ctx.author.avatar}")
            embedVar.add_field(name="Test",value="```test là``` Oui **c'**est un test du *formatage* Markdown au sein des `embed` Discord")
            await ctx.send(embed=embedVar)
        else:
            await ctx.reply("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

async def setup(bot):
    await bot.add_cog(Test(bot))