from discord.ui import View, Button, button
from discord import Interaction, ButtonStyle

class confirmationView(View):
    """Factorisation des boutons de confirmation ou annulation
    self.value = True lors que c'est confirmé, False sinon
    -> A None tant que pas de réponse"""
    def __init__(self):
        super().__init__()
        self.value = None
    @button(label='Confirm', style=ButtonStyle.green)
    async def confirm(self, interaction: Interaction, button: Button):
        await interaction.response.send_message('Confirmation en cours...', ephemeral=True)
        self.value = True
        self.stop()

    @button(label='Cancel', style=ButtonStyle.red)
    async def cancel(self, interaction: Interaction, button: Button):
        await interaction.response.send_message('Annulation en cours...', ephemeral=True)
        self.value = False
        self.stop()