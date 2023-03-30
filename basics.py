import discord
from discord.ext import commands
from discord import app_commands
from typing import Literal

from time import sleep
from random import randint
import json

class Confirm(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None

    # When the confirm button is pressed, set the inner value to `True` and
    # stop the View from listening to more input.
    # We also send the user an ephemeral message that we're confirming their choice.
    @discord.ui.button(label='Confirm', style=discord.ButtonStyle.green)
    async def confirm(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Confirming', ephemeral=True)
        self.value = True
        button.disabled=True
        self.stop()

    # This one is similar to the confirmation button except sets the inner value to `False`
    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.grey)
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message('Canceling', ephemeral=True)
        self.value = False
        button.disabled=True
        self.stop()

class Counter(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
    # Define the actual button
    # When pressed, this increments the number displayed until it hits 5.
    # When it hits 5, the counter button is disabled and it turns green.
    # note: The name of the function does not matter to the library
    @discord.ui.button(label='0', style=discord.ButtonStyle.red)
    async def count(self, interaction: discord.Interaction, button: discord.ui.Button):
        number = int(button.label) if button.label else 0
        if number + 1 >= 5:
            button.style = discord.ButtonStyle.green
            button.disabled = True
            self.stop()
        button.label = str(number + 1)

        # Make sure to update the message with our updated selves
        await interaction.response.edit_message(view=self)

class CommandesBasiques(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #TEST COMMAND
    @commands.hybrid_command(name="test",description="Commande de test pour le développeur du bot")
    async def test(self,ctx: commands.Context):
        if ctx.author.id==323147727779397632:
            BOUTTONS=Confirm()
            await ctx.reply("Test of button :",view=BOUTTONS,ephemeral=True)
            await BOUTTONS.wait() #On attends que l'intéraction du bouton soit terminée avant d'executer la suite
            await ctx.reply("Interaction terminée")
        else:
            await ctx.reply("Vous n'avez pas la permission d'utiliser cette commande",ephemeral=False)

    #COINFLIP
    @commands.hybrid_command(name="coin",description="Pile ou Face")
    async def coin(self, ctx: commands.Context):
        if randint(0,1):
            await ctx.send("Pile !")
        else:
            await ctx.send("Face !")

    #WRITE
    @commands.hybrid_command(name="write",description="Renvois l'argument dans la console en plus de le renvoyer dans le chat",aliases=['print'])
    @app_commands.describe(chose_a_dire="Qu'est ce que vous voudriez que je répètes ?")
    async def write(self, ctx: commands.Context, chose_a_dire: str):
        await ctx.send(f"{ctx.author} a dit : {chose_a_dire}",ephemeral=False)
        print(f"{ctx.author} a dit : {chose_a_dire}")
    
    #8BALL
    @commands.hybrid_command(name="8ball",description="Pose une question, j'y réponds !")
    @app_commands.describe(question="C'est quoi les bails ?")
    async def ball(self,ctx: commands.Context, question: str=None):
        """Littéralement un 8ball"""
        if question == None:
            await ctx.send("Vous n'avez pas poser de question !")
        else:
            eightballrandom = randint(1,8)
            if eightballrandom == 1:
                await ctx.send(f"Q : {question} \nR : Oui")
            elif eightballrandom == 2:
                await ctx.send(f"Q : {question} \nR : Non")
            elif eightballrandom == 3:
                await ctx.send(f"Q : {question} \nR : Peut être")
            elif eightballrandom == 4:
                await ctx.send(f"Q : {question} \nR : Surement")
            elif eightballrandom == 5:
                await ctx.send(f"Q : {question} \nR : Laisse moi réfléchir...")
                sleep(5)
                await ctx.send(f"Un peu débile comme question non ?")
            elif eightballrandom == 6:
                await ctx.send(f"Q : {question} \nR : Je n'ai pas l'autorisation de répondre à une telle question <:veropillow:909029139682562108><:veropillow2:909029164240232468>")
            elif eightballrandom == 7:
                await ctx.send(f"Q : {question} \nR : Je n'en suis pas si sûre...")
            elif eightballrandom == 8:
                await ctx.send(f"Q : {question} \nR : Pour le savoir, essais de le résoudre par toi même !")
                sleep(5)
                tentative_don = await ctx.send("Tu peux me payer 10$ sinon pour répondre à cette question <:Zeldapose:905816408267571200>")
                sleep(5)
                await tentative_don.delete()

    #GAMEMODE
    @app_commands.command(name="gamemode",description="Cheat Code")
    @app_commands.describe(mode="Quel gamemode souhaiteriez vous passez ?")
    async def gamemode(self, interaction: discord.Interaction,mode: str) -> None:
        """Cheat code"""
        await interaction.response.send_message("""```\nJava Error occured :\nJava is not installed on this current device system because, fréro, je suis un Bot Discord pas l'invite de commande MineCraft -_-```""")

    #PDP
    @commands.hybrid_command(name="pdp",description="Affiche la photo de profil d'un utilisateur",aliases=['pfp'])
    @app_commands.describe(arg="Utilisateur à sélectionner")
    async def pdp(self,ctx,arg: discord.Member=None):
        """Affiche la photo de profil d'un utilisateur"""
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.3")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
        if arg != None:
            embedVar.add_field(name="{}".format(arg),value="Photo de profil de {} !".format(arg), inline=False)
            embedVar.set_image(url="{}".format(arg.avatar))
        else:
            embedVar.add_field(name="{}".format(ctx.author),value="Voici votre photo de profil !", inline=False)
            embedVar.set_image(url="{}".format(ctx.author.avatar))
        await ctx.send(embed=embedVar)
    
    #STRAWPOLL
    @commands.hybrid_command(name="poll",description="Génère un sondage à partir du message entré dans la commande")
    @app_commands.describe(question="Question du sondage")
    async def poll(self,ctx: commands.Context, question: str):
        embedVar = discord.Embed(color=discord.Color.blue())
        embedVar.set_footer(text="Véronica Alpha 1.3")
        embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
        embedVar.add_field(name="Suggestion proposée :",value="{}".format(question), inline=False)
        temp=await ctx.send(embed=embedVar)
        await temp.add_reaction(self.bot.get_emoji(608326594485944321))
        await temp.add_reaction(self.bot.get_emoji(608326560906346505))

#-------------------------------------------- RECHERCHES --------------------------------------------
    #GOOGLE
    @commands.hybrid_command(name="google",description="Quick Search -> Google",aliases=['search'])
    @app_commands.describe(content="Effectuez une recherche sur Google")
    async def google(self,ctx,content: str):
        """Permet de faire une recherche rapide sur Google à partir d'une simple commande"""
        await ctx.send("Voilà le résultat de votre recherche via le moteur de recherche Google : https://www.google.com/search?q={}".format(content))
        await ctx.send("Peut être que la définition de ce que vous cherchez est sur Urban Dictionay ? Essayez la commande ``v.meaning``",ephemeral=True)
    
    #WIKIPEDIA
    @commands.hybrid_command(name="wikipedia",description="Quick Search -> Wikipédia",aliases=['wiki'])
    @app_commands.describe(content="Effectuez une recherche sur Wikipédia")
    async def wikipedia(self,ctx,content: str):
        await ctx.send("Voilà le résultat de votre recherche via Wikipédia : https://fr.wikipedia.org/wiki/{}".format(content))
        await ctx.send("Si rien ne s'affiche, cela veux dire que ce que vous avez recherché n'existe pas sur Wikipédia. Essayez une simple recherche internet avec ``v.google``",ephemeral=True)
    
    #MEANING
    @commands.hybrid_command(name="meaning",description="Définition (internet) -> Urban Dictionnary")
    @app_commands.describe(content="Mot dont vous voulez savoir la signification, via Urban Dicitonnary")
    async def meaning(self,ctx,content: str):
        await ctx.send("Voilà le résultat de votre recherche via Urban Dictionnary : https://www.urbandictionary.com/define.php?term={}".format(content))
        await ctx.send("Sa définition n'existe peut être pas sur Urban Dictionnary, donc pourquoi pas faire votre propre recherche ? Essayez la commande ``v.google``",ephemeral=True)

    #Viewer
    @commands.hybrid_command(name="viewer",description="Ajoute/retire les notifications (via mention) pour des news à propos de streams sur Twitch")
    async def viewer(self,ctx):
        """Permet d'être notifié quand une information est transmise à propos d'un stream. Refaire la commande désactive les notifications"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 397367943769358338:
            role = discord.utils.get(ctx.guild.roles, name="Viewer")
            if role in ctx.author.roles: #Retire le rôle
                await ctx.author.remove_roles(role)
                await ctx.send("Vous ne recevrez plus de notifications pour les streams !")
            else: #Ajoute le rôle
                await ctx.send("Vous avez obtenu le role Viewer <@!{}> ! Vous serez ping à chaque fois qu'un membre du serveur lancera un stream :)".format(ctx.author.id))
                await ctx.author.add_roles(role)
        else:
            await ctx.send("Ce n'est pas le bon channel pour effectuer cette commande",ephemeral=True)
#------------------------------------------- EVENT -----------------------------------------------
    #Event
    @commands.hybrid_command(name="event",description="Ajoute/retire les notifications (via mention) pour des news à propos d'events sur le serveur")
    async def event(self,ctx):
        """Permet d'être notifié quand une information est transmise à propos d'un event organisé sur le serveur. Refaire la commande désactive les notifications"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 397367943769358338:
            role = discord.utils.get(ctx.guild.roles, name="Event")
            if role in ctx.author.roles: #Retire le rôle
                await ctx.author.remove_roles(role)
                await ctx.send("Vous ne recevrez plus de notifications pour les événements !")
            else: #Ajoute le rôle
                await ctx.send("Vous avez obtenu le role event <@!{}> ! Vous serez ping à chaque fois qu'un nouvel event se déroulera :)".format(ctx.author.id))
                await ctx.author.add_roles(role)
        else:
            await ctx.send("Ce n'est pas le bon channel pour effectuer cette commande",ephemeral=True)

    #Inscription
    @commands.hybrid_command(name="inscription",description="Vous inscrit a l'event de la semaine",aliases=['in'])
    async def inscription(self,ctx):
        """Inscrit l'utilisateur qui execute cette commande à l'event de la semaine"""
        if ctx.channel.id == 397378707960102922 or ctx.channel.id == 827971395731324969:
            role = discord.utils.get(ctx.guild.roles, name="Inscrit")
            if role in ctx.author.roles: #Retire le rôle
                await ctx.author.remove_roles(role)
                await ctx.send("Vous êtes désinscrit <@!{}> !".format(ctx.author.id))
                #Retire la personne de la liste des inscrits :
                if not inscription_remove(ctx.author.id):
                    #Cela veut dire que la personne n'était déjà plus dans la liste
                    await ctx.send("Vous ne figuriez déjà pas dans la liste des inscrits avant votre inscription. Etrange..")
            else: #Ajoute le rôle
                await ctx.send("Vous êtes désormais inscrit à l'événement de la semaine <@!{}> !".format(ctx.author.id))
                await ctx.author.add_roles(role)
                #Ajoute l'utilisateur dans la liste des inscrits
                if not inscription_add(ctx.author.id):
                    #Cela veut dire que la personne était déjà dans la liste
                    await ctx.send("Vous étiez déjà dans la liste des inscrits ? Etrange..")
        else:
            await ctx.send("Ce n'est pas le bon channel pour effectuer cette commande",ephemeral=True)
    
    #Inscription Clear
    @commands.hybrid_command(name="inscription_clear",description="Retire à tout les inscrits listés, leur rôle inscrit et check in")
    async def inscription_clear(self,ctx):
        role = discord.utils.get(ctx.guild.roles, name="🍳Goûteur")
        if role in ctx.author.roles:
            guild=self.bot.get_guild(397332012542853122)
            with open("liste_inscrits.json") as f:
                temp = json.load(f)
            rapport=""
            for i in range(len(temp["IDs_list"])):
                membre = guild.get_member(temp["IDs_list"][i])
                try:
                    await membre.remove_roles(discord.utils.get(ctx.guild.roles, name="Inscrit"))
                    rapport += "- ⏬ <@!{}> n'a désormais plus le rôle inscrit\n".format(temp["IDs_list"][i])
                except:
                    rapport += "- <@!{}> n'avait pas le rôle Inscrit\n".format(temp["IDs_list"][i])
                try:
                    await membre.remove_roles(discord.utils.get(ctx.guild.roles, name="Checked in"))
                    rapport += "- ⏬ <@!{}> n'a désormais plus le rôle checked in\n".format(temp["IDs_list"][i])
                except:
                    rapport += "- <@!{}> n'avait pas le rôle Checked in\n".format(temp["IDs_list"][i])
            #On efface tout dans le fichier texte :
            temp["IDs_list"]=[]
            with open("liste_inscrits.json","w") as f:
                json.dump(temp,f)
            await ctx.send("Les participants n'ont plus leurs rôles de participation à l'event!")
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text="Véronica Alpha 1.3")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
            embedVar.add_field(name="Rapport de la commande :",value="{}".format(rapport), inline=False)
            await ctx.send(embed=embedVar)
        else:
            await ctx.send("Vous n'avez pas la permission d'executer cette commande!")
    
    #Liste Inscrits
    @commands.hybrid_command(name="liste_inscrits",description="Liste les personnes inscrites à l'événement de la semaine")
    async def liste_inscrits(self,ctx):
        with open("liste_inscrits.json") as f:
            temp = json.load(f)
        if not len(temp["IDs_list"]): #Si il n'y a pas d'inscrits
            await ctx.send("Il n'y a pas d'inscrit pour l'événement de cette semaine")
        else:
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text="Véronica Alpha 1.3")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
            liste=""
            for i in range(len(temp["IDs_list"])):
                liste=liste+"- <@!"+str(temp["IDs_list"][i])+">\n"
            embedVar.add_field(name="Liste des participants :",value="{}".format(liste), inline=False)
            await ctx.send(embed=embedVar)

    #Here
    @commands.hybrid_command(name="here",description="[CHECK-IN] : Confirme votre présence à l'event de la semaine")
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
                    await ctx.send("Soyez sur d'être inscrit avant de confirmer votre présence. Pour vous inscrire, effectuez la commande </inscription:1037315937025654804>")
    """
    @commands.hybrid_command(name="rps",description="Jouez à Pierre Feuille Ciseaux contre moi !")
    @app_commands.describe(choix="Chosissez entre Pierre, Feuille et Ciseaux")
    async def rps(self,ctx,choix: Literal['🪨rock',"🧻paper","✂️scissors"]):
        initiation=initiation_convertion(choix) #réponse de l'utilisateur en int
        if initiation==4:
            await ctx.send("Vous n'avez pas mis le bon argument !")
        else:
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_footer(text="Véronica Alpha 1.3")
            embedVar.set_author(name="Commande réalisée par {}".format(ctx.author), icon_url="{}".format(ctx.author.avatar))
            embedVar.add_field(name="Vous avez choisi :",value="{}".format(str_rps(initiation)), inline=True)
            reply_rps=randint(1,3) #choix aléatoire de la réponse de Véronica
            embedVar.add_field(name="Véronica a choisi :",value="{}".format(str_rps(reply_rps)), inline=True)
            result=rps_win(initiation,reply_rps)
            if result == "Tie":
                embedVar.add_field(name="Egalité !",value="{} Vs {}".format(str_rps(initiation),str_rps(reply_rps)), inline=False)
            elif result:
                embedVar.add_field(name="J'ai gagné !",value="{} Vs **{}**".format(str_rps(initiation),str_rps(reply_rps)), inline=False)
            else:
                embedVar.add_field(name="Félicitation ! Vous avez gagné !",value="**{}** Vs {}".format(str_rps(initiation),str_rps(reply_rps)), inline=False)
            await ctx.send(embed=embedVar)
    """
async def setup(bot):
    await bot.add_cog(CommandesBasiques(bot))

# ----- Définitions pour le RPS -----
def initiation_convertion(arg):
    """Détermine la réponse de l'utilisateur et la convertie en un nombre entier"""
    if "rock" in arg.lower() or "pierre" in arg.lower() or "🪨" in arg:
        return 1
    elif "paper" in arg.lower() or "sheet" in arg.lower() or "papier" in arg.lower() or "feuille" in arg.lower() or "🧻" in arg:
        return 2
    elif "scissors" in arg.lower() or "ciseaux" in arg.lower() or "✂️" in arg:
        return 3
    else:
        return 4

def str_rps(reply):
    if reply == 1:
        return "🪨Pierre"
    elif reply==2:
        return "🧻Papier"
    elif reply==3:
        return "️️️✂️Ciseaux"

def rps_win(init,reply):
    """Si 0 retourné, le joueur a gagné, si 1 retourné, Véronica a gagné, sinon c'est une égalité"""
    liste3=[1,2,3]
    for i in range(len(liste3)):
        if liste3[i]==init:
            if liste3[i-1]==reply: #condition de victoire
                return 0
            elif init==reply: #condition d'égalité
                return "Tie"
            else: #Aucune des autres conditions sont replies, donc condition de défaite
                return 1

# ----- Définitions pour les listes d'inscription -----
def inscription_remove(id)->bool:
    with open("liste_inscrits.json","r") as f:
        temp = json.load(f)
    if id in temp["IDs_list"]:
        temp["IDs_list"].remove(id)
        with open("liste_inscrits.json","w") as f:
            json.dump(temp,f)
        return True
    else:
        return False

def inscription_add(id)->bool:
    with open("liste_inscrits.json","r") as f:
        temp = json.load(f)
    if id not in temp["IDs_list"]:
        temp["IDs_list"].append(id)
        with open("liste_inscrits.json","w") as f:
            json.dump(temp,f)
        return True
    else:
        #La personnes est déjà dans la liste des inscrits ?
        return False