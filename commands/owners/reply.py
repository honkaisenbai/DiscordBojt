import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Reply(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def reply(self,ctx,user:nextcord.User=None,*,answer=None):
        if user == None:
            embed = nextcord.Embed(title='❌ Không rõ người dùng!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif answer == None:
            embed = nextcord.Embed(title='❌ Không có trả lời!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            embed = nextcord.Embed(title=f"""Đã gửi trả lời đến {user}
ID: {user.id}""",description=answer,color=Colour.green())
            await user.send(answer)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Reply(client))
