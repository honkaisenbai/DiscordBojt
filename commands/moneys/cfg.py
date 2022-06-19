import nextcord
from nextcord.ext import commands
from nextcord import Colour
from asyncio import sleep
import json
import random


config = json.load(open(__file__.replace('commands\moneys\cfg.py','config.json'),'r',encoding='utf-8'))

class Cfg(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def cfg(self,ctx,amount:int=1,choice:str='u'):
        with open(__file__.replace('commands\moneys\cfg.py','data\moneys.json'),'r',encoding='utf-8') as f:
            moneys = json.load(f)
        choices_face = ['u','d']
        if amount <= 0:
            embed = nextcord.Embed(title='❌ Không thể chơi với số tiền dưới 0 PuraCN!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif amount > moneys[str(ctx.author.id)]["moneys"]:
            embed = nextcord.Embed(title='❌ Bạn không đủ tiền để chơi!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif not moneys.get(str(ctx.author.id)):
            moneys[str(ctx.author.id)] = {"moneys":100000}
            with open(__file__.replace('commands\moneys\cfg.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
        elif choice not in choices_face:
            embed = nextcord.Embed(title=f'❌ Không rõ lựa chọn mặt xu `{choice}`!',description='',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            wait = 1
            answer = random.choice(choices_face)
            face = 'trên' if choice == 'u' else 'dưới'
            send = f'Bạn đã chọn mặt **{face}** và cược {amount:,} PuraCN\n🪙 Đang xoay.'
            msg = await ctx.reply(send)
            await sleep(wait)
            await msg.edit(send+'.')
            await sleep(wait)
            await msg.edit(send+'.')
            await sleep(wait)
            if choice == answer:
                face = 'trên' if answer == 'u' else 'dưới'
                await msg.edit(f'💵 Bạn đã trúng {amount:,} PuraCN {random.choice(config["emojisFun"])}\nKết quả: **{face}**')
                moneys[str(ctx.author.id)]["moneys"] += amount
                with open(__file__.replace('commands\moneys\cfg.py','data\moneys.json'), 'w') as f:
                    json.dump(moneys,f,indent=4)
            else:
                face = 'trên' if answer == 'u' else 'dưới'
                await msg.edit(f'💵 Bạn đã mất hết tiền cược {random.choice(config["emojisSad"])}\nKết quả: **{face}**')
                moneys[str(ctx.author.id)]["moneys"] -= amount
                with open(__file__.replace('commands\moneys\cfg.py','data\moneys.json'), 'w') as f:
                    json.dump(moneys,f,indent=4)

def setup(client):
    client.add_cog(Cfg(client))
