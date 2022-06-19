import nextcord
from nextcord.ext import commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def ping(self,ctx):
        await ctx.reply(f'Ping: {round(self.client.latency * 1000)}ms')

def setup(client):
    client.add_cog(Ping(client))
