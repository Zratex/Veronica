import typing
import discord
from discord import embeds
from discord.ext import commands
import time
from random import randint
import time

def setup(bot):
    bot.add_cog(CommandesBasiques(bot))

class CommandesBasiques(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def test(self,ctx):
        """Commande de test de Zratey"""
        if ctx.author.id == 323147727779397632: #Check if it's Zratey
            untest = await ctx.send("test")
            await untest.add_reaction('👍')
            def check(reaction,emoji):
                return reaction.message.id == untest.id and str(reaction.emoji) == '👍'
            reaction, reaction_bot = await self.bot.wait_for('reaction_add', check=check, timeout=60)
            if reaction_bot.id == untest.author.id:
                try:
                    reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=60)
                    await ctx.send("Complete")
                except:
                    await ctx.send("Commande interrompu. Vous avez pris trop de temps pour répondre")
        else:
            await ctx.send("Seul Zratey est autorisé à utiliser cette commande")
    
    @commands.command()
    async def testpara(self,ctx,arg=None):
        if arg != None:
            """Seconde Commande de test de Zratey"""
            if ctx.author.id == 323147727779397632 or ctx.author.id == 376321007583232002: #Check if it's Zratey
                embedVar = discord.Embed(color=discord.Color.blue())
                embedVar.set_author(name="Votre rôle principal")
                compteur=-1
                for role in ctx.guild.roles:
                    compteur=compteur+1 #nombre de rôles total sur le serv
                for i in range(compteur,1,-1): #1 c'est jusqu'où il doit aller, -1 pour commencer par les rôles les plus hauts
                    if ctx.guild.roles[i] in ctx.author.roles: #Vérifie que l'utilisateur a le rôle en question
                        if ctx.guild.roles[i].id == 820696835303669801 or ctx.guild.roles[i].id == 820696707859873892 or ctx.guild.roles[i].id == 770329263970582598 or ctx.guild.roles[i].id == 820697165872496710 or ctx.guild.roles[i].id == 820753488677306398:
                            pass
                        else:
                            print(ctx.guild.roles[i].id)
                            embedVar.add_field(name="Role principal", value="{}".format(ctx.guild.roles[i].mention), inline=True)
                            break #sert à rien d'aller plus loin si le résultat est trouvé
                await ctx.send(embed=embedVar)
            else:
                await ctx.send("Seul Zratey est autorisé à utiliser cette commande")
        else:
            await ctx.send("Il manque un argument à la commande.")

    @commands.command(aliases=['print'])
    async def write(self,ctx,arg):
        """Permet de print l'argument dans la console en plus de renvoyer l'argument"""
        await ctx.send("Envoyé par {} : {}".format(ctx.author,arg))
        print("Envoyé par {} : {}".format(ctx.author,arg))

    @commands.command()
    async def clear(self,ctx, nombre : int):
        """Supprime un certain nombre de messages selon le nombre indiqué. Cette commande est accessible seulement par les membres de la modération"""
        role = discord.utils.get(ctx.guild.roles, name="Chefs cuisiniers 🍴")
        if role in ctx.author.roles:
            messages = await ctx.channel.history(limit = nombre + 1).flatten()
            for message in messages :
                await message.delete()
            clear_done = await ctx.send("{} messages ont été effacés avec succès".format(nombre))
            time.sleep(10)
            await clear_done.delete()
        else:
            await ctx.send("Vous n'avez pas les permissions pour executer cette commande")
    
    @commands.command()
    async def coin(self,ctx):
        """Cette commande est un coin flip ! Elle vous retourne de façon aléatoire pile ou face"""
        result=randint(0,1)
        if result == 0:
            await ctx.send("Pile !")
        elif result == 1:
            await ctx.send("Face !")
        else:
            await ctx.send("Erreur ! <@!323147727779397632> help")

