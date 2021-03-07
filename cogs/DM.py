import discord
from discord.ext import commands

class Dm(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command(aliases=['DM','Dm'])
	async def dm(self,ctx,member:discord.Member=None,*, message = None):
		if member == None:
			await ctx.send('Whom Should I DM? :expressionless:')

		elif message == None:
			await ctx.send('What Should I Send :anger:')

		elif ctx.author == member:
			await ctx.send ('u cant send message to urself')
		
		# elif member == role

		else:
			await member.send(message+'. Sent By '+ctx.author.name+' From '+ctx.author.guild.name)
			await ctx.send('Message Sent :white_check_mark:')


def setup(client):
  client.add_cog(Dm(client))