import nextcord
from nextcord.ext import commands
import sys
from asyncio import sleep


class Shutdown(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def shutdown(self,ctx):
        await ctx.send('Đang tắt nguồn bot!',delete_after=3)
        await ctx.message.delete()
        await sleep(3)
        await self.client.close()

def setup(client):
    client.add_cog(Shutdown(client))
