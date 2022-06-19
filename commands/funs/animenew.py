import nextcord
from nextcord.ext import commands
from nextcord import Colour
import animec


class Animenew(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def animenew(self,ctx):
        news = animec.Aninews()
        links = news.links
        titles = news.titles
        embed = nextcord.Embed(title=f'{titles[0]}',description=f'[Thông tin]({links[0]} "Dẫn bạn đến web thông tin về anime")',color=Colour.green())
        embed.set_image(url=news.images[0])
        embed.set_author(name='Anime mới nhất')
        embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Animenew(client))
