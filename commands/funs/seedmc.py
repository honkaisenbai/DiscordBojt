import nextcord
from nextcord.ext import commands
import random


class Seedmc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def seedmc(self,ctx):
        await ctx.reply(f'Seed: `{random.randint(-999999999999999999,999999999999999999)}`')

def setup(client):
    client.add_cog(Seedmc(client))
