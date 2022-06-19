import nextcord
from nextcord.ext import commands
from nextcord import Colour
import animec


class Animechar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def animechar(self,ctx,*,query=None):
        try:
            char = animec.Charsearch(query=str(query))
        except:
            embed = nextcord.Embed(title=f'❌ Không thể tìm nhân vật anime với tên `{query}`',color=Colour.red())
            await ctx.reply(embed=embed)
        if query == None:
            embed = nextcord.Embed(title='❌ Thiếu tên nhân vật anime cần tìm!',color=Colour.red())
            await ctx.reply(embed=embed)
        else:
            embed = nextcord.Embed(title=char.title,url=char.url,color=nextcord.Colour.green(),timestamp=ctx.message.created_at)
            embed.set_image(url=char.image_url)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Animechar(client))
