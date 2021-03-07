import discord
from discord.ext import commands

class Spam(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command(aliases=['SPAM','Spam'])
	@commands.cooldown(1, 100, commands.BucketType.member)
	async def spam(self,ctx,number = None,*,spam_item = None):
		if ctx.guild.id == 795911343445508107:
			if ctx.author.id == 793433316258480128:
				if spam_item == None and number == None:
					await ctx.send('Command = spam, spam <the number of times u want it to spam>(the thing u want it too spam))')

				elif spam_item != None and number != None:
					if int(number) < 101:
						for spam in range(int(number)):
							await ctx.send(spam_item)

					else:
						await ctx.send('CREATE UR OWN SPAM FOR THAT MUCH!!!')

				else:
					pass
				
			elif ctx.author.id == 569105874912804874:
				if spam_item == None and number == None:
					await ctx.send('Command = spam, spam <the number of times u want it to spam>(the thing u want it too spam))')

				elif spam_item != None and number != None:
					if int(number) < 101:
						for spam in range(int(number)):
							await ctx.send(spam_item)

					else:
						await ctx.send('CREATE UR OWN SPAM FOR THAT MUCH!!!')

				else:
					pass
				
			else:
				await ctx.send('This server is not allowed to spam')
		elif ctx.author.id == 794184456906604575:
			await ctx.send('No spam for u')
		else:
			if spam_item == None and number == None:
				await ctx.send('Command = spam, spam <the number of times u want it to spam>(the thing u want it too spam))')

			elif spam_item != None and number != None:
				if int(number) < 101:
					for spam in range(int(number)):
						await ctx.send(spam_item)

				else:
					await ctx.send('CREATE UR OWN SPAM FOR THAT MUCH!!!')

			else:
				pass
	# @commands.command()	
	# async def stopspam()		
def setup(client):
  client.add_cog(Spam(client))