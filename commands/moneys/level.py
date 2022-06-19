import nextcord
from nextcord.ext import commands
from nextcord import Colour
import json


class Level(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def level(self,ctx):
        with open(__file__.replace('commands\moneys\level.py','data\levels.json'),'r',encoding='utf-8') as f:
            levels = json.load(f)
        with open(__file__.replace('commands\moneys\level.py','data\moneys.json'),'r',encoding='utf-8') as f:
            moneys = json.load(f)
        if not levels.get(str(ctx.author.id)):
            levels[str(ctx.author.id)] = {"level":0,"exp":-10}
            with open(__file__.replace('commands\moneys\level.py','data\levels.json'),'w',encoding='utf-8') as f:
                json.dump(levels,f,indent=4)
            if not moneys.get(str(ctx.author.id)):
                moneys[str(ctx.author.id)] = {"moneys":100000}
                with open(__file__.replace('commands\moneys\level.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
        else:
            embed = nextcord.Embed(title=f'Cấp độ - {ctx.author}',color=Colour.blurple())
            embed.add_field(name='Cấp độ',value=f'{levels[str(ctx.author.id)]["level"]} LV',inline=True)
            embed.add_field(name='EXP',value=f'{levels[str(ctx.author.id)]["exp"]:,} EXP',inline=True)
            embed.add_field(name='Tiền',value=f'{moneys[str(ctx.author.id)]["moneys"]:,} PuraCN',inline=True)
            embed.set_thumbnail(url=ctx.author.display_avatar)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Level(client))