import discord
from discord.ext import commands

class Admin(commands.Cog):
	def __init__(self,client):
		self.client = client

	@commands.command(aliases=['CLEAR','Clear'])
	@commands.has_permissions(manage_messages=True)
	async def clear(self,ctx, amount : int):
		if amount > 50:
			await ctx.send('Not so much')
		else:
			await ctx.channel.purge(limit= amount+1)

	@commands.command(no_pm=True)
	@commands.has_permissions(manage_roles = True)
	async def removerole(self, ctx, user: discord.Member, role: str):
			'''Removes a role from a user if you have appropriate permissions'''
			roler = discord.utils.find(ctx.guild.roles, name=role)

			if roler is not None:
					try:
							await user.add_roles(roler)
					except discord.Forbidden:
							await ctx.channel.send("You don't have permission to do this.")
			else:
					await ctx.channel.send("I can't remove a nonexistent role.")


	@commands.command(no_pm=True)
	@commands.has_permissions(manage_roles = True)
	async def addrole(self, ctx, user: discord.Member, role: str):
				'''Adds a role to a user if you have appropriate permissions'''
				roler = discord.utils.get(ctx.guild.roles, name=role)

				if roler is not None:
						try:
								await user.add_roles(roler)
						except discord.Forbidden:
								await ctx.channel.send("You don't have permission to do this.")
				else:
						await ctx.channel.send("I can't add a nonexistent role.")


	@commands.command(aliases=['Kick','KICK'])
	@commands.has_permissions(kick_members=True)
	async def kick(self,ctx, member : discord.Member, *, reason=None):
		if ctx.author.id == 797519687147585546:
			await ctx.send ('I will not betray my owner')
		elif member == None:
			await ctx.send('Whom to kick dumb')
		else:
			try:
				await member.kick(reason=reason)
				await ctx.send(f'lol {member.mention} just got kicked')
			except discord.Forbidden:
				await ctx.channel.send("You don't have permission to do this.")


	@commands.command(aliases=['BAN','Ban'])
	@commands.has_permissions(ban_members=True)
	async def ban(self,ctx,member : discord.Member, *, reason=None):
		if ctx.author.id == 797519687147585546:
			await ctx.send ('I will not betray my owner')
		else:
			await member.ban()
			await ctx.send(f'lol {member.mention} just got banned')


	@commands.command(aliases=['UNBAN','Unban'])
	@commands.has_permissions(ban_members=True)
	async def unban(self,ctx, *,member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name,user.discriminator) == (member_name,member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(user + ' has been unbanned')
				return

def setup(client):
  client.add_cog(Admin(client))