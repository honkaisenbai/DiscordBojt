import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Nick(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_nicknames=True)
    @commands.bot_has_permissions(manage_nicknames=True)
    @commands.guild_only()
    async def nick(self,ctx,member:nextcord.Member=None,*,nick=None):
        if member == None:
            embed = nextcord.Embed(title="❌ Không rõ người dùng!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif nick == None:
            pura_role:nextcord.Role = nextcord.utils.get(ctx.guild.roles,name='PuraGH')
            if pura_role.position < member.top_role.position:
                embed = nextcord.Embed(title="❌ Tôi không thể đổi biệt danh thành viên này!",description='Vai trò thành viên này cao hơn vai trò của tôi',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                await member.edit(nick=member.name,reason=f'{ctx.author} đã thay đổi biệt danh của {member} là `{member.name}`')
                embed = nextcord.Embed(title=f'Đã thay đổi biệt danh của {member} là `{member.name}`',color=Colour.red(),timestamp=ctx.message.created_at)
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)
        elif len(nick) > 32:
            embed = nextcord.Embed(title='❌ Biệt danh không được vượt quá 32 ký tự!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            pura_role:nextcord.Role = nextcord.utils.get(ctx.guild.roles,name='PuraGH')
            if pura_role.position < member.top_role.position:
                embed = nextcord.Embed(title="❌ Tôi không thể đổi biệt danh thành viên này!",description='Vai trò thành viên này cao hơn vai trò của tôi',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                await member.edit(nick=nick,reason=f'{ctx.author} đã thay đổi biệt danh của {member} là `{nick}`')
                embed = nextcord.Embed(title=f'Đã thay đổi biệt danh của {member} là `{nick}`',color=Colour.red(),timestamp=ctx.message.created_at)
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Nick(client))
