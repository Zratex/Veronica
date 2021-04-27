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
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="dans les yeux celui qui lis ce message 👀"))

@client.command()
async def here(ctx):
    if ctx.channel.id == 397378707960102922:
        role = discord.utils.get(ctx.guild.roles, name="Checked In")
        if role in ctx.author.roles:
            await ctx.send("oe")
        else:
            await ctx.send("o")
            await ctx.author.add_roles(role)

@client.command()
async def test(ctx):
    if ctx.author.id == 323147727779397632: #Check if it's Zratey
        await ctx.send("{}".format(ctx.message.content))

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

###################################################################################################
#                                            MONEY                                                #
###################################################################################################

@client.command()
#une définition en anglais par Urban Dictionnarry 
async def meaning(ctx):
    txt = ctx.message.content
    txt = txt[10:]
    txt2 =""
    for x in txt:
        if x == " ":
            txt2=txt2+"_"
        else:
            txt2=txt2+x
    await ctx.channel.send("https://www.urbandictionary.com/define.php?term={}".format(txt2))
    await ctx.channel.send("Si rien ne s'affiche, cela veux dire que ce que vous avez recherché n'existe pas sur Urban Dictionay. Essayez une simple recherche internet avec ``v.google``")

@client.command()
async def money(ctx):
    #show the current money of a user
    if ctx.channel.id == 397367943769358338 or 397378707960102922:
        if os.path.exists(f"money/{ctx.author.id}wallet.txt"):
            filemoney = open(f"money/{ctx.author.id}wallet.txt", "r")
            for x in filemoney:
                bank=x
            filemoney.close()
            await ctx.channel.send("Vous avez **{}**<:coquillette:802972160364249119> dans votre compte en banque <@!{}> !".format(bank, ctx.author.id))
        else:
            await ctx.channel.send("Vous n'avez pas de porte-feuille ? Laissez moi en créer un pour vous...")
            filemoney = open(f"money/{ctx.author.id}wallet.txt", "w")
            filemoney.write("150")
            await ctx.channel.send("C'est fait ! J'ai ouvert un compte bancaire pour vous ! Vous débutez avec **150**<:coquillette:802972160364249119>.")
            filemoney.close()
    else:
        await ctx.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(ctx.author.id))

