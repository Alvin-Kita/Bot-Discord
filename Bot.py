# Auteur: Alvin KITA
# Date initiale: 4 octobre 2022
# Date de dernière modification
# Version: 1.1
# Description: d'afficher l'emploi du temps de la semaine, et de symplifier les commandes au tacos.
# Peut servir de bonne base pour afficher des messages à la classe ou ne pas avoir à passer par le portail de la classe.

import discord
from discord.ext.commands import Bot
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# ID = int("---ID DU SERVEUR---")  # Mon serveur privé de tests
@client.event
async def on_ready():
    print(f"Bot prêt {client.user} !")

@client.event
async def on_message(message):

    if message.author == client.user:  # <== On evite que le bot réponde à ses propres messages
        return

    if message.content.lower().startswith('!'):

        if message.content.lower().startswith('!aide'):
            await message.channel.send("!carte -> affiche la carte du temple Pizza Pasta")
            await message.channel.send("!eat suivi de ce que tu veux manger au snack -> envoie la commande sur le channel dédié aux commandes")
            await message.channel.send("!temps -> affiche l'emploi du temps")

######## Commande au Tacos et Menu           

        elif message.content.lower().startswith('!carte'):
            await message.channel.send(file=discord.File("picture/menu1.png"))
            await message.channel.send(file=discord.File("picture/menu2.png"))

        elif message.content.lower().startswith('!eat'):
            MVchannel = client.get_channel(int(---ID DU SERVEUR---))  # <==  Le serveur ou envoyer la liste des plats à commander
            #await message.delete()  # <== Supprime le message d'appel, en attentes de test avant de déployer la fonction
            await MVchannel.send('Commande de @{}'.format(message.author.name))
            await MVchannel.send(message.content[4 : ])

######### Emploi du temps

        elif message.content.lower().startswith('!temps'):

            if message.content.lower().startswith('!temps'):
                await message.channel.send("Emploi du temps de la semaine")
                await message.channel.send(file=discord.File("picture/temps.png"))
#########

        else:
            await message.channel.send("Je n'ai pas compris la commande...")
            await message.channel.send("...")
            await message.channel.send("!aide -> Affiche cette liste des commandes")
            await message.channel.send("!carte -> affiche la carte du temple Pizza Pasta")
            await message.channel.send("!eat suivi de ce que tu veux manger au snack -> envoie la commande sur le channel dédié aux commandes")
            await message.channel.send("!temps -> affiche l'emploi du temps")
            


client.run("---CLE DU BOT---")
