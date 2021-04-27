import discord
import os
import time
import calendar
from discord.ext.commands import Bot
from discord.ext import commands
from discord.utils import get
from itertools import cycle
from random import randint
from time import sleep

client = commands.Bot(command_prefix = '/')



Zratey = 323147727779397632
Zayonne = 328217366368616448



class MyClient(discord.Client):
    

    async def on_ready(self):
        print('Connectée en tant que')
        print(self.user.name)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="dans les yeux celui qui lis ce message 👀"))


    

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("/e"):
            await message.channel.send("Réponds moi par 'E'")
            msg = await client.wait_for("message")
            await message.channel.send("Ok {}!".format(msg.author.id))

        #exemple test emoji
        if message.content == ":raykaza:":
            await message.channel.purge(limit=1)
            await message.channel.send("<a:raykaza:828323793629216831>")
        
        if message.content.startswith("/gamemode 1"):
            await message.channel.send("Cheater")
        
        #Commande 8 ball
        if message.content.startswith('/8ball'):
            ball = randint(1, 8)
            if ball == 1:
                await message.channel.send("Yes")
            elif ball == 2:
                await message.channel.send("Peut être")
            elif ball == 3:
                await message.channel.send("Evidemment")
            elif ball == 4:
                await message.channel.send("Non")
            elif ball == 5:
                await message.channel.send("T'as cru ?")
            elif ball == 6:
                await message.channel.send("Demande à quelqu'un d'autre peut être")
            elif ball == 7:
                await message.channel.send("Selon mes renseignements, Non {0.author.mention}".format(message))
            elif ball == 8:
                await message.channel.send("C'est compliqué...")
                sleep(5)
                await message.channel.send("Un peu débile comme question non ?")
            else:
                await message.channel.send("<@!323147727779397632> Erreur 8ball")
        
        #Commandes ping
        if message.content.startswith("/ping"):
          await message.channel.send(f"Pong! J'ai un ping de {round(self.latency * 1000)}ms")
        
        #retourne la photo de profile de l'utilisateur
        if message.content.startswith("/pdp"):
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.add_field(name="Commande réalisée par {}".format(message.author), value="Voici votre photo de profile", inline=False)
            embedVar.set_image(url="{}".format(message.author.avatar_url))
            await message.channel.send(embed=embedVar)
        
        #Search definition on Urban Dictionary
        if message.content.startswith("/def"):
            txt = message.content
            txt = txt[5:]
            txt2 =""
            for x in txt:
                if x == " ":
                    txt2=txt2+"_"
                else:
                    txt2=txt2+x
            await message.channel.send("https://www.urbandictionary.com/define.php?term={}".format(txt2))
            await message.channel.send("Si rien ne s'affiche, cela veux dire que ce que vous avez recherché n'existe pas sur Urban Dictionay. Essayez une simple recherche internet avec ``/google``")
        
        #Quick Search on Google
        if message.content.startswith("/google"):
            txt = message.content
            txt = txt[8:]
            txt2 =""
            for x in txt:
                if x == " ":
                    txt2=txt2+"_"
                else:
                    txt2=txt2+x
            await message.channel.send("Voilà le résultat de votre recherche via le moteur de recherche Google : https://www.google.com/search?q={}".format(txt2))
            await message.channel.send("Peut être que la définition de ce que vous cherchez est sur Urban Dictionay ? Essayez la commande ``/def``")
        
        #Quick Search on Wiki
        if message.content.startswith("/wiki"):
            txt = message.content
            txt = txt[6:]
            txt2 =""
            for x in txt:
                if x == " ":
                    txt2=txt2+"_"
                else:
                    txt2=txt2+x
            await message.channel.send("Voilà le résultat de votre recherche via Wikipédia : https://fr.wikipedia.org/w/index.php?search={}".format(txt2))
            await message.channel.send("Si rien ne s'affiche, cela veux dire que ce que vous avez recherché n'existe pas sur Wikipédia. Essayez une simple recherche internet avec ``/google``")
        
        #Commande pour montrer le profile de l'utilisateur
        if message.content.startswith("/profile"):
            embedVar = discord.Embed(color=discord.Color.blue())
            embedVar.set_author(name="Profile de {}".format(message.author), icon_url="{}".format(message.author.avatar_url))
            embedVar.add_field(name="Identifiant Discord", value="{}".format(message.author.id), inline=False)
            if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}wallet.txt"):
                filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                for x in filemoney:
                    bank=x
                filemoney.close()
                embedVar.add_field(name="Money en banque", value="{}<:coquillette:802972160364249119>".format(bank), inline=True)
            else:
                embedVar.add_field(name="Money en banque", value="Compte en banque inexistant", inline=True)
            
            filexp = open(f"E:\\Véronica\\xpdata\\lvl{message.author.id}.txt", "r")
            for x in filexp:
                lvlxp = x
            filexp.close()
            embedVar.add_field(name="Niveau d'experience", value="Niveau {}".format(lvlxp), inline=True)
            date=message.author.created_at
            date=time.strftime("%D à %H:%M")
            embedVar.add_field(name="Date de création du compte Discord", value="{}".format(date), inline=True)
            date=message.author.joined_at
            date=time.strftime("%D à %H:%M")
            embedVar.add_field(name="Date où vous avez rejoint ce serveur", value="{}".format(date), inline=True)
            embedVar.add_field(name="Role principal", value="{}".format(message.author.top_role.mention), inline=True)
            listperso=["Mario", "Donkey Kong", "Link", "Samus Aran", "Yoshi", "Kirby", "Fox", "Pikachu"]
            if os.path.exists(f"E:\\Véronica\\smash\\users\\{message.author.id}.txt"):
                filecharac = open(f"E:\\Véronica\\smash\\users\\main{message.author.id}.txt", "r")
                for x in filecharac:
                    main = x
                filecharac.close()
                embedVar.add_field(name="Main", value="{}".format(listperso[int(main)-1]), inline=False)
                filecharac = open(f"E:\\Véronica\\smash\\characters\\img_ressources.txt", "r")
                for ligne in filecharac:
                    if ligne[0:2] == main:
                        url_img_link=ligne[2:]
                        break
                filecharac.close()
                embedVar.set_image(url="{}".format(url_img_link))
            else:
                embedVar.add_field(name="Main", value="Aucun main", inline=False)
            await message.channel.send(embed=embedVar)
        
        
        ###################################################################################################
        #                                               XP                                                #
        ###################################################################################################

        
        if message.content == "/rank":
            if os.path.exists(f"E:\\Véronica\\xpdata\\lvl{message.author.id}.txt"):
                filexp = open(f"E:\\Véronica\\xpdata\\lvl{message.author.id}.txt", "r")
                for x in filexp:
                    lvlxp = x
                filexp.close()

                await message.channel.send("<@!{}>, Vous êtes actuellement lvl {} !".format(message.author.id, lvlxp))
            else:
                await message.channel.send("Hmm ? Je suis désolé, mais il semblerait que je ne trouve pas votre niveau dans ma base de donnée. Essayez de voir avec <@!323147727779397632> ce qu'il ne va pas.")
            
        if message.content.startswith(""):
            bannedchannel=0
            noxp = open(f"E:\\Véronica\\xpdata\\noxpchannel.txt", "r")
            for ligne in noxp:
                if message.channel.id == int(ligne):
                    bannedchannel=1
            noxp.close()
                
            if bannedchannel==0:
                if os.path.exists(f"E:\\Véronica\\xpdata\\{message.author.id}.txt"):
                    filexp = open(f"E:\\Véronica\\xpdata\\{message.author.id}.txt", "r")
                    for x in filexp:
                        lastxp = int(x)
                    filexp.close()

                    filexp = open(f"E:\\Véronica\\xpdata\\{message.author.id}.txt", "w")
                    lastxp = randint(5,20)+lastxp
                    filexp.write(f"{lastxp}")
                    filexp.close()
                
                    #lvl up
                    filexp = open(f"E:\\Véronica\\xpdata\\lvl{message.author.id}.txt", "r")
                    for x in filexp:
                        lvl = int(x)
                    filexp.close()

                    filexp = open(f"E:\\Véronica\\xpdata\\lvl{message.author.id}.txt", "w")
                    filexp.write(f"{lvl}")
                    filexp.close()

                    filexp = open(f"E:\\Véronica\\xpdata\\lvl.txt", "r")
                    requirexp = 0
                    lvlup = 0
                    for ligne in filexp:
                        if lvl >= 10:
                            requirexp=int(ligne[2:])
                        else:
                            if ligne[1] == " ":
                                requirexp=int(ligne[1:])
                    

                        if int(ligne[0]) == lvl:
                            if lastxp >= requirexp:
                                lvlup = 1
                    filexp.close()
                    if lvlup==1:
                        filexp = open(f"E:\\Véronica\\xpdata\\lvl{message.author.id}.txt", "w")
                        filexp.write(f"{lvl+1}")
                        filexp.close()
                        await message.channel.send("Félicitations <@!{}> ! Vous êtes passé au niveau {} !".format(message.author.id, lvl+1))
                        print("{} lvl up".format(message.author.id))
                        filexp = open(f"E:\\Véronica\\xpdata\\{message.author.id}.txt", "w")
                        filexp.write("0")
                        filexp.close()
                        lvlup=0
                        

                else:
                    filexp = open(f"E:\\Véronica\\xpdata\\{message.author.id}.txt", "w")
                    filexp.write("{}".format(randint(15,25)))
                    filexp.close()

                    filexp = open(f"E:\\Véronica\\xpdata\\lvl{message.author.id}.txt", "w")
                    filexp.write("0")
                        
            bannedchannel=0
        
        ###################################################################################################
        #                                            MONEY                                                #
        ###################################################################################################

        #roulette
        if message.content.startswith("/spin"):
            if message.channel.id == 397367943769358338:
                if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}wallet.txt"):
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                    for x in filemoney:
                        current_money=int(x)
                    filemoney.close()

                    txt = message.content
                    check_int=txt[6:]
                    validcommand = 0
                    for x in check_int:
                        if x != "0" and x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8" and x != "9":
                            validcommand = 1
                    
                    if len(txt[6:]) != 0 and validcommand==0:
                        moneymiser = int(txt[6:])
                        #La monaie qui sera misée pour la commande
                    else:
                        moneymiser = 30
                        #La monnaire misée malgré le fait qu'aucune valeur ne soit entrée

                    randomspin = randint(0,100)
                    if len(txt) == 5 or len(txt) == 6:
                        txt=txt+"0"
                    
                    if len(txt) == 0:
                        await message.channel.send("Veuillez insérer une valeur après la commande")
                    else:
                        if current_money-moneymiser > 0 and validcommand==0 :
                            if int(txt[-1:]) == 0 or moneymiser == 30:
                                if randomspin >= 0 and randomspin <= 3:
                                    moneymiser = moneymiser * 2
                                    current_money = current_money + moneymiser
                                    await message.channel.send("Félicitations <@!{}> ! Vous avez doublé votre valeur misée ! 🎉".format(message.author.id))
                                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(current_money))
                                    filemoney.close()
                                elif randomspin > 3 and randomspin <= 8:
                                    current_money = current_money - moneymiser
                                    await message.channel.send("Quel dommages <@!{}> ! Vous avez perdu toute votre valeur misée... <:marre:692645274631536680>".format(message.author.id))
                                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(current_money))
                                    filemoney.close()
                                elif randomspin > 8 and randomspin <= 17:
                                    current_money = current_money - moneymiser
                                    moneymiser = round(moneymiser * 0.25)
                                    current_money = current_money + moneymiser
                                    await message.channel.send("<@!{}> Vous avez reçu **{}**<:coquillette:802972160364249119> de ce que vous aviez misé de base".format(message.author.id, moneymiser))
                                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(current_money))
                                    filemoney.close()
                                elif randomspin > 17 and randomspin <= 50:
                                    current_money = current_money - moneymiser
                                    moneymiser = round(moneymiser * 0.5)
                                    current_money = current_money + moneymiser
                                    await message.channel.send("<@!{}> Vous avez reçu **{}**<:coquillette:802972160364249119> de ce que vous aviez misé de base".format(message.author.id, moneymiser))
                                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(current_money))
                                    filemoney.close()
                                elif randomspin > 50 and randomspin <= 75:
                                    current_money = current_money - moneymiser
                                    moneymiser = round(moneymiser * 0.75)
                                    current_money = current_money + moneymiser
                                    await message.channel.send("<@!{}> Vous avez reçu **{}**<:coquillette:802972160364249119> sur ce que vous aviez misé de base".format(message.author.id, moneymiser))
                                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(current_money))
                                    filemoney.close()
                                elif randomspin > 75 and randomspin <= 85:
                                    await message.channel.send("<@!{}> Vous avez reçu **{}**<:coquillette:802972160364249119>, donc vous avez rien perdu. Félicitations je suppose ?".format(message.author.id, moneymiser))
                                elif randomspin > 85 and randomspin <= 100:
                                    current_money = current_money - moneymiser
                                    moneymiser = round(moneymiser * 1.5)
                                    current_money = current_money + moneymiser
                                    await message.channel.send("Félicitations <@!{}> ! Vous avez reçu **{}**<:coquillette:802972160364249119> de ce que vous aviez misé de base".format(message.author.id, moneymiser))
                                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                    filemoney.write("{}".format(current_money))
                                    filemoney.close()
                                else:
                                    await message.channel.send("<@!323147727779397632> problem here")
                            else:
                                await message.channel.send("Veuillez insérer une valeur ronde ( c'est à dire qui fini par 0 )")
                        else:
                            validcommand=0
                            await message.channel.send("Hmmm. Soit vous m'avez pas mis de valeur, soit vous n'avez pas assez d'argent pour miser.")
                else:
                    await message.channel.send("Vous n'avez pas de compte en banque dans ma base de donnée ! Veuillez effectuer la commande ``/money`` pour vous en créer un.")
            else:
                await message.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(message.author.id))


        if message.content == "/daily":
        
            if message.channel.id == 397367943769358338:
                if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}wallet.txt"):
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                    for x in filemoney:
                        current_money=int(x)
                    filemoney.close()

                    if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}dailycooldown.txt"):
                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}dailycooldown.txt", "r")
                        for x in filemoney:
                            past_time=int(x)
                        filemoney.close()
                    else:
                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}dailycooldown.txt", "w")
                        filemoney.write("000000000")
                        filemoney.close()
                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}dailycooldown.txt", "r")
                        for x in filemoney:
                            past_time=int(x)
                        filemoney.close()

                    current_time=calendar.timegm(time.gmtime())
                    zawarudo=int(current_time)-past_time

                    if zawarudo >= 86400:
                        validcommand=1
                    else:
                        validcommand=0
                    
                    if validcommand==1:
                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}dailycooldown.txt", "w")
                        filemoney.write("{}".format(current_time))
                        filemoney.close()

                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                        filemoney.write("{}".format(current_money+50))
                        filemoney.close()
                        await message.channel.send("<@!{}>, vous avez récupéré **50**<:coquillette:802972160364249119> journalier. :white_check_mark:".format(message.author.id))
                        validcommand=0
                    else:
                        await message.channel.send("Calmez vous <@!{}> ! Ce n'est pas encore le temps de réclamer votre récompense journalière !".format(message.author.id))
                    validcommand=0
                
                else:
                    await message.channel.send("Vous n'avez pas de porte-feuille ? Laissez moi en créer un pour vous...")
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                    filemoney.write("200")
                    await message.channel.send("C'est fait ! J'ai ouvert un compte bancaire pour vous ! Vous débutez avec **150** : .")
                    await message.channel.send("Ne vous inquiétez pas, je vous ait bien évidemment ajouté à ces **150**<:coquillette:802972160364249119>, vos **50**<:coquillette:802972160364249119> de la récompense journalière :eyes:")
                    filemoney.close()

                    current_time="{}".format(time.time())
                    current_time=current_time[0:9]
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}dailycooldown.txt", "w")
                    filemoney.write("{}".format(current_time))
                    filemoney.close()
            
            else:
                await message.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(message.author.id))
        

        #lootbox
        if message.content == "/lootbox":
            if message.channel.id == 397367943769358338:
                if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}wallet.txt") and os.path.exists(f"E:\\Véronica\\smash\\"):
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                    for x in filemoney:
                        bank=int(x)
                    filemoney.close()
                    if os.path.exists(f"E:\\Véronica\\money\\lootbox\\{message.author.id}.txt"):
                        filebox = open(f"E:\\Véronica\\money\\lootbox\\{message.author.id}.txt", "r")
                        for x in filebox:
                            amount=int(x)
                        filebox.close()
                    else:
                        filebox = open(f"E:\\Véronica\\money\\lootbox\\{message.author.id}.txt", "w")
                        filebox.write("0")
                        amount=0
                        filebox.close()
                    embedVar = discord.Embed(title="Lootbox menu <:lootbox:828330747416281128>", description="Menu d'intéractions avec le système de Lootbox", color=discord.Color.blue())
                    embedVar.set_author(name="Commande réalisée par {}".format(message.author), icon_url="{}".format(message.author.avatar_url))
                    embedVar.add_field(name="Lootbox en stock", value="{} <:lootbox:828330747416281128>".format(amount), inline=False)
                    embedVar.add_field(name="Liste des commandes pouvant être effectués avec les Lootbox", value="-------------------------------------------------------", inline=False)
                    embedVar.add_field(name="/lootbox info", value="Cette commande vous retourne des informations vous expliquant comment ce système fonctionne", inline=True)
                    embedVar.add_field(name="/lootbox open", value="Cette commande vous permet d'ouvrir des box que vous auriez en stock", inline=True)
                    embedVar.add_field(name="/lootbox rate", value="Cette commande retourna un texte détaillant les pourcentages pour obtenir des présents, ou simplement ce que vous pouvez gagner avec", inline=True)
                    embedVar.add_field(name="/lootbox special rate", value="Cette commande retourna un texte détaillant les pourcentages pour obtenir des présents sur des box spéciales, ou simplement ce que vous pouvez gagner avec", inline=True)
                    embedVar.set_footer(text="Alpha version of Véronica")
                    await message.channel.send(embed=embedVar)
                    response = await client.wait_for("message")
                    if response.channel.id == message.channel.id:
                        if response.author.id == message.author.id:
                            if response.content == "/lootbox open":
                                if amount >= 1:
                                    amount = amount - 1
                                    filebox = open(f"E:\\Véronica\\money\\lootbox\\{message.author.id}.txt", "w")
                                    filebox.write(str(amount))
                                    filebox.close()
                                    loot1=randint(0,100)
                                    loot2=randint(0,100)
                                    print(loot2)
                                    #+250 coquillettes
                                    if loot1 >= 0 and loot1 < 35:
                                        bank=bank+250
                                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                        filemoney.write(str(bank))
                                        filemoney.close()
                                        await message.channel.send("<@!{}> vous avez obtenu **250**<:coquillette:802972160364249119> !".format(message.author.id))
                                    #+500 coquillettes
                                    elif loot1 >= 35 and loot1 < 65:
                                        bank=bank+500
                                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                        filemoney.write(str(bank))
                                        filemoney.close()
                                        await message.channel.send("<@!{}> vous avez obtenu **500**<:coquillette:802972160364249119> !".format(message.author.id))
                                    #+750 coquillettes
                                    elif loot1 >= 65 and loot1 < 85:
                                        bank=bank+750
                                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                        filemoney.write(str(bank))
                                        filemoney.close()
                                        await message.channel.send("<@!{}> vous avez obtenu **750**<:coquillette:802972160364249119> !".format(message.author.id))
                                    #+1k coquillettes
                                    elif loot1 >= 85 and loot1 < 95:
                                        bank=bank+1000
                                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                        filemoney.write(str(bank))
                                        filemoney.close()
                                        await message.channel.send("<@!{}> vous avez obtenu **1000**<:coquillette:802972160364249119> !".format(message.author.id))
                                    #+2k coquillettes
                                    elif loot1 >= 95 and loot1 <= 100:
                                        bank=bank+2000
                                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                        filemoney.write(str(bank))
                                        filemoney.close()
                                        await message.channel.send("<@!{}> vous avez obtenu **2000**<:coquillette:802972160364249119> !".format(message.author.id))
                                    #---LOOT 2---#
                                    #nothing
                                    if loot2 >= 0 and loot2 < 50:
                                        await message.channel.send("<@!{}> pas de chance pour le second loot. Genre littéralement lmfao".format(message.author.id))
                                    #jeton
                                    elif loot2 >= 50 and loot2 < 75:
                                        jeton=0
                                        if os.path.exists(f"E:\\Véronica\\money\\jeton\\{message.author.id}.txt"):
                                            filebox = open(f"E:\\Véronica\\money\\jeton\\{message.author.id}.txt", "r")
                                            for x in filebox:
                                                jeton=int(x)
                                            filebox.close()
                                        filebox = open(f"E:\\Véronica\\money\\jeton\\{message.author.id}.txt", "w")
                                        filebox.write(str(jeton+1))
                                        filebox.close()
                                        await message.channel.send("<@!{}> vous avez obtenu un jeton !".format(message.author.id))
                                    #role flex
                                    elif loot2 >= 75 and loot2 < 85:
                                        role = discord.utils.get(message.author.guild.roles, name="Drip dude")
                                        if role in message.author.roles:
                                            await message.channel.send("<@!{}> vous avez déjà le role Drip dude ! Vous recevez donc **1000**<:coquillette:802972160364249119> à la place".format(message.author.id))
                                            bank=bank+1000
                                            filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                            filemoney.write(str(bank))
                                            filemoney.close()
                                        else:
                                            await message.author.add_roles(role)
                                            await message.channel.send("<@!{}> vous avez obtenu un nouveau role ! Je vous laisse le découvrir par vous même <:Wink:608327025098489863>".format(message.author.id))
                                    #Obtenir une nouvelle lootbox
                                    elif loot2 >= 85 and loot2 < 95:
                                        filebox = open(f"E:\\Véronica\\money\\lootbox\\{message.author.id}.txt", "w")
                                        filebox.write(str(amount+1))
                                        filebox.close()
                                        await message.channel.send("<@!{}> vous avez obtenu une nouvelle box <:lootbox:828330747416281128> !".format(message.author.id))
                                    elif loot2 >= 95 and loot2 < 99:
                                        await message.channel.send("<@!{}> vous êtes normalement censé obtenir une lootbox spéciale <:lootbox:828330747416281128>. Mais mon créateur à la flemme de le coder pour le moment".format(message.author.id))
                                    #perso
                                    elif loot2 == 100:
                                        doublon=0
                                        perso=randint(1,8)
                                        filesmash = open(f"E:\\Véronica\\smash\\users\\{message.author.id}.txt", "r")
                                        had=""
                                        for x in filesmash:
                                            if int(x) == perso:
                                                doublon=1
                                            had=had+x
                                        filesmash.close()
                                        if doublon == 0:
                                            had=had+"\n0{}".format(perso)
                                            filesmash = open(f"E:\\Véronica\\smash\\users\\{message.author.id}.txt", "w")
                                            filesmash.write(had)
                                            filesmash.close()
                                            filesmash = open(f"E:\\Véronica\\smash\\characters\\0{perso}.txt", "r")
                                            listinfo=[]
                                            for x in filesmash:
                                                listinfo.append(x)
                                            filesmash.close()
                                            await message.channel.send("<@!{}> vous avez obtenu **{}** !".format(message.author.id,listinfo[0]))
                                        else:
                                            bank=bank+5000
                                            filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                            filemoney.write(str(bank))
                                            filemoney.close()
                                            await message.channel.send("<@!{}> vous avez obtenu un personnage que vous avez déjà. Donc vous avez obtenu **5000**<:coquillette:802972160364249119> à la place !".format(message.author.id))
                                else:
                                    await message.channel.send("Vous n'avez pas de lootbox à ouvrir")
                            elif response.content == "/lootbox info":
                                filebox = open(f"E:\\Véronica\\money\\lootbox\\info.txt", "r")
                                content=""
                                for i in range(1):
                                    print(filebox[i])
                                filebox.close()
                                embedVar = discord.Embed(title="Lootbox info", description="Informations relatives aux lootbox", color=discord.Color.blue())
                                embedVar.set_author(name="Commande réalisée par {}".format(message.author), icon_url="{}".format(message.author.avatar_url))
                                embedVar.add_field(name="Description", value="{}".format(content), inline=False)
                                embedVar.set_footer(text="Alpha version of Véronica")
                                await message.channel.send(embed=embedVar)
                            elif response.content == "/lootbox rate":
                                await message.channel.send("Mon prochain message sera la liste des pourcentages d'objets que vous pouvez obtenir avec une lootbox")
                                
                                filebox = open(f"E:\\Véronica\\money\\lootbox\\rate_normal.txt", "r")
                                content=""
                                for x in filebox:
                                    content=content+x
                                filebox.close()
                                await message.channel.send(content)
                            elif response.content == "/lootbox special rate":
                                await message.channel.send("Mon prochain message sera la liste des pourcentages d'objets que vous pouvez obtenir avec une lootbox spéciale")
                                filebox = open(f"E:\\Véronica\\money\\lootbox\\rate_speciaux.txt", "r")
                                content=""
                                for x in filebox:
                                    content=content+x
                                filebox.close()
                                await message.channel.send(content)
                            else:
                                await message.channel.send("Soit vous avez mal écrit la commande, soit vous avez pas répondu à ce que j'attendais. Veuillez réessayer avec la commande ``/lootbox``")
                        else:
                            await message.channel.send("Ce n'est pas à vous de répondre <@!{}> ! Veuillez recommencer la commande ``/lootbox`` <@!{}>".format(response.author.id, message.author.id))


                else:
                    await message.channel.send("Vous n'avez pas de compte en banque dans ma base de donnée ! Veuillez effectuer la commande ``/money`` pour vous en créer un. Ou alors vous n'avez pas de starter ! Alors veuillez effectuer la commande ``/starter``")
        #Le shop du système d'économie
        if message.content.startswith("/shop"):
            if message.channel.id==397367943769358338:
                if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}wallet.txt"):
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                    for x in filemoney:
                        bank=int(x)
                    filemoney.close()
                    await message.channel.send("Bienvenue dans le shop ! Veuillez sélectionner quelque chose à acheter en répondant à mon message par le numéro qui correspond à votre achat.")
                    embedVar = discord.Embed(title="Véronica's shop !", description="Le shop de Véronica si vous avez du mal avec l'anglais <:Wink:608327025098489863>", color=discord.Color.blue())
                    embedVar.set_author(name="Commande réalisée par {}".format(message.author), icon_url="{}".format(message.author.avatar_url))
                    embedVar.add_field(name=":one: Rôle DJ", value="Coût : 500<:coquillette:802972160364249119>", inline=True)
                    embedVar.add_field(name=":two: Rôle personnalisé", value="Coût : 15000<:coquillette:802972160364249119>", inline=True)
                    embedVar.add_field(name=":three: Lootbox", value="Coût : 1000<:coquillette:802972160364249119>", inline=True)
                    embedVar.add_field(name="/cancel", value="Vous permet d'annuler la commande", inline=False)
                    embedVar.set_footer(text="Alpha version of Véronica")
                    await message.channel.send(embed=embedVar)
                    while True:
                        response = await client.wait_for("message")
                        if message.channel.id == response.channel.id:
                            if message.author.id == response.author.id:
                                try:
                                    result=int(response.content)
                                    if result >= 1 or result <= 3:
                                        if result == 1:
                                            if bank-500 >= 0:
                                                role = discord.utils.get(message.author.guild.roles, name="DJ")
                                                if role in message.author.roles:
                                                    await message.channel.send("Vous avez déjà le rôle DJ ! Vous ne pouvez pas l'acheter de nouveau")
                                                    break
                                                else:
                                                    bank=bank-500
                                                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                                    filemoney.write("{}".format(bank))
                                                    filemoney.close()
                                                    await message.author.add_roles(role)
                                                    await message.channel.send("Vous avez dépensé **500**<:coquillette:802972160364249119> pour obtenir le rôle DJ !")
                                                    break
                                            else:
                                                await message.channel.send("Désolé, mais vous n'avez pas assez d'argent pour vous acheter ceci")
                                                break
                                        if result == 2:
                                            if bank-15000 >= 0:
                                                bank=bank-15000
                                                filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                                filemoney.write("{}".format(bank))
                                                filemoney.close()
                                                await message.channel.send("Vous avez dépensé **5000**<:coquillette:802972160364249119> pour obtenir l'autorisation d'avoir un rôle personnalisé ! Veuillez contacter un membre du staff en lui montrant mon message afin qu'il puisse le vous créer.")
                                                break
                                            else:
                                                await message.channel.send("Désolé, mais vous n'avez pas assez d'argent pour vous acheter ceci")
                                                break
                                        if result == 3:
                                            if bank-1000 >= 0:
                                                bank=bank-1000
                                                filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                                filemoney.write("{}".format(bank))
                                                filemoney.close()
                                                await message.channel.send("Vous avez dépensé **1000**<:coquillette:802972160364249119> pour obtenir une lootbox ! Pour l'ouvrir, veuillez voir dans le menu dédié avec la commande ``/lootbox``")
                                                amount=0
                                                if os.path.exists(f"E:\\Véronica\\money\\lootbox\\{message.author.id}.txt"):
                                                    filebox = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                                                    for x in filebox:
                                                        amount=int(x)
                                                    filebox.close()
                                                filebox = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                                filebox.write("{}".format(amount+1))
                                                filebox.close()
                                                break
                                            else:
                                                await message.channel.send("Désolé, mais vous n'avez pas assez d'argent pour vous acheter ceci")
                                                break
                                    else:
                                        await message.channel.send("La valeur est incorrecte. Veuillez réessayer")
                                except ValueError:
                                    if response.content.startswith("/cancel"):
                                        await message.channel.send("Commande annulée !")
                                        break
                                    else:
                                        await message.channel.send("Votre réponse n'est pas un chiffre ! Veuillez essayer de nouveau.")
                            else:
                                await message.channel.send("Ce n'est pas à vous de répondre <@!{}> ! S'il vous plaît <@!{}>, veuillez répondre à ce que je vous demande.".format(response.author.id,message.author.id))
                else:
                    await message.channel.send("Vous n'avez pas de compte en banque dans ma base de donnée ! Veuillez effectuer la commande ``/money`` pour vous en créer un.")
            else:
                await message.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(message.author.id))
        
        #Pour ouvrir un compte bancaire 
        if message.content.startswith("/money"):
            if message.channel.id == 397367943769358338:
                if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}wallet.txt"):
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                    for x in filemoney:
                        bank=x
                    filemoney.close()

                    await message.channel.send("Vous avez **{}**<:coquillette:802972160364249119> dans votre compte en banque <@!{}> !".format(bank, message.author.id))
                else:
                    await message.channel.send("Vous n'avez pas de porte-feuille ? Laissez moi en créer un pour vous...")
                    filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                    filemoney.write("150")
                    await message.channel.send("C'est fait ! J'ai ouvert un compte bancaire pour vous ! Vous débutez avec **150**<:coquillette:802972160364249119>.")
                    filemoney.close()
            else:
                await message.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(message.author.id))

        #Système de don    
        if message.content == "/donate":
            if message.channel.id == 397367943769358338:
                txt = message.content
                if txt[:11] == "/donate <@!":
                    if txt[30:31] == " ":
                        validcommand=1
                    else:
                        validcommand=0
                else:
                    validcommand=0
                check_int=txt[31:]
                for x in check_int:
                        if x != "0" and x != "1" and x != "2" and x != "3" and x != "4" and x != "5" and x != "6" and x != "7" and x != "8" and x != "9":
                            validcommand = 0
                
                if validcommand==1:
                    identifient = txt[11:29]
                    value= int(txt[31:])
                    if os.path.exists(f"E:\\Véronica\\money\\{message.author.id}wallet.txt"):
                        filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "r")
                        for x in filemoney:
                            current_money=int(x)
                        filemoney.close()
                    else:
                        await message.channel.send("Vous n'avez pas de compte en banque dans ma base de donnée ! Veuillez effectuer la commande ``/money`` pour vous en créer un.")
                    
                    if current_money-value >= 0:
                        if os.path.exists(f"E:\\Véronica\\money\\{identifient}wallet.txt"):
                            if int(identifient) != message.author.id:
                                filemoney = open(f"E:\\Véronica\\money\\{identifient}wallet.txt", "r")
                                for x in filemoney:
                                    gift_man_money=int(x)
                                filemoney.close()

                                filemoney = open(f"E:\\Véronica\\money\\{message.author.id}wallet.txt", "w")
                                filemoney.write("{}".format(current_money-value))
                                filemoney.close()

                                filemoney = open(f"E:\\Véronica\\money\\{identifient}wallet.txt", "w")
                                filemoney.write("{}".format(gift_man_money+value))
                                filemoney.close()

                                await message.channel.send("Votre don de **{}** <:coquillette:802972160364249119> a été transité avec succès !".format(value))
                            else:
                                await message.channel.send("Bien essayé 😏")
                        else:
                            await message.channel.send("La personne a qui vous vouliez faire une transaction n'a pas de compte en banque ! Demandez lui d'éxecuter la commande ``/money`` pour qu'elle puisse s'en créer un !")
                    else:
                        await message.channel.send("Vous n'avez pas assez d'argent pour effectuer cette transaction.")
                    
                else:
                    await message.channel.send("Syntaxe invalide pour la commande donate ! Voici comment vous devez disposer la commande :")
                    await message.channel.send("``/donate [mention d'une destinataire] [valeur de money qui va être transité]``")
                    await message.channel.send("Suivez l'exemple que je viens d'envoyer juste au dessus. N'oubliez pas de remplacer ce qu'il y a en crochet parce qui est indiqué, ainsi que de ne pas oublier de respecter les espaces !")
            else:
                await message.channel.send("Vous n'avez pas l'autorisation d'effectuer cette commande dans le salon où vous l'avez éxécuté <@!{}>".format(message.author.id))









    
        
    async def tast(self, ctx):
        response = "test success"
        await ctx.send(ctx, response)
    
    

    
        

fileid = open("E:\\Véronica\\id.txt", "r")
client = MyClient()
client.run(fileid.read())