import discord
import time
import calendar
from discord.ext import commands
from discord.utils import get
import os
client = commands.Bot(command_prefix = 'v.')

@client.event
async def on_ready():
    print('Connectée')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="moi ! Je ne fais office que de présence 😎"))



class MyClient(discord.Client):
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

    
@client.command()
async def here(ctx):
    if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
        role = discord.utils.get(ctx.guild.roles, name="Inscrit")
        checkin = discord.utils.get(ctx.guild.roles, name="Checked In")
        if checkin in ctx.author.roles:
            await ctx.send("Vous avez déjà confirmé votre présence !")
        else:
            if role in ctx.author.roles:
                await ctx.send("Merci d'avoir vérifié votre présence pour l'événement de la semaine <@!{}> !".format(ctx.author.id))
                await ctx.author.add_roles(checkin)
            else:
                await ctx.send("Soyez sur d'être inscrit avant de confirmer votre présence. Pour vous inscrire, effectuez la commande ``v.inscription``")
            

@client.command()
async def inscription(ctx):
    if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
        role = discord.utils.get(ctx.guild.roles, name="Inscrit")
        if role in ctx.author.roles:
            await ctx.send("Vous vous êtes déjà inscrit <@!{}> !".format(ctx.author.id))
        else:
            await ctx.send("Vous êtes désormais inscrit à l'événement de la semaine <@!{}> !".format(ctx.author.id))
            await ctx.author.add_roles(role)

@client.command(aliases=['désinscription'])
async def desinscription(ctx):
    if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
        role = discord.utils.get(ctx.guild.roles, name="Inscrit")
        if role in ctx.author.roles:
            await ctx.send("Vous êtes désormais désinscrit de l'événement de la semaine <@!{}> !".format(ctx.author.id))
            await ctx.author.delete_roles(role)
        else:
            await ctx.send("Vous n'êtes pas inscrit à l'événement de la semaine <@!{}> !".format(ctx.author.id))

@client.command()
async def test(ctx):
    if ctx.author.id == 323147727779397632: #Check if it's Zratey
        await ctx.send("{}".format(ctx.message.content))

@client.command()
async def event(ctx):
    if ctx.channel.id == 397378707960102922 or ctx.channel.id == 397367943769358338:
        role = discord.utils.get(ctx.guild.roles, name="Event")
        if role in ctx.author.roles:
            await ctx.send("Vous avez déjà le role !")
        else:
            await ctx.send("Vous avez obtenu le role event <@!{}> ! Vous serez ping à chaque fois qu'un nouvel event se déroulera :)".format(ctx.author.id))
            await ctx.author.add_roles(role)

@client.command()
#recherche sur Google
async def google(ctx):
    txt = ctx.message.content
    txt = txt[9:]
    txt2 =""
    for x in txt:
        if x == " ":
            txt2=txt2+"_"
        else:
            txt2=txt2+x
    await ctx.channel.send("Voilà le résultat de votre recherche via le moteur de recherche Google : https://www.google.com/search?q={}".format(txt2))
    await ctx.channel.send("Peut être que la définition de ce que vous cherchez est sur Urban Dictionay ? Essayez la commande ``v.meaning``")

@client.command()
#recherche sur Wiki
async def wiki(ctx):
    txt = ctx.message.content
    txt = txt[7:]
    txt2 =""
    for x in txt:
        if x == " ":
            txt2=txt2+"_"
        else:
            txt2=txt2+x
    await ctx.channel.send("Voilà le résultat de votre recherche via Wikipédia : https://fr.wikipedia.org/w/index.php?search={}".format(txt2))
    await ctx.channel.send("Si rien ne s'affiche, cela veux dire que ce que vous avez recherché n'existe pas sur Wikipédia. Essayez une simple recherche internet avec ``v.google``")
@client.command()
#recherche sur Google
async def meaning(ctx):
    txt = ctx.message.content
    txt = txt[10:]
    txt2 =""
    for x in txt:
        if x == " ":
            txt2=txt2+"_"
        else:
            txt2=txt2+x
    await ctx.channel.send("Voilà le résultat de votre recherche via Urban Dictionnary : https://www.urbandictionary.com/define.php?term={}".format(txt2))
    await ctx.channel.send("Sa définition n'existe peut être pas sur Urban Dicrionnary, donc pourquoi pas faire votre propre recherche ? Essayez la commande ``v.google``")



    
client.run(os.environ['token'])
