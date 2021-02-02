##############################################
# DISCORD BOT = " John Doe Cyber Bot "      #
# Développeur : https://github.com/Haisenberg#
##############################################
import discord
##############################################
import discord.ext
##############################################
from discord import role
##############################################              
from discord.ext import commands, tasks
##############################################
import json
##############################################
from discord.utils import get
##############################################
import re
##############################################
import random  
##############################################
import os
##############################################
from discord.ext.commands import Bot
##############################################
from itertools import cycle
##############################################                                     
from urllib import parse, request
##############################################
from datetime import datetime, timedelta
##############################################
import asyncio
##############################################
from time import sleep
##############################################
from discord.voice_client import VoiceClient
##############################################
from discord import FFmpegPCMAudio
##############################################
from os import system
##############################################
import youtube_dl
##############################################
import requests
##############################################
from discord import Activity, ActivityType
##############################################
import pyfiglet
##############################################
import socket
##############################################
import re
##############################################
import sys
##############################################
from requests import get
##############################################
import bs4
##############################################
from bs4 import BeautifulSoup
##############################################
import hashlib 
##############################################
import base64
##############################################
import datetime
##############################################
import safygiphy
##############################################
import urllib.request
##############################################
from urllib.request import Request, urlopen
##############################################
import io
##############################################
import string
##############################################

##############################################
ascii_banner = pyfiglet.figlet_format("John Doe")
print(ascii_banner)
##############################################

#############################################################################
TOKEN = '' #TOKEN
bot = commands.Bot(command_prefix ="$") #PREFIX
bot.remove_command('help')
client = discord.Client() 
#############################################################################

########################################################################################################################
@bot.event
async def on_ready():
    print("\033[42mJohn Doe es en ligne...\033[42m")
    await bot.change_presence(activity=Activity(name=f"{len(bot.guilds)} serveurs | $help",type=ActivityType.watching))
########################################################################################################################

########################################################################################################################
@bot.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(title="Panel d'aide", color=0x00ff00)
    embed.set_author(name="")
    embed.add_field(name='***$admin***', value='Administrateur', inline=True)
    embed.add_field(name='***$mod***',value='Modération', inline=True)
    embed.add_field(name='***$tool***',value='Boite à outils', inline=True)
    await ctx.send("https://64.media.tumblr.com/0870408ef69639327475f93f665ac490/5c7bd8bcc33b5478-02/s500x750/ee4ec4c470d99ab8460c749465e887e34373caae.gif")
    await ctx.send(embed=embed)
########################################################################################################################
@bot.command(pass_context=True)
async def admin(ctx):
    embed = discord.Embed(title="", color=0x00ff00)
    embed.set_author(name="")
    embed.add_field(name='***$admin***', value='Commande Administrateur', inline=True)
    embed.add_field(name='***$clear [number]***', value='Supprimer des messages en masse', inline=True)
    embed.add_field(name='***$pseudo [user]***', value='Modifier un pseudonyme', inline=True)

    await ctx.send(embed=embed)
########################################################################################################################
@bot.command(pass_context=True)
async def mod(ctx):
    embed = discord.Embed(title="", color=0x00ff00)
    embed.set_author(name="")
    embed.add_field(name='***$warn [@user]***', value='Warn un utilisateur', inline=True)
    embed.add_field(name='***$kick [@user]***', value='Exclure un utilisateur', inline=True) 
    embed.add_field(name='***$ban [@user]***', value='Bannir un utilisateur', inline=True) 
    embed.add_field(name='***$unban [@user]***', value='Debannir un utilisateur', inline=True) 
    embed.add_field(name='***$mute [@user]***', value='Mute un utilisateur', inline=True) 
    embed.add_field(name='***$unmute [@user]***', value='Demute un utilisateur', inline=True) 

    await ctx.send(embed=embed)
