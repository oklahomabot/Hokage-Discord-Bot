import discord
from discord.ext import commands

class Ping(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['PING','Ping'])
  async def ping(self,ctx):
    embed=discord.Embed(title='Pong!!!',colour=discord.Colour.blue())
    embed.add_field(name='\u200b',value=f'<:flex:816896077722157076> Bot Latency - {round(self.client.latency * 1000)}ms',inline=True)
    embed.set_footer(text=f'{ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)



  @commands.command(aliases=['INTRODUCTION','Introduction','intro','INTRO','Intro'])
  async def botintro(self,ctx):
    embed=discord.Embed(title='Details about me',description='Hi I am Hokage, I am made by Dr_Gamer. I am a fun bot and hope that u will have fun using me', colour=discord.Colour.blue())
    embed.set_image(url="https://i.pinimg.com/originals/97/ca/07/97ca07c3b59df019c9b27a49cf172ff7.jpg")
    embed.set_footer(text=f'{ctx.author.name}',icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)

  @commands.command(aliases=['memcount','MEM','Mem','MemCount','MEMCOUNT','Memcount'])
  async def mem(self,ctx):
    embed=discord.Embed(title=ctx.guild.name,description=f'There are {ctx.guild.member_count} members in the server',colour=discord.Colour.blue())
    embed.set_footer(text=f'{ctx.author.name}',icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)


def setup(client):
  client.add_cog(Ping(client))