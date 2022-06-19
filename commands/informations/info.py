import nextcord
from nextcord.ext import commands
from nextcord import Colour
import json


config = json.load(open(__file__.replace('commands\informations\info.py','config.json'),'r',encoding='utf-8'))

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def info(self,ctx):
        owner = self.client.get_user(770612800552042508)
        embed = nextcord.Embed(title=f'{self.client.user} - {config["version_bot"]}',description=f'''**Chủ Bot:** `{owner}`
    **Prefix:** `{self.client.command_prefix}`
    **Máy chủ:** `{len(self.client.guilds)} máy chủ`
    **Ping:** `{round(self.client.latency * 1000)}ms`

    [Máy chủ hỗ trợ](https://discord.com/api/oauth2/authorize?client_id={self.client.user.id}&permissions=8&scope=bot "Nhấn để vào máy chủ hỗ trợ của bot\nLưu ý: Nên để bot có Quyền quản lý để đảm bảo bot hoạt động tốt hơn")''',color=Colour.green())
        embed.set_thumbnail(url=self.client.user.avatar)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Info(client))
