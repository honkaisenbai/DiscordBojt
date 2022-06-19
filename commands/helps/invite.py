import nextcord
from nextcord.ext import commands
from nextcord import Colour
import json


config = json.load(open(__file__.replace('commands\helps\invite.py','config.json'),'r',encoding='utf-8'))

class Invite(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def invite(self,ctx):
        vote_button = nextcord.ui.Button(style=nextcord.ButtonStyle.link,url='https://top.gg/bot/913700803628384306/vote',label='Vote ;-;')
        view = nextcord.ui.View(timeout=60)
        view.add_item(vote_button)
        embed = nextcord.Embed(title='Đường dẫn thêm bot vào máy chủ',description='Giúp chia sẻ và vote bot luôn được không ;-;?',url=config["invitelink"],color=Colour.random())
        await ctx.send(embed=embed,view=view)

def setup(client):
    client.add_cog(Invite(client))
