import nextcord
from nextcord.ext import commands
import requests
from nextcord import Colour
import random


class Meme(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def meme(self,ctx):
        url = requests.get('https://www.reddit.com/r/memes.json')
        memes = url.json()
        random_meme = random.randint(1,25)
        title_meme = memes["data"]["children"][random_meme]["data"]["title"]
        image_url = memes["data"]["children"][random_meme]["data"]["url"]
        embed = nextcord.Embed(title=title_meme,color=Colour.green(),timestamp=ctx.message.created_at)
        embed.set_image(url=image_url)
        embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Meme(client))
