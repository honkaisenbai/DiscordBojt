import nextcord
from nextcord.ext import commands


class Lock(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    @commands.bot_has_permissions(manage_channels=True)
    @commands.guild_only()
    async def lock(self,ctx):
        await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False,reason=f'{ctx.author} đã khóa kênh `{ctx.channel}`')
        await ctx.message.delete()
        await ctx.send(f'{ctx.channel.mention} đã được khóa')

def setup(client):
    client.add_cog(Lock(client))