########################################################################################################################
@bot.command(pass_context=True)
async def tool(ctx):
    embed = discord.Embed(title="", color=0x00ff00)
    embed.set_author(name="")
    embed.add_field(name='***$wiki [text]***',value='Faire une recherche Wikipedia', inline=True)
    embed.add_field(name='***$minecraft [pseudonyme]***', value='Recuperer des informations sur un compte MC', inline=True)
    embed.add_field(name='***$geoip [0.0.0.0]***',value='Geolocaliser une adresse IP', inline=True)
    embed.add_field(name='***$nmap [0.0.0.0] ou [URL]***',value='Analyse NMAP', inline=True)
    embed.add_field(name='***$md5 [text]***',value='Hashing MD5', inline=True)
    embed.add_field(name='***$sha256 [text]***',value='Hashing SHA256', inline=True)
    embed.add_field(name='***$sha512 [text]***',value='Hashing SHA512', inline=True)
    embed.add_field(name='***$pp [@user]***', value='Obtenir un avatar', inline=True)
    embed.add_field(name='***$myid***', value='Obtenir votre ID', inline=True)
    embed.add_field(name='***$info***',value='Information du serveur', inline=True)
    embed.add_field(name='***$userinfo [@User]***',value='Information sur un utilisateur', inline=True)
    embed.add_field(name='***$usercounter***', value='Indique le nombre de utilisateur sur le serveur', inline=True)
    embed.add_field(name='***$invitation***', value='Inviter John Doe à boire un café sur votre serveur', inline=True)

    await ctx.send(embed=embed)
########################################################################################################################
########################################################################################################################   / Nouvelle Catégorie
########################################################################################################################

#########################################
#               CLEAR                   #
######################################### 
@bot.command()
@commands.has_permissions(administrator=True)
async def clear(context, amount = 2):
    await context.channel.purge(limit = amount)
    await context.send(f'***{amount-1} messages on été supprimé.***')

#########################################
#               EDIT PSEUDO             #
######################################### 
@bot.command(pass_context=True) 
@commands.has_guild_permissions(manage_nicknames=True)
async def pseudo(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    await ctx.send(f"{member.name}' à changer sont pseudonyme !**")

########################################################################################################################
########################################################################################################################   / Nouvelle Catégorie
########################################################################################################################

#########################################
#               INVITE                  #
######################################### 
@bot.command()
async def invitation(ctx):
    await ctx.send("Inviter John Doe à boire un café sur ton serveur !")

#########################################
#               WIKIPEDIA               #
######################################### 
@bot.command(helpinfo='Wikipedia summary', aliases=['w', 'wiki'])
async def wikipedia(ctx, *, query: str):
    '''
    RECHERCHE WIKIPEDIA 
    '''
    sea = requests.get(
        ('https://fr.wikipedia.org//w/api.php?action=query'
         '&format=json&list=search&utf8=1&srsearch={}&srlimit=5&srprop='
        ).format(query)).json()['query']

    if sea['searchinfo']['totalhits'] == 0:
        await ctx.send('Désolé, votre recherche n’a pas pu être trouvée.')
    else:
        for x in range(len(sea['search'])):
            article = sea['search'][x]['title']
            req = requests.get('https://fr.wikipedia.org//w/api.php?action=query'
                               '&utf8=1&redirects&format=json&prop=info|images'
                               '&inprop=url&titles={}'.format(article)).json()['query']['pages']
            if str(list(req)[0]) != "-1":
                break
        else:
            await ctx.send('Désolé, votre recherche n’a pas pu être trouvée.')
            return
        article = req[list(req)[0]]['title']
        arturl = req[list(req)[0]]['fullurl']
        artdesc = requests.get('https://fr.wikipedia.org/api/rest_v1/page/summary/'+article).json()['extract']
        lastedited = datetime.datetime.strptime(req[list(req)[0]]['touched'], "%Y-%m-%dT%H:%M:%SZ")
        embed = discord.Embed(title='**'+article+'**', url=arturl, description=artdesc, color=0x3FCAFF)
        embed.set_footer(text='Wiki entry last modified',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.set_author(name='Wikipedia', url='https://fr.wikipedia.org/',
                         icon_url='https://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png')
        embed.timestamp = lastedited
        await ctx.send(':white_check_mark: **Résultat Wikipedia :** ***"{}"***:'.format(query), embed=embed)

#########################################
#               HASH MD5                #
######################################### 
@bot.command()
async def md5(ctx, *, msg :str):
    """Hasher MD5"""
    await ctx.send("`{}`".format(hashlib.md5(bytes(msg.encode("utf-8"))).hexdigest()))\

#########################################
#               HASH SHA256             #
######################################### 
@bot.command()
async def sha256(ctx, *, msg:str):
    """Hasher SHA256"""
    await ctx.send(f"https://i.gzn.jp/img/2020/05/14/sha-256-animation/105.gif")
    await ctx.send("`{}`".format(hashlib.sha256(bytes(msg.encode("utf-8"))).hexdigest()))

#########################################
#               HASH SHA512             #
######################################### 
@bot.command()
async def sha512(ctx, *, msg:str):
    """Hasher SHA512"""
    await ctx.send(f"https://techcrunch.com/wp-content/uploads/2019/01/tracking-phones.gif")
    await ctx.send("`{}`".format(hashlib.sha512(bytes(msg.encode("utf-8"))).hexdigest()))

########################################################################################################################
########################################################################################################################   / Nouvelle Catégorie
########################################################################################################################

#########################################
#               KICK                    #
######################################### 
@bot.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"https://i.giphy.com/media/xTk9ZBWrma4PIC9y4E/giphy.gif")
    await ctx.send(f'***{member.mention} cette utlisateur à été expulser de {ctx.guild.name} !***')

#########################################
#               BAN                     #
######################################### 
@bot.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("***Spécifier le membre !***")
        return
    await member.ban()
    await ctx.send(f"https://i.giphy.com/media/xTk9ZBWrma4PIC9y4E/giphy.gif")
    await ctx.send(f"***Cette utilisateur {member.mention} à été banni de {ctx.guild.name} !***")

#########################################
#                 UNBAN                 #
######################################### 
@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f'{user} à été unban !')
			return
	#Ici on sait que lutilisateur na pas ete trouvé
	await ctx.send(f'Lutilisateur {user} es pas dans la liste des bans !')

