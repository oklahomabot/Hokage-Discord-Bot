import discord
from discord.ext import commands
import random

class eightball(commands.Cog):
  def __init__(self,client):
    self.client = client

  @commands.command(aliases=['8ball','Eightball'])
  async def _8ball(self,ctx, *, question ):
    responses = [ 'It is certain.',
                  'It is decidedly so.',
                  'Without a doubt.',
                  'Yes – definitely.',
                  'You may rely on it.',
                  'As I see it, yes.',
                  'Most likely.',
                  'Outlook good.',
                  'Yes.',
                  'Signs point to yes.',
                  'Reply hazy, try again.',
                  'Ask again later.',
                  'Better not tell you now.',
                  'Cannot predict now.',
                  'Concentrate and ask again.',
                  "Don't count on it.",
                  'My reply is no.',
                  'My sources say no.',
                  'Outlook not so good.',
                  'Very doubtful.']
    answer = random.choice(responses)

    embed = discord.Embed(title='8ball',colour=discord.Colour.blue())
    embed.add_field(name='Question',value=question,inline=False)
    embed.add_field(name='Answer',value=answer,inline=False)
    embed.set_image(url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR-w5VZ0dtWa1kcKH56dOB7GsfQMTAi15Cxjw&usqp=CAU')
    embed.set_footer(icon_url=f'{ctx.author.avatar_url}')
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(eightball(client))    