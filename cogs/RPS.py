from discord.ext import commands
import random
import discord


class Rps(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command(aliases=['sps', 'rps', 'Rps'])
	async def Sps(self, ctx, *, user_choice):
		rps_options = ['rock', 'paper', 'scissors']
		bot_choice = random.choice(rps_options)
		if user_choice == None:
			await ctx.send('Choose a value idiot[ex. --rps paper]')
		else:
			embed=discord.Embed(title='Rock Paper Scissor',colour=discord.Colour.blue())
			if bot_choice == user_choice.lower():
				embed.add_field(name=f'I chose {bot_choice}',value='Its a draw!')
			elif bot_choice == 'rock':
				if user_choice.lower() == 'paper':
					embed.add_field(name=f'I chose {bot_choice}',value='You won!')
				elif user_choice.lower() == 'scissors':
					embed.add_field(name=f'I chose {bot_choice}',value='I won!')
			elif bot_choice == 'paper':
				if user_choice.lower() == 'scissors':
					embed.add_field(name=f'I chose {bot_choice}',value='You won!')
				elif user_choice.lower() == 'rock':
					embed.add_field(name=f'I chose {bot_choice}',value='I won!')
			elif bot_choice == 'scissors':
				if user_choice.lower() == 'rock':
					embed.add_field(name=f'I chose {bot_choice}',value='You won!')
				elif user_choice.lower() == 'paper':
					embed.add_field(name=f'I chose {bot_choice}',value='I won!')
			await ctx.send(embed=embed)
				


def setup(client):
    client.add_cog(Rps(client))
