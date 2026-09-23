from discord import Button, ButtonStyle, Interaction
from discord.ui import View, button


class selectInteractionWithTamagotchiView(View):
    def __init__(self):
        super().__init__()
        self.value = None
    @button(label='Nourrir', style=ButtonStyle.green)
    async def feed(self, interaction: Interaction, button: Button):
        await interaction.response.send_message('Sustentation en cours...', ephemeral=True)
        self.value = True
        self.stop()

    @button(label='Jouer', style=ButtonStyle.blurple)
    async def play(self, interaction: Interaction, button: Button):
        await interaction.response.send_message('Acquisition du fun en cours...', ephemeral=True)
        self.value = False
        self.stop()