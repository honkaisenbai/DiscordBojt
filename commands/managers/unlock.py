import nextcord
from nextcord.ext import commands


class Unlock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.guild_only()
    async def unlock(self,ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True,reason=f'{ctx.author} đã mở khóa kênh `{ctx.channel}`')
        await ctx.message.delete()
        await ctx.send(f'{ctx.channel.mention} đã được mở khóa')

def setup(client):
    client.add_cog(Unlock(client))
