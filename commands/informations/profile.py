import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Profile(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def profile(self,ctx,*,member:nextcord.Member=None):
        if member==None:
            member=ctx.author
        roles = [role for role in member.roles]
        roless = ', '.join([role.mention for role in roles])
        bot_true_false = member.bot
        if bot_true_false == True:
            bot_verify = ":robot: Người máy"
        else:
            bot_verify = ":adult: Người dùng"
        status_member = str(member.status)
        if status_member == 'online':
            status = 'Trực tuyến'
        elif status_member == 'offline':
            status = 'Ngoại tuyến'
        elif status_member == 'dnd':
            status = 'Vui lòng không làm phiền'
        elif status_member == 'idle':
            status = 'Nhàn rỗi'
        embed = nextcord.Embed(title=f"Thông tin người dùng - {member}",description=member.mention,colour=Colour.blurple())
        embed.set_thumbnail(url=member.display_avatar)
        embed.add_field(name='Tên',value=member.name,inline=True)
        embed.add_field(name='Tag',value=f'#{member.discriminator}',inline=True)
        embed.add_field(name='ID',value=member.id,inline=True)
        embed.add_field(name='Tạo tài khoản vào ngày',value=member.created_at.strftime("%d/%m/%Y"),inline=True)
        embed.add_field(name='Tham gia vào ngày',value=member.joined_at.strftime("%d/%m/%Y"),inline=True)
        embed.add_field(name='Vai trò cao nhất',value=member.top_role.mention,inline=False)
        embed.add_field(name=f'Vai trò ({len(roles)})',value=roless,inline=False)
        embed.add_field(name='Loại',value=bot_verify,inline=True)
        embed.add_field(name='Trạng thái',value=status,inline=True)
        embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Profile(client))
