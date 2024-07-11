from typing import Any, List, Optional
import discord
from discord.components import SelectOption
from discord.ext import commands
from discord.interactions import Interaction
from discord.utils import MISSING

class Vote(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        from Version import	version
        self.version=version()
    
    @commands.hybrid_command(name="resultats",description="Permet de voir les résultat courant des élections")
    async def resultats(self,ctx: commands.Context):
        if ctx.author.id==323147727779397632:
            embedVar=discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author),icon_url=f"{ctx.author.avatar}")
            import json
            with open("vote_municipales.json") as f:
                temp = json.load(f)
            from collections import defaultdict
            compteur_votes = defaultdict(int)
            for candidat in temp["votes"].values():
                compteur_votes[candidat] += 1
            for candidat, votes in compteur_votes.items():
                result_municipales=f"Nombre de votes pour **{candidat}** : {votes}\n"
            embedVar.add_field(name="Resultats courant des élections municipales",
                            value=f"{result_municipales}")
            await ctx.send(embed=embedVar)

    @commands.hybrid_command(name="vote",description="Permet de voter pour une élection à propos du serveur Minecraft")
    async def vote(self,ctx: commands.Context):
        if Inscrit(str(ctx.author.id)): #Si l'utilsateur est recensé:
            embedVar=discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text=self.version,icon_url=f"{self.bot.user.avatar}")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author),icon_url=f"{ctx.author.avatar}")
            embedVar.add_field(name="Votes municipales",value="Via l'interface de Véronica, nous allons effectuer le vote ! Il vous suffit d'appuyer sur le bouton correspondant au candidat pour qui vous voulez voter.",inline=False)
            import json
            with open("vote_municipales.json") as f:
                temp = json.load(f)
            liste=""
            for candidat in temp["candidats"]:
                liste+=f"- {candidat}\n"
            embedVar.add_field(name="Liste électorale",value=f"{liste}",inline=False)
            BUTTONS=Select(ctx=ctx)
            await ctx.send(embed=embedVar,view=BUTTONS)
        else:
            await ctx.send("Vous n'êtes pas recensé(e) ! Contactez l'administrateur à propos de ça")

async def setup(bot):
    await bot.add_cog(Vote(bot))

def Inscrit(userid):
    """Vérifie si l'utilsateur est dans la liste des personnes rencensés. L'id entré doit être en string"""
    import json
    with open("vote_municipales.json") as f:
        temp=json.load(f)
    if userid in temp["Recenses"]:
        return True
    else:
        return False

class Select(discord.ui.View):
    def __init__(self,ctx):
        super().__init__()
        self.ctx=ctx
        import json
        with open("vote_municipales.json") as f:
            temp = json.load(f)
        self.listeMunicipale=temp["candidats"]
        self.add_item(MunicipalesDropdown(self.ctx,self.listeMunicipale))

class MunicipalesDropdown(discord.ui.Select):
    def __init__(self,ctx,listeMunicipale):
        self.ctx=ctx
        options=[]
        self.listeMunicipale=listeMunicipale
        for candidat in self.listeMunicipale: #Pour chaque candidat :
            options.append(discord.SelectOption(label=f'{candidat}',description=f"Votez pour {candidat}"))
            super().__init__(placeholder='Candidat à voter', min_values=1, max_values=1, options=options)
    async def callback(self,interaction: discord.Interaction):
        #On réimporte le fichier json dans le cas qu'il y ait eut une modification du fichier entre temps
        if interaction.user.id==self.ctx.author.id:
            import json
            with open("vote_municipales.json") as f:
                temp = json.load(f)
            if temp["Elections"]: #Si les élections sont ouvertes
                CONFIRM=Confirm()
                if str(self.ctx.author.id) in temp["votes"]:
                    indication="Vous avez déjà pour `{}`".format(temp["votes"][str(self.ctx.author.id)])
                else:
                    indication=""
                await interaction.response.send_message(f"Êtes vous sur de vouloir voter pour `{self.values[0]}` ? {indication}",view=CONFIRM,ephemeral=True)
                await CONFIRM.wait()
                if CONFIRM.value: #Si le choix est confirmé:
                    temp["votes"].update({str(self.ctx.author.id): self.values[0]})
                    with open("vote_municipales.json","w") as f:
                        json.dump(temp,f,indent=3)
                    await self.ctx.send(f"Votre vote a été pris en compte !",ephemeral=True)
                else:
                    await self.ctx.send("Votre vote n'a pas été pris en compte.",ephemeral=True)
            else:
                await interaction.response.send_message("Aucune élections en cours",ephemeral=True)
        else:
            await interaction.response.send_message("{} pour des raisons algorithmique, vous ne pouvez pas répondre à la commande invoqué par {}".format(interaction.user.mention,self.ctx.author))

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    
    @discord.ui.button(label='Oui',style=discord.ButtonStyle.green)
    async def confirm(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Traitement de votre sélection...",ephemeral=True)
        self.value=True
        button.disabled=True
        self.stop()
    @discord.ui.button(label='Non',style=discord.ButtonStyle.red)
    async def cancel(self,interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("Anulation de votre sélection...",ephemeral=True)
        self.value=False
        button.disabled=True
        self.stop()