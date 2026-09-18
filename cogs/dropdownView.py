from discord.ui import Select, View
from discord import SelectOption, Interaction

class Dropdown(Select):
    def __init__(self,optionList: list[dict],placeHolderTitle: str="Veuillez sélectionner une des options présentée..."):
        """Structure de optionList :
        [{label: "", description: "", emoji: "",value=""},{label: "", description: "", emoji: "",value=""},...]
        """
        options = []
        for elt in optionList:
            if elt["value"]=="":
                elt["value"]=None
            options.append(SelectOption(label=elt["label"], description=elt["description"], emoji=elt["emoji"], value=elt["value"]))
        
        super().__init__(placeholder="{}".format(placeHolderTitle), min_values=1, max_values=1, options=options)

    async def callback(self, interaction: Interaction):
        self.view.result = self.values[0] # Stockage du résultat dans la vue parente
        
        # Ces lignes sont obligatoires :
        await interaction.response.defer()
        self.view.stop()


class DropdownView(View):
    def __init__(self,optionList: list[dict],placeHolderTitle: str=None):
        """Structure de optionList :
        [{label: "", description: "", emoji: ""},{label: "", description: "", emoji: "", value=""},...]
        """
        super().__init__()
        self.result = None
        self.add_item(Dropdown(optionList,placeHolderTitle))