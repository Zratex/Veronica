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
#TEST COMMAND
    @commands.hybrid_command(name="test",description="Commande de test pour le développeur du bot")
    async def test(self,ctx: commands.Context):
        if ctx.author.id==323147727779397632 or ctx.author.id==376321007583232002:
            init_message = await ctx.send("Création du thread de test") #Message de création du thread
            thread = await init_message.create_thread(name="Thread test",auto_archive_duration=60,reason="Test thread creation") #Création du thread
            message = self.bot.get_channel(thread.id) #Acquisition de la capacité à écrire dans le thread
            await message.send("Message dans le thread là ouais")
            await message.send(f"<#{ctx.channel.id}>")
            #await thread.edit(archived=True) #Archive le channel
        else:
            await ctx.reply("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

async def setup(bot):
    await bot.add_cog(Test(bot))