import nextcord
from nextcord.ext import commands
import random
from nextcord import Colour
from asyncio import sleep
import json


config = json.load(open(__file__.replace('commands\moneys\slots.py','config.json'),'r',encoding='utf-8'))

class Slots(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    @commands.cooldown(1,5,commands.BucketType.user)
    async def slots(self,ctx,amount:int=1):
        with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'r',encoding='utf-8') as f:
            moneys = json.load(f)
        wait = 0.5
        percent = 0.5
        if amount > moneys[str(ctx.author.id)]["moneys"]:
            embed = nextcord.Embed(title='❌ Bạn không đủ tiền để chơi!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif amount <= 0:
            embed = nextcord.Embed(title='❌ Không thể chơi với số tiền dưới 0 PuraCN!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif not moneys.get(str(ctx.author.id)):
            moneys[str(ctx.author.id)] = {"moneys":100000}
            with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            msg = await ctx.reply('🎲 Đang quay')
            await sleep(wait)
            await msg.edit('🎲 Đang quay.')
            await sleep(wait)
            await msg.edit('🎲 Đang quay..')
            await sleep(wait)
            await msg.edit('🎲 Đang quay...')
            await msg.edit('💵 Xin chúc mừng, ...')
            await sleep(2)
            if random.random() < percent:
                await msg.edit(f'💵 Xin chúc mừng, bạn đã nhận được {amount:,} PuraCN {random.choice(config["emojisFun"])}')
                moneys[str(ctx.author.id)]["moneys"] += amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
            else:
                moneys[str(ctx.author.id)]["moneys"] -= amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
                await msg.edit(f'💵 Xin chúc mừng, bạn đã mất hết tiền cược {random.choice(config["emojisSad"])}')
        else:
            msg = await ctx.reply('🎲 Đang quay')
            await sleep(wait)
            await msg.edit('🎲 Đang quay.')
            await sleep(wait)
            await msg.edit('🎲 Đang quay..')
            await sleep(wait)
            await msg.edit('🎲 Đang quay...')
            await sleep(wait)
            await msg.edit('💵 Xin chúc mừng, ...')
            await sleep(2)
            if random.random() < percent:
                await msg.edit(f'💵 Xin chúc mừng, bạn đã nhận được {amount:,} PuraCN {random.choice(config["emojisFun"])}')
                moneys[str(ctx.author.id)]["moneys"] += amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
            else:
                moneys[str(ctx.author.id)]["moneys"] -= amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
                await msg.edit(f'💵 Xin chúc mừng, bạn đã mất hết tiền cược {random.choice(config["emojisSad"])}')

    @slots.command()
    async def all(self,ctx):
        with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'r',encoding='utf-8') as f:
            moneys = json.load(f)
        wait = 0.5
        amount = moneys[str(ctx.author.id)]["moneys"]
        percent = 0.5
        if not moneys.get(str(ctx.author.id)):
            moneys[str(ctx.author.id)] = {"moneys":100000}
            with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            msg = await ctx.reply('🎲 Đang quay')
            await sleep(wait)
            await msg.edit('🎲 Đang quay.')
            await sleep(wait)
            await msg.edit('🎲 Đang quay..')
            await sleep(wait)
            await msg.edit('🎲 Đang quay...')
            await msg.edit('💵 Xin chúc mừng, ...')
            await sleep(2)
            if random.random() < percent:
                await msg.edit(f'💵 Xin chúc mừng, bạn đã nhận được {amount:,} PuraCN {random.choice(config["emojisFun"])}')
                moneys[str(ctx.author.id)]["moneys"] += amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
            else:
                moneys[str(ctx.author.id)]["moneys"] -= amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
                await msg.edit(f'💵 Xin chúc mừng, bạn đã mất hết tiền cược {random.choice(config["emojisSad"])}')
        else:
            msg = await ctx.reply('🎲 Đang quay')
            await sleep(wait)
            await msg.edit('🎲 Đang quay.')
            await sleep(wait)
            await msg.edit('🎲 Đang quay..')
            await sleep(wait)
            await msg.edit('🎲 Đang quay...')
            await sleep(wait)
            await msg.edit('💵 Xin chúc mừng, ...')
            await sleep(2)
            if random.random() < percent:
                await msg.edit(f'💵 Xin chúc mừng, bạn đã nhận được {amount:,} PuraCN {random.choice(config["emojisFun"])}')
                moneys[str(ctx.author.id)]["moneys"] += amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
            else:
                await msg.edit(f'💵 Xin chúc mừng, bạn đã mất hết tiền cược {random.choice(config["emojisSad"])}')
                moneys[str(ctx.author.id)]["moneys"] -= amount
                with open(__file__.replace('commands\moneys\slots.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)

def setup(client):
    client.add_cog(Slots(client))
