#main.py
#May.10

import mcstatus
from mcstatus import JavaServer#mc status api
import discord
from discord.ext import commands #discord API
import os
import requests
import json
import sqlite3
import random#加载各种各样的库
from keep_alive import keep_alive#24/7 On

client = commands.Bot(command_prefix='$')

aiurl = "https://api.qingyunke.com/api.php?key=free&appid=0&msg="#$ai的url

@client.listen()#机器人就绪检查
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

      
@client.command()#EMC信息
async def emc(ctx):
  server =  server = JavaServer.lookup("earthmc.net")
  status = server.status()
  onplayers = status.players.online
  embed=discord.Embed(title="EarthMC", description="Information and useful links")
  embed.add_field(name="EarthMC IP", value="earthmc.net", inline=False)
  embed.add_field(name="Version", value="Java 1.17+", inline=False)
  embed.add_field(name="Map(Nova)", value="https://earthmc.net/map/nova/", inline=False)
  embed.add_field(name="Discord", value="https://discord.gg/6rAnxd8", inline=False)
  embed.add_field(name="Support", value="https://discord.gg/mBZAEB8xAD", inline=False)
  embed.add_field(name="Online Players",value="{} players are playing EarthMC!".format(onplayers),inline=False)
  await ctx.send(embed=embed)

  
@client.command()#ping任何服务器
async def mcping(ctx,ip):
  server =  server = JavaServer.lookup(ip)
  status = server.status()
  onplayers = status.players.online
  ping = status.latency
  await ctx.send('{}'.format(ip))
  await ctx.send('Online players:{}'.format(onplayers))
  await ctx.send('Ping:{}'.format(ping))

@client.command()#读取discord ID
async def showmyid(ctx):
  id=ctx.author.id
  mention=ctx.author.mention
  await ctx.send("{},your discord id is {}".format(mention,id))

@client.command()#AI聊天 by Jackyfzh
async def ai(ctx,message):
  rep = requests.get(aiurl+message)
  rep = json.loads(rep.text)
  rep = rep["content"]
  await ctx.send("{}".format(rep))
  
@client.command()#机器人信息
async def info(ctx):
  embed = discord.Embed(title="Help Document", color=0xeee657)
  embed.add_field(name="$emc",value="By using this command, you can check some information about EarthMC server.",inline=False)
  embed.add_field(name="$mcping <Server IP>",value="By using this command, you can get some info about the server you provided. However, the ping may not be accurate because you're not at the same place with the bot.",inline=False)
  embed.add_field(name="$showmyid",value="By using this command, you can get your discord ID conveniently.",inline=False)
  embed.add_field(name="$ai <msg>",value="By using this command, you can chat with an AI. (This command is developed by Jackyfzh.)",inline=False)
  embed.add_field(name="$info",value="By using this command, you can read what you are reading now.",inline=False)
  await ctx.send(embed=embed)



keep_alive()
client.run(os.getenv('TOKEN'))#SET THE TOKEN TO YOURS

