import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(ModerationCommandes(bot))

class ModerationCommandes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.group(invoke_without_command=True)
    async def help(self,ctx,):
        embedVar = discord.Embed(description="Utilisez `v.help <nom_de_la_commande>` pour avoir les informations à propos de la commande en question",color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Commandes basiques", value="`event`,`here`,`inscription`(ou `in`),`ball`(ou `8ball`),`write` (ou `print`),`coin`,`google` (ou `search`),`wiki`,`meaning` (ou `def`),`pdp`,`rps`,`test`,`testpara`",inline=False)
        embedVar.add_field(name="Modération", value="`clear`,`kick`,`jail`,`mp`",inline=False)
        embedVar.add_field(name="Data", value="`profile`,`setup`,`delete`",inline=False)
        embedVar.add_field(name="Money", value="`daily`,`shop`",inline=False)
        embedVar.add_field(name="Rig PC", value="COMING SOON",inline=False)
        embedVar.add_field(name="Commandes fondamentales", value="`help`,`load`,`reload`,`unload`",inline=False)
        await ctx.send(embed=embedVar)

# ----- Commandes basiques -----
    @help.command(aliases=['testpara'])
    async def test(self,ctx):
        embedVar = discord.Embed(description="Commande de test de Zratey",color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.test** `<les arguments changent en fonction de ce que Zratey veut tester>`",inline=False)
        await ctx.send(embed=embedVar)
    @help.command(aliases=['in'])
    async def inscription(self,ctx):
        desc="**Cette commande ajoute le rôle <@&827971229620502608> à l'utilisateur.** Il sera donc inscrit pour le prochain événement du serveur."
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.inscription** ou **v.in**",inline=False)
        await ctx.send(embed=embedVar)
    @help.command()
    async def here(self,ctx):
        desc="Cette commande permet d'indiquer aux organisateurs de l'événément de la semaine la présence de l'utilisateur avant le début de l'événément. Le rôle <@&848111256794693642> sera attribué, donnant accès à l'utilisateur aux salons relatifs à l'événément de la semaine"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="v.here",inline=False)
        await ctx.send(embed=embedVar)
    @help.command()
    async def event(self,ctx):
        desc="**Cette commande ajoute le rôle <@&830050902445522954> à l'utilisateur.** Ce rôle permet d'être notifié à chaque news en rapport avec les événements du serveur. Refaire cette commande permet de retirer le rôle, donc de ne plus être notifié"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="v.event",inline=False)
        await ctx.send(embed=embedVar)
    @help.command(aliases=['8ball'])
    async def ball(self,ctx):
        desc="Véronica retournera une réponse aléatoire parmis 8 réponses différentes à la question de l'utilisateur."
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.8ball** `<question>` ou **v.ball** `<question>`",inline=False)
        embedVar.add_field(name="Réponse n°1", value="Oui",inline=True)
        embedVar.add_field(name="Réponse n°2", value="Non",inline=True)
        embedVar.add_field(name="Réponse n°3", value="Peut être",inline=True)
        embedVar.add_field(name="Réponse n°4", value="Surement",inline=True)
        embedVar.add_field(name="Réponse n°5", value="Laisse moi réfléchir...Un peu débile comme question non ?",inline=True)
        embedVar.add_field(name="Réponse n°6", value="Je n'ai pas l'autorisation de répondre à une telle question",inline=True)
        embedVar.add_field(name="Réponse n°7", value="Je n'en suis pas si sûre...",inline=True)
        embedVar.add_field(name="Réponse n°8", value="Pour le savoir, essais de le résoudre par toi même !",inline=True)
        await ctx.send(embed=embedVar)
    @help.command(aliases=['print'])
    async def write(self,ctx):
        desc="**Faites coucou à Zratey !** Cette commande est une commande qui sert normalement à Zratey pour print dans ma console de commande certains charactères. Mais vous pouvez l'utiliser si ça vous chante <:zeldashrug:914140291802464258> A noter que les règles du serveur sont applicables même au travers de ce print. De plus, Zratey ne verra pas forcément ce message, donc si vous voulez réellement le contacter, addressez lui la parole via messages privés"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.write** `<votre_message>` ou **v.print** `<votre_message>`",inline=False)
        await ctx.send(embed=embedVar)
    @help.command()
    async def coin(self,ctx):
        desc="C'est un pile ou face ! 🪙"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="v.coin",inline=False)
        await ctx.send(embed=embedVar)
    @help.command(aliases=['search'])
    async def google(self,ctx):
        desc="Génère un lien de recherche Google vers ce que l'utilisateur a mis en argument"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.google** `<votre_recherche>` ou **v.search** `<votre_recherche>`",inline=False)
        await ctx.send(embed=embedVar)
    @help.command()
    async def wiki(self,ctx):
        desc="Génère un lien de recherche Wikipédia vers ce que l'utilisateur a mis en argument"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.wiki** `<votre_recherche>`",inline=False)
        await ctx.send(embed=embedVar)
    @help.command(aliases=['def'])
    async def meaning(self,ctx):
        desc="Génère un lien de recherche Urban Dictionnary pour que l'utilisateur ait la définition du mot qu'il souhaite. En revanche, c'est un dictionnaire d'internet et anglais."
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.meaning** `<votre_recherche>` ou **v.def** `<votre_recherche>`",inline=False)
        await ctx.send(embed=embedVar)
    @help.command()
    async def pdp(self,ctx):
        desc="Retourne la photo de profile de l'utilisateur, ou celle de l'utilisateur qu'il a mentionné"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe pour la pdp de l'utilisateur", value="v.pdp",inline=False)
        embedVar.add_field(name="Syntaxe pour la pdp d'un autre membre du serveur", value="**v.pdp** `@<mention_utilisateur>`",inline=False)
        await ctx.send(embed=embedVar)
    @help.command()
    async def rps(self,ctx):
        desc="Joues au Pierre Feuille Sciseaux avec moi ! La réponse choisie par Véronica est choisie de façon aléatoire"
        embedVar = discord.Embed(description="{}".format(desc),color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.2")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar_url))
        embedVar.add_field(name="Catégorie", value="Commandes basiques",inline=False)
        embedVar.add_field(name="Syntaxe", value="**v.rps** `<argument>` (dans l'élément doit se trouver le choix de l'utilisateur entre 🪨,🧻 et ✂️. L'anglais est supporté)",inline=False)
        await ctx.send(embed=embedVar)
