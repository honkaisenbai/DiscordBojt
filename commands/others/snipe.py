import nextcord
from nextcord import Colour
from nextcord.ext import commands
import json


class Snipe(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def snipe(self,ctx):
        with open(__file__.replace('commands\others\snipe.py','data\sniped_messages.json'),'r',encoding='utf-8') as f:
            sniped_messages = json.load(f)
        try:
            sniped_message = sniped_messages[str(ctx.guild.id)][str(ctx.channel.id)]
        except:
            embed = nextcord.Embed(title='❌ Không có tin nhắn nào được lưu!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
            return
        content = sniped_message["content"]
        author = sniped_message["author"]
        time = sniped_message["time"]
        author = ctx.guild.get_member(author)
        embed = nextcord.Embed(title=f"Thời gian: {time}",description=content,color=Colour.green(),timestamp=ctx.message.created_at)
        embed.set_author(name=f'Người gửi: {author}',icon_url=author.display_avatar)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Snipe(client))
