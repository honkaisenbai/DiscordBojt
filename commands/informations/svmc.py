import nextcord
from nextcord.ext import commands
from nextcord import Colour
import requests


class Svmc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def svmc(self,ctx, *, ipServer = None):
        if ipServer == None:
            embed=nextcord.Embed(title="❌ Thiếu ip máy chủ minecraft", color=Colour.red)
            await ctx.reply(embed=embed,delete_after=3)
        else:
            url = f'https://api.mcsrvstat.us/2/{ipServer}'
            icon_url = f'https://api.mcsrvstat.us/icon/{ipServer}'
            try:
                stats = requests.get(url)
                json_stats = stats.json()
                port = json_stats["port"]
                max_players = json_stats["players"]["max"]
                online_players = json_stats["players"]["online"]
                version = json_stats["version"]
                hostname = json_stats["hostname"]
            except:
                embed = nextcord.Embed(title="❌ Không rõ ip máy chủ hoặc máy chủ không tồn tại!", color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            embed = nextcord.Embed(title=f'Thông tin máy chủ minecraft {hostname}:{port}',color=Colour.blurple(),timestamp=ctx.message.created_at)
            embed.add_field(name="Tên máy chủ",value=hostname,inline=True)
            embed.add_field(name="Port",value=port,inline=True)
            embed.add_field(name="Số lượng người trực tuyến",value=online_players,inline=False)
            embed.add_field(name="Giới hạn người chơi",value=max_players,inline=True)
            embed.add_field(name="Phiên bản",value=version,inline=True)
            embed.set_thumbnail(url=icon_url)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Svmc(client))