#-------------------------------------------- EVENT --------------------------------------------
    @commands.command()
    async def event(self,ctx):
        """Permet d'être notifié quand une information est transmise à propos d'un event organisé sur le serveur"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 397367943769358338:
            role = discord.utils.get(ctx.guild.roles, name="Event")
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.send("Vous ne recevrez plus de notifications pour les événements !")
            else:
                await ctx.send("Vous avez obtenu le role event <@!{}> ! Vous serez ping à chaque fois qu'un nouvel event se déroulera :)".format(ctx.author.id))
                await ctx.author.add_roles(role)
    
    @commands.command(aliases=['in'])
    async def inscription(self,ctx):
        """S'inscrit à un certain event"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
            role = discord.utils.get(ctx.guild.roles, name="Inscrit")
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.send("Vous êtes désinscrits <@!{}> !".format(ctx.author.id))
            else:
                await ctx.send("Vous êtes désormais inscrit à l'événement de la semaine <@!{}> !".format(ctx.author.id))
                await ctx.author.add_roles(role)
    
    @commands.command()
    async def here(self,ctx):
        """Le check in du bot"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
            role = discord.utils.get(ctx.guild.roles, name="Inscrit")
            checkin = discord.utils.get(ctx.guild.roles, name="Checked In")
            if checkin in ctx.author.roles:
                await ctx.send("Vous avez déjà confirmé votre présence !")
            else:
                if role in ctx.author.roles:
                    await ctx.send("Merci d'avoir vérifié votre présence pour l'événement de la semaine <@!{}> !".format(ctx.author.id))
                    await ctx.author.add_roles(checkin)
                    await ctx.author.remove_roles(role)
                else:
                    await ctx.send("Soyez sur d'être inscrit avant de confirmer votre présence. Pour vous inscrire, effectuez la commande ``v.in``")

#-------------------------------------------- FIN EVENT --------------------------------------------
    
    @commands.command(aliases=['8ball'])
    async def ball(self,ctx,arg=None):
        """Littéralement un 8ball"""
        if arg == None:
            await ctx.send("Vous n'avez pas poser de question !")
        else:
            eightballrandom = randint(1,8)
            if eightballrandom == 1:
                await ctx.send("Oui")
            elif eightballrandom == 2:
                await ctx.send("Non")
            elif eightballrandom == 3:
                await ctx.send("Peut être")
            elif eightballrandom == 4:
                await ctx.send("Surement")
            elif eightballrandom == 5:
                await ctx.send("Laisse moi réfléchir...")
                time.sleep(5)
                await ctx.send("Un peu débile comme question non ?")
            elif eightballrandom == 6:
                await ctx.send("Je n'ai pas l'autorisation de répondre à une tel question <:veropillow:909029139682562108><:veropillow2:909029164240232468>")
            elif eightballrandom == 7:
                await ctx.send("Je n'en suis pas si sûre...")
            elif eightballrandom == 8:
                await ctx.send("Pour le savoir, essais de le résoudre par toi même !")
                time.sleep(10)
                tentative_don = await ctx.send("Tu peux me payer 10$ sinon pour répondre à cette question <:Zeldapose:905816408267571200>")
                time.sleep(3)
                await tentative_don.delete()

    @commands.command()
    async def google(self,ctx):
        """Permet de faire une recherche rapide sur Google à partir d'une simple commande"""
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

    @commands.command()
    async def wiki(self,ctx):
        """Permet de faire une recherche rapide sur Wikipédia à partir d'une simple commande"""
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
    @commands.command()
    async def meaning(self,ctx):
        """Permet de faire une recherche rapide sur Urban Dictionnary à partir d'une simple commande"""
        txt = ctx.message.content
        txt = txt[10:]
        txt2 =""
        for x in txt:
            if x == " ":
                txt2=txt2+"%20"
            else:
                txt2=txt2+x
        await ctx.channel.send("Voilà le résultat de votre recherche via Urban Dictionnary : https://www.urbandictionary.com/define.php?term={}".format(txt2))
        await ctx.channel.send("Sa définition n'existe peut être pas sur Urban Dictionnary, donc pourquoi pas faire votre propre recherche ? Essayez la commande ``v.google``")

    @commands.command()
    async def gamemode(self,ctx):
        """Cheat code"""
        await ctx.channel.send("`Java Error occured : Java is not installed in this current system because, man, je suis un Bot Discord pas l'invité de commande MineCraft`")


    
    @commands.command()
    async def pdp(self,ctx,arg: discord.Member=None):
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        if arg != None:
            embedVar.add_field(name="{}".format(arg),value="Photo de profile de {} !".format(arg), inline=False)
            embedVar.set_image(url="{}".format(arg.avatar_url))
        else:
            embedVar.add_field(name="{}".format(ctx.author),value="Voici votre photo de profile !", inline=False)
            embedVar.set_image(url="{}".format(ctx.author.avatar_url))
        await ctx.send(embed=embedVar)
