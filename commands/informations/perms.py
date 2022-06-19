import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Perms(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def perms(self,ctx):
        embed = nextcord.Embed(title='Các quyền của từng lệnh',description=':exclamation: Lưu ý: Bot cũng cần những quyền của từng lệnh để những lệnh đó hoạt động',color=Colour.yellow())
        embed.add_field(name='Kick',value='`Khai trừ thành viên`',inline=True)
        embed.add_field(name='Ban, Unban',value='`Cấm thành viên`',inline=True)
        embed.add_field(name='Mute, Unmute',value='`Quản lý tin nhắn`,`Quản lý vai trò`',inline=True)
        embed.add_field(name='Clear', value='`Quản lý tin nhắn`,`Xem lịch sử tin nhắn`', inline=True)
        embed.add_field(name='Lock, Unlock',value='`Quản lý kênh`',inline=True)
        embed.add_field(name='Role',value='`Quản lý vai trò`',inline=True)
        embed.add_field(name='Nick',value='`Quản lý biệt danh`',inline=True)
        embed.add_field(name='Badwords',value='`Quản lý tin nhắn`',inline=True)
        embed.add_field(name='Timeout, Untimeout',value='`Hạn chế thành viên`',inline=True)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Perms(client))
