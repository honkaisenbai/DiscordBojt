import nextcord
from nextcord.ext import commands
from nextcord import Colour
import qrcode as qrcode_create
from io import BytesIO


class Qrcode(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def qrcode(self,ctx,*,url=None):
        if url == None:
            embed = nextcord.Embed(title='❌ Không rõ đường dẫn',color=Colour.red())
            await ctx.send(embed=embed,delete_after=3)
        else:
            image_qrcode = qrcode_create.make(url)
            with BytesIO() as a:
                image_qrcode.save(a,scale=8)
                a.seek(0)
                file = nextcord.File(a,'qrcode.png')
                await ctx.send(file=file)

def setup(client):
    client.add_cog(Qrcode(client))
