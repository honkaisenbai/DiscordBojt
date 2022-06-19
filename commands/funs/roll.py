import nextcord
from nextcord.ext import commands
import random


class Roll(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1,5, commands.BucketType.user)
    async def roll(self,ctx):
        await ctx.reply(f'{random.randint(1,100)}')

def setup(client):
    client.add_cog(Roll(client))
