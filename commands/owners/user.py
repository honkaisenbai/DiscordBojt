import nextcord
from nextcord.ext import commands
from nextcord import Colour


class User(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def user(self,ctx,*,user:nextcord.User=None):
        if user == None:
            user = ctx.author
        bot_true_false = user.bot
        if bot_true_false == True:
            bot_verify = ":robot: Người máy"
        else:
            bot_verify = ":adult: Người dùng"
        embed = nextcord.Embed(title=f"Thông tin người dùng - {user}",description=user.mention,colour=Colour.blurple(),timestamp=ctx.message.created_at)
        embed.set_thumbnail(url=user.display_avatar)
        embed.add_field(name='Tên',value=user.name,inline=True)
        embed.add_field(name='Tag',value=f'#{user.discriminator}',inline=True)
        embed.add_field(name='ID',value=user.id,inline=True)
        embed.add_field(name='Tạo tài khoản vào ngày',value=user.created_at.strftime("%d/%m/%Y"),inline=True)
        embed.add_field(name='Loại',value=bot_verify,inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(User(client))
