import discord
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
            if ctx.author.id == 323147727779397632: #Check if it's Zratey
                await ctx.send("test")
            else:
                await ctx.send("Seul Zratey est autorisé à utiliser cette commande")
        else:
            await ctx.send("Haha")
    
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

    @commands.command(aliases=['in'])
    async def inscription(ctx):
        """S'inscrit à un certain event"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
            role = discord.utils.get(ctx.guild.roles, name="Inscrit")
            if role in ctx.author.roles:
                await ctx.send("Vous vous êtes déjà inscrit <@!{}> !".format(ctx.author.id))
            else:
                await ctx.send("Vous êtes désormais inscrit à l'événement de la semaine <@!{}> !".format(ctx.author.id))
                await ctx.author.add_roles(role)
    
    @commands.command(aliases=['8ball'])
    async def ball(self,ctx):
        """Littéralement un 8ball"""
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
            await ctx.send("Je n'ai pas l'autorisation de répondre à une tel question")
        elif eightballrandom == 7:
            await ctx.send("Je n'en suis pas si sûre...")
        elif eightballrandom == 8:
            await ctx.send("Pour le savoir, essais de le résoudre par toi même !")
            time.sleep(10)
            tentative_don = await ctx.send("Tu peux me payer 10$ sinon pour répondre à cette question ")
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
                txt2=txt2+"_"
            else:
                txt2=txt2+x
        await ctx.channel.send("Voilà le résultat de votre recherche via Urban Dictionnary : https://www.urbandictionary.com/define.php?term={}".format(txt2))
        await ctx.channel.send("Sa définition n'existe peut être pas sur Urban Dicrionnary, donc pourquoi pas faire votre propre recherche ? Essayez la commande ``v.google``")

    @commands.command()
    async def gamemode(self,ctx):
        """Cheat code"""
        await ctx.channel.send("`Java Error occured : Java is not installed in this current system because, man, je suis un Bot Discord pas l'invité de commande MineCraft`")
    
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
                else:
                    await ctx.send("Soyez sur d'être inscrit avant de confirmer votre présence. Pour vous inscrire, effectuez la commande ``v.inscription``")

    @commands.command()
    async def event(self,ctx):
        """Permet d'être notifié quand une information est transmise à propos d'un event organisé sur le serveur"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 397367943769358338:
            role = discord.utils.get(ctx.guild.roles, name="Event")
            if role in ctx.author.roles:
                await ctx.send("Vous avez déjà le role !")
            else:
                await ctx.send("Vous avez obtenu le role event <@!{}> ! Vous serez ping à chaque fois qu'un nouvel event se déroulera :)".format(ctx.author.id))
                await ctx.author.add_roles(role)
    
    @commands.command()
    async def pdp(ctx):
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.add_field(name="Commande réalisée par {}".format(ctx.author), value="Voici votre photo de profile", inline=False)
        embedVar.set_image(url="{}".format(ctx.author.avatar_url))
        await ctx.send(embed=embedVar)