@client.command()
async def shop(ctx):
    if ctx.channel.id==397367943769358338 or 397378707960102922:
        if os.path.exists(f"money/{ctx.author.id}wallet.txt"):
            filemoney = open(f"money/{ctx.author.id}wallet.txt", "r")
            for x in filemoney:
                bank=int(x)
            filemoney.close()
            await ctx.channel.send("Bienvenue dans le shop ! Veuillez sélectionner quelque chose à acheter en répondant à mon message par le numéro qui correspond à votre achat.")
            embedVar = discord.Embed(title="Véronica's shop !", description="Le shop de Véronica si vous avez du mal avec l'anglais <:Wink:608327025098489863>", color=discord.Color.blue())
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
            embedVar.add_field(name=":one: Rôle DJ", value="Coût : 500<:coquillette:802972160364249119>", inline=True)
            embedVar.add_field(name=":two: Rôle personnalisé", value="Coût : 15000<:coquillette:802972160364249119>", inline=True)
            embedVar.add_field(name=":three: Lootbox", value="Coût : 1000<:coquillette:802972160364249119>", inline=True)
            embedVar.add_field(name="v.cancel", value="Vous permet d'annuler la commande", inline=False)
            embedVar.set_footer(text="Alpha version of Véronica")
            await ctx.channel.send(embed=embedVar)
            while True:
                response = await client.wait_for("message")
                if ctx.channel.id == response.channel.id:
                    if ctx.author.id == response.author.id:
                        try:
                            result=int(response.content)
                            if result >= 1 or result <= 3:
                                if result == 1:
                                    if bank-500 >= 0:
                                        role = discord.utils.get(ctx.author.guild.roles, name="DJ")
                                        if role in ctx.author.roles:
                                            await ctx.channel.send("Vous avez déjà le rôle DJ ! Vous ne pouvez pas l'acheter de nouveau")
                                            break
                                        else:
                                            bank=bank-500
                                            filemoney = open(f"money/{ctx.author.id}wallet.txt", "w")
                                            filemoney.write("{}".format(bank))
                                            filemoney.close()
                                            await ctx.author.add_roles(role)
                                            await ctx.channel.send("Vous avez dépensé **500**<:coquillette:802972160364249119> pour obtenir le rôle DJ !")
                                            break
                                    else:
                                        await ctx.channel.send("Désolé, mais vous n'avez pas assez d'argent pour vous acheter ceci")
                                        break
                            if result == 2:
                                if bank-15000 >= 0:
                                    bank=bank-15000
                                    filemoney = open(f"money/{ctx.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(bank))
                                    filemoney.close()
                                    await ctx.channel.send("Vous avez dépensé **5000**<:coquillette:802972160364249119> pour obtenir l'autorisation d'avoir un rôle personnalisé ! Veuillez contacter un membre du staff en lui montrant mon message afin qu'il puisse le vous créer.")
                                    break
                                else:
                                    await ctx.channel.send("Désolé, mais vous n'avez pas assez d'argent pour vous acheter ceci")
                                    break
                            if result == 3:
                                if bank-1000 >= 0:
                                    bank=bank-1000
                                    filemoney = open(f"money/{ctx.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(bank))
                                    filemoney.close()
                                    await ctx.channel.send("Vous avez dépensé **1000**<:coquillette:802972160364249119> pour obtenir une lootbox ! Pour l'ouvrir, veuillez voir dans le menu dédié avec la commande ``/lootbox``")
                                    amount=0
                                    if os.path.exists(f"money/{ctx.author.id}.txt"):
                                        filebox = open(f"money/{ctx.author.id}wallet.txt", "r")
                                        for x in filebox:
                                            amount=int(x)
                                        filebox.close()
                                        filebox = open(f"money/{ctx.author.id}wallet.txt", "w")
                                        filebox.write("{}".format(amount+1))
                                        filebox.close()
                                        break
                                    else:
                                        await ctx.channel.send("Désolé, mais vous n'avez pas assez d'argent pour vous acheter ceci")
                                        break
                            else:
                                await ctx.channel.send("La valeur est incorrecte. Veuillez réessayer")
                        except ValueError:
                            if response.content.startswith("v.cancel"):
                                await ctx.channel.send("Commande annulée !")
                                break
                            else:
                                await ctx.channel.send("Votre réponse n'est pas un chiffre ! Veuillez essayer de nouveau.")
                    else:
                        await ctx.channel.send("Ce n'est pas à vous de répondre <@!{}> ! S'il vous plaît <@!{}>, veuillez répondre à ce que je vous demande.".format(response.author.id,ctx.author.id))
                        break
                else:
                    await ctx.channel.send("Vous n'avez pas de compte en banque dans ma base de donnée ! Veuillez effectuer la commande ``/money`` pour vous en créer un.")
                    break
            else:
                await ctx.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(ctx.author.id))

@client.command()
async def donate(ctx):
    if ctx.channel.id == 397367943769358338 or 397378707960102922:
        txt = ctx.message.content
        if txt[:12] == "v.donate <@!":
            if txt[31:32] == " ":
                validcommand=1
            else:
                validcommand=0
        else:
            validcommand=0
        check_int=txt[32:]
        for x in check_int:
                if x != "0" and x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8" and x != "9":
                    validcommand = 0
                
        if validcommand==1:
            identifient = txt[12:30]
            value= int(txt[32:])
            if os.path.exists(f"money/{ctx.author.id}wallet.txt"):
                filemoney = open(f"money/{ctx.author.id}wallet.txt", "r")
                for x in filemoney:
                    current_money=int(x)
                filemoney.close()
            else:
                await ctx.channel.send("Vous n'avez pas de compte en banque dans ma base de donnée ! Veuillez effectuer la commande ``v.money`` pour vous en créer un.")
                    
            if current_money-value >= 0:
                if os.path.exists(f"money/{identifient}wallet.txt"):
                    if int(identifient) != ctx.author.id:
                        filemoney = open(f"money/{identifient}wallet.txt", "r")
                        for x in filemoney:
                            gift_man_money=int(x)
                        filemoney.close()

                        filemoney = open(f"money/{ctx.author.id}wallet.txt", "w")
                        filemoney.write("{}".format(current_money-value))
                        filemoney.close()

                        filemoney = open(f"money/{identifient}wallet.txt", "w")
                        filemoney.write("{}".format(gift_man_money+value))
                        filemoney.close()

                        await ctx.channel.send("Votre don de **{}** <:coquillette:802972160364249119> a été transité avec succès !".format(value))
                    else:
                        await ctx.channel.send("Bien essayé 😏")
                else:
                    await ctx.channel.send("La personne a qui vous vouliez faire une transaction n'a pas de compte en banque ! Demandez lui d'éxecuter la commande ``v.money`` pour qu'elle puisse s'en créer un !")
            else:
                await ctx.channel.send("Vous n'avez pas assez d'argent pour effectuer cette transaction.")
                    
        else:
            await ctx.channel.send("Syntaxe invalide pour la commande donate ! Voici comment vous devez disposer la commande :")
            await ctx.channel.send("``v.donate [mention d'une destinataire] [valeur de money qui va être transité]``")
            await ctx.channel.send("Suivez l'exemple que je viens d'envoyer juste au dessus. N'oubliez pas de remplacer ce qu'il y a en crochet parce qui est indiqué, ainsi que de ne pas oublier de respecter les espaces !")
    else:
        await ctx.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(ctx.author.id))

