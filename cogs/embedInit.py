from discord import Embed, Member, Color

def embedInit(user: Member, bot) -> Embed:
    """
    Initialise un embed, parce qu'on aime bien la factorisation
    
    user : auteur de la commande
    bot : c'est le bot Discord
    """
    embedVar = Embed(color=Color.blue())
    embedVar.set_footer(text=bot.version,icon_url=f"{bot.user.avatar}")
    embedVar.set_author(name="Commande réalisée par {}".format(user.global_name), icon_url="{}".format(user.avatar))
    return embedVar