#########################################
#               MUTE                    #
######################################### 
@bot.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("***Spécifier le membre !***")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.add_roles(role)
    await ctx.send(f"***Cette utilisateur {member.mention} à été mute !***")

#########################################
#               UNMUTE                  #
######################################### 
@bot.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("***Spécifier le membre !***")
        return
    role = discord.utils.get(ctx.guild.roles, name="muted")
    await member.remove_roles(role)
    await ctx.send(f"***Cette utilisateur {member.mention} à été unmute !***")

#########################################
#                 WARN                  #
######################################### 
@bot.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member : discord.Member, *, reason=None):
    await member.send(f"Vous avez étais warn par {ctx.guild.name} raison : {reason}")
    await ctx.send(f"***{member.mention} à été warn pour : {reason} !***")

########################################################################################################################
########################################################################################################################   / Nouvelle Catégorie
########################################################################################################################

#########################################
#              INFO SERVEUR             #
######################################### 
@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", color=discord.Color.red())
    embed.add_field(name="Serveur créer le", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Fondateur", value=f"{ctx.guild.owner}")
    embed.add_field(name="Région", value=f"{ctx.guild.region}")
    embed.add_field(name="Serveur ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon}")

    await ctx.send(embed=embed)

#########################################
#               USER COUNTER            #
######################################### 
@bot.command()
async def usercounter(ctx, member: discord.Member=None):
    await ctx.send(f"https://em.wattpad.com/9d073ce66a5a80a8756e896d46b1c544f834d7cb/687474703a2f2f7331302e666176696d2e636f6d2f6f7269672f3136313132332f6165737468657469632d616c7465726e61746976652d6172742d636f6d70757465722d466176696d2e636f6d2d343838393730352e676966?s=fit&h=360&w=360&q=80")
    await ctx.send(f"***{ctx.guild.member_count} utilisateurs sur ce serveur !***")

#########################################
#             INVITE COUNTER            #
######################################### 
@bot.command()
async def invites(ctx, member:discord.Member=None):
      if member == None:
          member = ctx.message.author
      totalInvites = 0
      for i in await ctx.guild.invites():
          if i.inviter == member:
              totalInvites += i.uses
      await ctx.send("**" + member.mention + " à inviter `" + str(totalInvites) + "` membres sur `" + str(ctx.guild.name) + "`!**")

#########################################
#               USER INFO               #
######################################### 
@bot.command(pass_context=True)
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member

    embed = discord.Embed(colour = member.colour)
 
 
    embed.set_author(name=f'Information utilisateur =  {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Demander par {ctx.author}', icon_url=ctx.author.avatar_url)
 
    embed.add_field(name='ID :', value=member.id)
    embed.add_field(name='Name :', value=member.display_name)
 
    embed.add_field(name='Créer le :', value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name='A rejoins le serveur le  :', value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
 
    embed.add_field(name='Bot ?', value=member.bot)
    await ctx.send(embed=embed)

#########################################
#              SEND AVATAR              #
######################################### 
@bot.command()
async def pp(ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)

#########################################
#                MY ID                  #
######################################### 
@bot.command(pass_context=True)
async def myid(ctx, member: discord.Member = None):
    await ctx.send(f"***Votre ID =*** {ctx.author.id}")

#########################################
#               IP GEO                  #
######################################### 
@bot.command()
async def geoip(ctx, *, ipadd):
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipadd}')
    geo = r.json()
    IP = geo['query']
    ISP = geo['isp']
    Country = geo['country']
    City = geo['city']
    Region = geo['region']  
    ORG = geo['org']
    em = discord.Embed(description=f"**IP**: {ipadd}\n \n**AdresseIP**: ``{IP}``\n**Ville**: ``{City}``\n**Région**: ``{Region}``\n**Pays**: ``{Country}``\n**ISP**: ``{ISP}``\n**ORG**: ``{ORG}``", color=0x00ff00)
    em.set_thumbnail(url="https://cdn.discordapp.com/attachments/744132540998221864/748121107764084856/51zdsrq20LL.png")
    await ctx.send(f"https://techcrunch.com/wp-content/uploads/2019/01/tracking-phones.gif")
    await ctx.send(embed=em)

#########################################
#                 NMAP                  #
######################################### 
@bot.command()
async def nmap(ctx, arg1):
    scanyuh = get(f"https://api.hackertarget.com/nmap/?q={arg1}")
    result = scanyuh.text.strip(" ( https://nmap.org/ )")
    em = discord.Embed(title=f"NMAP Scanner!", description=f"**{result}**", color=0x00ff00)
    await ctx.send(embed=em)

#########################################
#               MINECRAFT               #
######################################### 
@bot.command(helpinfo='Information du compte MC , Skin & ancien pseudonyme', aliases=['skin', 'mc'])
async def minecraft(ctx, username='Shrek'):
    '''
    Information du compte MC , Skin & ancien pseudonyme
    '''
    uuid = requests.get('https://api.mojang.com/users/profiles/minecraft/{}'
                        .format(username)).json()['id']

    url = json.loads(base64.b64decode(requests.get(
        'https://sessionserver.mojang.com/session/minecraft/profile/{}'
            .format(uuid)).json()['properties'][0]['value'])
                     .decode('utf-8'))['textures']['SKIN']['url']

    names = requests.get('https://api.mojang.com/user/profiles/{}/names'
                         .format(uuid)).json()
    history = "**Historique des anciens pseudonyme :**\n"
    for name in reversed(names):
        history += name['name'] + "\n"

    await ctx.send(':detective: **Pseudonyme : `{}`**\n**Skin : {}**\n**UUID : {}**'.format(username, url, uuid))
    await ctx.send(history)

########################################################################################################################
########################################################################################################################   / Nouvelle Catégorie
########################################################################################################################

#########################################
#            JOIN VOC CHANNEL           #
######################################### 
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

#########################################
#            LEAVE VOC CHANNEL          #
######################################### 
@bot.command(pass_context=True)
async def leave (ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()

bot.run(TOKEN)

