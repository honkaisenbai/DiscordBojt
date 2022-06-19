import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Unban(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    @commands.guild_only()
    async def unban(self,ctx, *, member:nextcord.User=None):
        guild:nextcord.Guild = ctx.guild
        if member == ctx.author:
            embed = nextcord.Embed(title="❌ Bạn không thể tự gỡ cấm chính mình!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif member == None:
            embed = nextcord.Embed(title="❌ Không rõ người dùng!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            await guild.unban(user=member,reason=f'{ctx.author} đã gỡ cấm {member}')
            embed = nextcord.Embed(title=f'{member} đã được gỡ cấm',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Unban(client))
