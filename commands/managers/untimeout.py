import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Untimeout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    @commands.guild_only()
    async def untimeout(self,ctx,*,member:nextcord.Member=None):
        if member == None:
            embed = nextcord.Embed(title='❌ Không rõ thành viên!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            await member.edit(timeout=None,reason=f'{ctx.author} đã gỡ tắt tiếng {member}')
            embed = nextcord.Embed(title=f'Đã gỡ tắt tiếng cho {member}',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            embed = nextcord.Embed(title=f'Bạn đã được gỡ tắt tiếng trong máy chủ {ctx.guild.name}',timestamp=ctx.message.created_at,color=Colour.green())
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await member.send(embed=embed)

def setup(client):
    client.add_cog(Untimeout(client))
