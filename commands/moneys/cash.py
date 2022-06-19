import nextcord
from nextcord.ext import commands
import json


class Cash(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cash(self,ctx):
        with open(__file__.replace('commands\moneys\cash.py','data\moneys.json'),'r',encoding='utf-8') as f:
            moneys = json.load(f)
        if not moneys.get(str(ctx.author.id)):
            moneys[str(ctx.author.id)] = {"moneys":100000}
            with open(__file__.replace('commands\moneys\cash.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            await ctx.reply(f'💰 Số tiền hiện tại của bạn: {moneys[str(ctx.author.id)]["moneys"]:,} PuraCN')
        else:
            await ctx.reply(f'💰 Số tiền hiện tại của bạn: {moneys[str(ctx.author.id)]["moneys"]:,} PuraCN')

def setup(client):
    client.add_cog(Cash(client))
