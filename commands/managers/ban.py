import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Ban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.guild_only()
    async def ban(self,ctx, user: nextcord.User=None, *, reason="Không có lý do"):
        guild:nextcord.Guild = ctx.guild
        if user == ctx.author:
            embed = nextcord.Embed(title="❌ Bạn không thể tự cấm chính mình!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif user == None:
            embed = nextcord.Embed(title="❌ Không rõ người dùng!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            await guild.ban(user,reason=f'{ctx.author} đã cấm {user} với lý do `{reason}`')
            embed = nextcord.Embed(color=Colour.green(),title=f"""{user} đã bị cấm khỏi máy chủ
Lý do: `{reason}`""",timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            embed = nextcord.Embed(title=f"""Bạn đã bị cấm khỏi máy chủ `{ctx.guild.name}
Lý do: `{reason}`""",color=Colour.red(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await user.send(embed=embed)

def setup(client):
    client.add_cog(Ban(client))
