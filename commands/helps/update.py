import nextcord
from nextcord.ext import commands


class Update(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def update(self,ctx):
        file = nextcord.File(__file__.replace("commands\helps\\update.py","data\CHANGELOG.md"),spoiler=True)
        await ctx.send(file=file)

def setup(client):
    client.add_cog(Update(client))