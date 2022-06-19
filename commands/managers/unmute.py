import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Unmute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True,manage_roles=True)
    @commands.bot_has_permissions(manage_messages=True,manage_roles=True)
    @commands.guild_only()
    async def unmute(self,ctx, member: nextcord.Member=None):
        mutedRole = nextcord.utils.get(ctx.guild.roles, name="Muted")
        if member == ctx.author:
            embed = nextcord.Embed(title="❌ Bạn không thể tự gỡ tắt tiếng chính mình!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif member == None:
            embed = nextcord.Embed(title="❌ Không rõ thành viên!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif mutedRole not in member.roles:
            embed = nextcord.Embed(title='❌ Thành viên này hiện không bị tắt tiếng!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            await member.remove_roles(mutedRole,reason=f'{ctx.author} đã gỡ tắt tiếng {member}')
            embed = nextcord.Embed(color=Colour.green(),title=f"{member} đã được gỡ tắt tiếng",timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            embed = nextcord.Embed(title=f"Bạn đã được gỡ tắt tiếng trong máy chủ `{ctx.guild.name}`",timestamp=ctx.message.created_at,color=Colour.green())
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await member.send(embed=embed)

def setup(client):
    client.add_cog(Unmute(client))
