import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Kick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    @commands.guild_only()
    async def kick(self,ctx, member: nextcord.Member=None, *, reason="Không có lý do"):
        guild = ctx.guild
        if member == ctx.author:
            embed = nextcord.Embed(title="❌ Bạn không thể tự đá chính mình!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif member == None:
            embed = nextcord.Embed(title="❌ Không rõ thành viên!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            pura_role:nextcord.Role = nextcord.utils.get(ctx.guild.roles,name='PuraGH')
            if pura_role.position < member.top_role.position:
                embed = nextcord.Embed(title="❌ Tôi không thể đá thành viên này!",description='Vai trò thành viên này cao hơn vai trò của tôi',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                await guild.kick(user=member,reason=f'{ctx.author} đã đá {member} với lý do `{reason}`')
                embed=nextcord.Embed(color=Colour.green(),title=f"""{member} đã bị đá khỏi máy chủ
Lý do: `{reason}`""",timestamp=ctx.message.created_at)
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)
                embed = nextcord.Embed(title=f"""Bạn đã bị đá khỏi máy chủ `{ctx.guild.name}`
Lý do: `{reason}`""")
                await member.send(embed=embed)

def setup(client):
    client.add_cog(Kick(client))
