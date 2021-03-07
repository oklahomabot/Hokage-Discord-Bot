import asyncio
import discord
import requests
import wikipedia
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown


class Wiki(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Wiki cog loaded successfully")

    @commands.command(aliases=['search'],description="Shows wikipedia summary")
    async def wiki(self, ctx, *, msg):
        try:
            content = wikipedia.summary(msg, auto_suggest=False, redirect=True)

            embed = discord.Embed(title="Wikipedia", color=0xFF0000)
            chunks = [content[i : i + 1024] for i in range(0, len(content), 2000)]
            for chunk in chunks:
                embed.add_field(name="\u200b", value=chunk, inline=False)
            await ctx.send(embed=embed)
        except:
            await ctx.send("**Failed to get information**")


def setup(client):
    client.add_cog(Wiki(client))