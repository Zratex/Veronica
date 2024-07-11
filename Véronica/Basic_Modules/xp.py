import discord
from discord.ext import commands
from discord import app_commands

from random import randint

#Importation des fonctions pour communiquer avec la base de donnée
from Database import database


class XP(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.id == 752958545758126082:
            return #On veux pas que le bot se réponde à lui même
        else:
            if message.channel.id==397378707960102922:
                if database.UserExist(message.author.id):
                    if database.setUserXp(message.author.id,None,randint(5,15))==-1:
                        await message.channel.send("Félicitations <@!{}> ! Vous êtes parvenu au niveau **{}**".format(message.author.id,database.getUserLvl(message.author.id)))
                else:
                    await message.channel.send("Vous n'êtes pas inscrit dans la base de donnée ! Laissez moi vous créer un profile..")
                    try:   
                        database.createUser(message.author.id)
                    except Exception as E:
                        await message.channel.send("Une erreure est survenue. Veuillez contacter Zratey de l'erreur. L'erreur en question : {E}")
                    else:
                        await message.channel.send("C'est fait, vous avez désormais un profile dans la base de donnée !")

async def setup(bot):
    await bot.add_cog(XP(bot))