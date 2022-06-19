import nextcord
from nextcord import Colour
from nextcord.ext import commands


class Credits(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def credits(self,ctx):
        top_1 = self.client.get_user(770612800552042508)
        embed = nextcord.Embed(title=f"Danh sách những người đóng góp xây dựng bot {self.client.user}",color=Colour.yellow())
        embed.set_author(name=f'Credits')
        embed.add_field(name=f'#1 {top_1}',value='Code bot(Full Bot)',inline=False)
        embed.add_field(name=f'#2 Không có',value="Không có")
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Credits(client))
