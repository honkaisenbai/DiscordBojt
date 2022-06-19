import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Request(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1,60, commands.BucketType.user)
    async def request(self,ctx,*,request=None):
        if request == None:
            embed = nextcord.Embed(title='❌ Không có yêu cầu!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            embed = nextcord.Embed(title=f'Đã gửi yêu cầu, hệ thống sẽ xem xét và trả lời nếu có thể',color=Colour.green())
            await ctx.reply(embed=embed,delete_after=3)
            guild = self.client.get_guild(934727632933781535)
            channel = guild.get_channel(949565795841765376)
            embed = nextcord.Embed(title=f'{ctx.author} - {ctx.author.id}',description=request,timestamp=ctx.message.created_at,color=Colour.yellow())
            embed.set_thumbnail(url=ctx.author.display_avatar)
            await channel.send(embed=embed)

def setup(client):
    client.add_cog(Request(client))