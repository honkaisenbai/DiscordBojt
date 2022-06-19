import nextcord
from nextcord.ext import commands
from nextcord import Colour
from asyncio import sleep


class Clear(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True,read_message_history=True)
    @commands.bot_has_permissions(manage_messages=True,read_message_history=True)
    @commands.guild_only()
    async def clear(self,ctx,amount:int=1):
        if amount > 100:
            embed = nextcord.Embed(title='❌ Không thể xóa hơn 100 tin nhắn!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif amount <= 0:
            embed = nextcord.Embed(title='❌ Không thể xóa dưới 0 tin nhắn!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            await ctx.message.delete()
            embed = nextcord.Embed(title=f'Đã xóa {amount} tin nhắn',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.channel.purge(limit=amount)
            await ctx.send(embed=embed,delete_after=3)

def setup(client):
    client.add_cog(Clear(client))
