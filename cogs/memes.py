import discord
from discord.ext import commands
import praw
import random



class Memes(commands.Cog):
    def __init__(self, client):
        self.client = client



    @commands.command(aliases=['reddit', 'Meme'], help='sends a random meme')
    async def meme(self, ctx):
        reddit = praw.Reddit(client_id="7Zw29dR_r8yAHA",
                             client_secret="E0Nag3bDaErNio49vcRhStuSN9kI_Q",
                             user_agent="MEME_BOT")

        list_subreddits = ['memes', 'dankmemes', 'funny', 'AdviceAnimals', 'MemeEconomy', 'ComedyCemetry',
                           'PrequelMemes']
        rand_sub = random.randint(0, 6)
        subreddit = reddit.subreddit(list_subreddits[rand_sub])

        category = ['top', 'hot', 'rising', 'new']
        rand_category = random.choice(category)

        top = None
        if rand_category == 'top':
            print('from top')
            top = subreddit.top(limit=15)
        elif rand_category == 'hot':
            print('from hot')
            top = subreddit.hot(limit=10)
        elif rand_category == 'rising':
            print('from rising')
            top = subreddit.rising(limit=20)
        elif rand_category == 'new':
            print('from new')
            top = subreddit.new(limit=15)

        chosen_meme = random.randint(0, 14)
        list_memes = []

        for submission in top:
            if str(submission.url) not in list_memes:
                list_memes.append(submission.url)

        await ctx.send(list_memes[chosen_meme])


def setup(client):
    client.add_cog(Memes(client))
