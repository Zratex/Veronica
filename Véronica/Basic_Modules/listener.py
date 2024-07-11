import discord
from discord.ext import commands
from discord import app_commands

class on_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == 752958545758126082:
            return #On veux pas que le bot se réponde à lui même
        else:
            #Réaction coucou
            slt=["bonjour","coucou","bonsoir","bvn","slt","salut","hello"]
            cc=0
            for elt in slt:
                if elt in message.content.lower():
                    if "DimiSalut" not in message.content:
                        cc=1
            if cc == 1:
                await message.add_reaction("<:Coucou:865883301814599681>") #Le bot ajoute une réaction saluant la personne qui dit bonjour
            
            auteur = message.author
            if auteur.id==329554825907798019: #Réponds feur à Kamlox
                if message.content[-4:].lower() == "quoi" or message.content[-3:].lower() == "koi":
                    await message.channel.send("FEUR")
            if message.guild == None:
                channel = await self.bot.fetch_user(323147727779397632) #Envois le contenu du MP reçu par Véronica à Zratey
                await channel.send("Reçu de la part de {}: {}".format(auteur,message.content))

async def setup(bot):
    await bot.add_cog(on_message(bot))