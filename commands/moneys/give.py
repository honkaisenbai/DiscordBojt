import nextcord
from nextcord.ext import commands
from nextcord import Colour
import json


class Give(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def give(self,ctx,member:nextcord.Member,amount:int=None):
        with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'r',encoding='utf-8') as f:
            moneys = json.load(f)
        if amount == None:
            embed = nextcord.Embed(title='❌ Không rõ số tiền cần tặng!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif amount <= 0:
            embed = nextcord.Embed(title='❌ Không thể tặng số tiền dưới 0 PuraCN!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif member == ctx.author:
            embed = nextcord.Embed(title='❌ Bạn không thể tặng tiền cho chính mình!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif amount > moneys[str(ctx.author.id)]["moneys"]:
            embed = nextcord.Embed(title='❌ Bạn không đủ tiền để tặng!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif not moneys.get(str(ctx.author.id)):
            moneys[str(ctx.author.id)] = {"moneys":100000}
            with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            if not moneys.get(str(member.id)):
                moneys[str(member.id)] = {"moneys":100000}
                with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
                moneys[str(ctx.author.id)]["moneys"] -= amount
                moneys[str(member.id)]["moneys"] += amount
                with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
                embed = nextcord.Embed(title=f'✅ Bạn đã tặng `{amount:,}` PuraCN cho {member}',color=Colour.green(),timestamp=ctx.message.created_at)
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)
                embed = nextcord.Embed(title=f'✅ Bạn đã nhận `{amount:,}` PuraCN trong máy chủ `{ctx.guild}`',timestamp=ctx.message.created_at,color=Colour.green())
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await member.send(embed=embed)
            else:
                moneys[str(ctx.author.id)]["moneys"] -= amount
                moneys[str(member.id)]["moneys"] += amount
                with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'w',encoding='utf-8') as f:
                    json.dump(moneys,f,indent=4)
                embed = nextcord.Embed(title=f'✅ Bạn đã tặng `{amount:,}` PuraCN cho {member}',color=Colour.green(),timestamp=ctx.message.created_at)
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)
                embed = nextcord.Embed(title=f'✅ Bạn đã nhận `{amount:,}` PuraCN trong máy chủ `{ctx.guild}`',timestamp=ctx.message.created_at,color=Colour.green())
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await member.send(embed=embed)
        elif not moneys.get(str(member.id)):
            moneys[str(member.id)] = {"moneys":100000}
            with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            moneys[str(ctx.author.id)]["moneys"] -= amount
            moneys[str(member.id)]["moneys"] += amount
            with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            embed = nextcord.Embed(title=f'✅ Bạn đã tặng `{amount:,}` PuraCN cho {member}',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            embed = nextcord.Embed(title=f'✅ Bạn đã nhận `{amount:,}` PuraCN trong máy chủ `{ctx.guild}`',timestamp=ctx.message.created_at,color=Colour.green())
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await member.send(embed=embed)
        else:
            moneys[str(ctx.author.id)]["moneys"] -= amount
            moneys[str(member.id)]["moneys"] += amount
            with open(__file__.replace('commands\moneys\give.py','data\moneys.json'),'w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            embed = nextcord.Embed(title=f'✅ Bạn đã tặng `{amount:,}` PuraCN cho {member}',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            embed = nextcord.Embed(title=f'✅ Bạn đã nhận `{amount:,}` PuraCN trong máy chủ `{ctx.guild}`',timestamp=ctx.message.created_at,color=Colour.green())
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await member.send(embed=embed)

def setup(client):
    client.add_cog(Give(client))