@client.command()
async def daily(ctx):
    if ctx.channel.id == 397367943769358338 or 397378707960102922:
        if os.path.exists(f"money/{ctx.author.id}wallet.txt"):
            filemoney = open(f"money/{ctx.author.id}wallet.txt", "r")
            for x in filemoney:
                current_money=int(x)
            filemoney.close()

            if os.path.exists(f"money/{ctx.author.id}dailycooldown.txt"):
                filemoney = open(f"money/{ctx.author.id}dailycooldown.txt", "r")
                for x in filemoney:
                    past_time=int(x)
                filemoney.close()
            else:
                filemoney = open(f"money/{ctx.author.id}dailycooldown.txt", "w")
                filemoney.write("000000000")
                filemoney.close()
                filemoney = open(f"money/{ctx.author.id}dailycooldown.txt", "r")
                for x in filemoney:
                    past_time=int(x)
                filemoney.close()

            current_time=str(int(time.time()))
            zawarudo=int(current_time)-past_time

            if zawarudo >= 86400:
                validcommand=1
            else:
                validcommand=0
                    
            if validcommand==1:
                filemoney = open(f"money/{ctx.author.id}dailycooldown.txt", "w")
                filemoney.write("{}".format(current_time))
                filemoney.close()

                filemoney = open(f"money/{ctx.author.id}wallet.txt", "w")
                filemoney.write("{}".format(current_money+50))
                filemoney.close()
                await ctx.channel.send("<@!{}>, vous avez récupéré **50**<:coquillette:802972160364249119> journalier. :white_check_mark:".format(ctx.author.id))
                validcommand=0
            else:
                await ctx.channel.send("Calmez vous <@!{}> ! Ce n'est pas encore le temps de réclamer votre récompense journalière !".format(ctx.author.id))
            validcommand=0
                
        else:
            await ctx.channel.send("Vous n'avez pas de porte-feuille ? Laissez moi en créer un pour vous...")
            filemoney = open(f"money/{ctx.author.id}wallet.txt", "w")
            filemoney.write("200")
            await ctx.channel.send("C'est fait ! J'ai ouvert un compte bancaire pour vous ! Vous débutez avec **150**<:coquillette:802972160364249119> !")
            await ctx.channel.send("Ne vous inquiétez pas, je vous ait bien évidemment ajouté à ces **150**<:coquillette:802972160364249119>, vos **50**<:coquillette:802972160364249119> de la récompense journalière :eyes:")
            filemoney.close()

            current_time="{}".format(time.time())
            current_time=current_time[0:9]
            filemoney = open(f"money/{ctx.author.id}dailycooldown.txt", "w")
            filemoney.write("{}".format(current_time))
            filemoney.close()
            
    else:
        await ctx.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(ctx.author.id))

class MyClient(discord.Client):
    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

    
        

client.run(os.environ['token'])
