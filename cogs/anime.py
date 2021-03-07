import discord
from discord.ext import commands

class Admin(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command()
	async def naruto(self,ctx):
		embed=discord.Embed(title='Naruto Uzumaki',colour = discord.Colour.blue())
		embed.add_field(name='```Info...```',value="Naruto Uzumaki is a fictional character in the manga and anime franchise Naruto, created by Masashi Kishimoto. Serving as the eponymous protagonist of the series, he is a young ninja from the fictional village of Konohagakure (Hidden Leaf Village). The villagers ridicule Naruto on account of the Nine-Tailed Demon Fox—a malevolent creature that attacked Konohagakure—that was sealed away in Naruto's body. Despite this, he aspires to become his village's leader, the Hokage in order to receive their approval.")
		embed.add_field(name='```More...```',value=" His carefree, optimistic and boisterous personality enables him to befriend other Konohagakure ninja, as well as ninja from other villages. Naruto appears in the series' films and in other media related to the franchise, including video games and original video animations.",inline=False)
		embed.set_image(url = 'https://static.wikia.nocookie.net/naruto/images/d/dd/Naruto_Uzumaki%21%21.png/revision/latest?cb=20161013233552')
		await ctx.send(embed=embed)# ya u can but u had to end the embed.add_field( ) one also" u forgot to end a parenthesis
	
	
	@commands.command()
	async def boruto(self,ctx):
		embed=discord.Embed(title='Boruto Uzumaki',colour = discord.Colour.blue())
		embed.add_field(name='```Info...```',value="Boruto Uzumaki (Japanese: うずまき ボルト, Hepburn: Uzumaki Boruto), originally spelled by Viz Media as 'Bolt',[1] is a fictional character created by manga author Masashi Kishimoto who first appears in the finale of the manga series Naruto as the son of the protagonist Naruto Uzumaki and Hinata Uzumaki. He later appears as the main protagonist in the 2015 anime film Boruto: Naruto the Movie where he is training as a ninja to surpass his father, the leader of the ninja village Konohagakure and also being mentored by his father's best friend, Sasuke Uchiha. Boruto also serves as a protagonist in the manga and anime series Boruto: Naruto Next Generations. In the manga, it starts off with the retelling of the Boruto film, while the anime begins with his childhood in the ninja academy where he meets his future teammates—Sarada Uchiha and Mitsuki—as well as his teacher, Konohamaru Sarutobi.")#wait lemme see why

		await ctx.send(embed=embed)

	@commands.command()
	async def sasuke(self,ctx):
		embed=discord.Embed(title='Sasuke Uchiha',colour = discord.Colour.blue())
		embed.add_field(name='```Info...```',value="Sasuke Uchiha (Japanese: うちは サスケ, Hepburn: Uchiha Sasuke) (/ˈsɑːskeɪ/) is a fictional character in the Naruto manga and anime franchise created by Masashi Kishimoto. Sasuke belongs to the Uchiha clan, a notorious ninja family, and one of the most powerful, allied with Konohagakure (木ノ葉隠れの里, English version: 'Hidden Leaf Village'). Most of its members were massacred by Sasuke's older brother, Itachi Uchiha, before the series began, leaving Sasuke one of the few living. Despite becoming empathetic toward his teammates Naruto Uzumaki and Sakura Haruno, Sasuke's feelings of powerlessness force him to abandon his friends and his home in his quest to become stronger, and to find Orochimaru.")
		embed.add_field(name='```More...```',value="Sasuke appears in several of the series' animated feature films and related media, including video games, original video animations (OVAs), and Boruto: Naruto the Movie (2015) and its manga sequel, Boruto: Naruto Next Generations (2016), in which he is depicted as a vigilante supporting his village and a mentor to Naruto's son Boruto Uzumaki.",inline=False)
		await ctx.send(embed=embed)

	@commands.command(aliases=['GAARA','Gaara'])
	async def gaara(self,ctx):
		embed=discord.Embed(title='GAARA',colour = discord.Colour.blue())
		embed.add_field(name='```Info...```',value="Gaara (我愛羅) is a fictional character in the Naruto manga and anime series created by Masashi Kishimoto. Originally debuting as an antagonist, Gaara is a shinobi affiliated with Sunagakure and is the son of Sunagakure's leader, the Fourth Kazekage. He was born as a demon's host as part of his father's intention to have a weapon to restore their village. However, a combination of being ostracized by the Sunagakure villagers, his early inability to control the Tailed Beast, and the notion that his deceased mother called him her curse on the village caused Gaara to become a ruthless killer who believes his own purpose is to kill his enemies. ")
		embed.add_field(name='```More...```',value="Gaara was created a foil to the series' eponymous character, Naruto Uzumaki, as the two were born through similar circumstances, but develop vastly different personalities due to a troubled upbringing. His designs and name underwent major changes in the making of his final one which also was modified in later arcs to give Gaara a design that is easier to draw.",inline=False)

		embed.set_image(url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQR3XWDTzsVVZjDn1TaSQsPitUotvJZjNy7Ag&usqp=CAU')


		await ctx.send(embed=embed)

def setup(client):
  client.add_cog(Admin(client))