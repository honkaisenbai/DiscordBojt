import nextcord
from nextcord.ext import commands
from asyncio import sleep
from nextcord import Colour
import humanfriendly


class Reminder(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def reminder(self,ctx,time=None,*,loinhac="Không có lời nhắc"):
        try:
            if time == None:
                embed = nextcord.Embed(title="❌ Thiếu thời gian!",color=Colour.red())
                embed.add_field(name='Các đơn vị thời gian',value='1s(1 giây), 1m(1 phút), 1h(1 giờ), 1d(1 ngày)',inline=False)
                await ctx.reply(embed=embed,delete_after=3)
            else:
                time = humanfriendly.parse_timespan(time)
                embed = nextcord.Embed(title=f'''Đã hẹn thời gian cho {ctx.author}
Thời gian: `{round(time)}s`
Lời nhắc: `{loinhac}`''',timestamp=ctx.message.created_at,color=Colour.yellow())
                await ctx.send(embed=embed)
                await sleep(time)
                embed = nextcord.Embed(title=f'''{ctx.author}
Thời gian nhắc nhở đã hết!
Lời nhắc: `{loinhac}`''',timestamp=ctx.message.created_at,color=Colour.green())
                await ctx.send(content=ctx.author.mention,embed=embed)
        except:
            embed = nextcord.Embed(title='❌ Sai đơn vị thời gian!',color=Colour.red())
            embed.add_field(name='Các đơn vị thời gian',value='1s(1 giây), 1m(1 phút), 1h(1 giờ), 1d(1 ngày)',inline=False)
            await ctx.reply(embed=embed,delete_after=3)

def setup(client):
    client.add_cog(Reminder(client))
