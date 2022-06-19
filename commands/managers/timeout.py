import nextcord
from nextcord.ext import commands
from nextcord import Colour
import humanfriendly
import datetime


class Timeout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    @commands.guild_only()
    async def timeout(self,ctx,member:nextcord.Member=None,time=None,*,reason='Không rõ lý do'):
        try:
            if member == None:
                embed = nextcord.Embed(title='❌ Không rõ thành viên!',color=Colour.red())
                await ctx.reply(embed=embed)
            elif time == None:
                embed = nextcord.Embed(title='❌ Không rõ thời gian!',color=Colour.red())
                await ctx.reply(embed=embed)
            else:
                pura_role:nextcord.Role = nextcord.utils.get(ctx.guild.roles,name='PuraGH')
                if pura_role.position < member.top_role.position:
                    embed = nextcord.Embed(title="❌ Tôi không thể tắt tiếng thành viên này!",description='Vai trò thành viên này cao hơn vai trò của tôi',color=Colour.red())
                    await ctx.reply(embed=embed,delete_after=3)
                else:
                    time = humanfriendly.parse_timespan(time)
                    await member.edit(timeout=nextcord.utils.utcnow()+datetime.timedelta(seconds=time),reason=f'{ctx.author} đã tắt tiếng {member} trong thời gian {round(time)}s với lý do `{reason}`')
                    embed = nextcord.Embed(title=f"""{member} đã bị tắt tiếng
Lý do: `{reason}`
Thời gian: `{round(time)}s`""",color=Colour.green(),timestamp=ctx.message.created_at)
                    embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                    await ctx.send(embed=embed)
                    embed = nextcord.Embed(title=f"""Bạn đã bị tắt tiếng trong máy chủ {ctx.guild.name}
Lý do: `{reason}`
Thời gian: `{round(time)}s`""")
                    await member.send(embed=embed)
        except:
            embed = nextcord.Embed(title='❌ Sai đơn vị thời gian!',color=Colour.red())
            embed.add_field(name='Các đơn vị thời gian',value='1s(1 giây), 1m(1 phút), 1h(1 giờ), 1d(1 ngày)',inline=False)
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Timeout(client))
