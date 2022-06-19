import nextcord
from nextcord.ext import commands
from nextcord import Colour
import random
from asyncio import sleep


class Hack(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.guild_only()
    async def hack(self,ctx,*,member:nextcord.Member=None):
        if member == None:
            embed = nextcord.Embed(title='❌ Không rõ người dùng!',color=Colour.red())
            await ctx.reply(embed=embed)
        else:
            msg = await ctx.send(embed=nextcord.Embed(title=f'Bắt đầu hack {member.display_name}!'))
            await sleep(3)
            for i in range(2):
                await msg.edit(embed=nextcord.Embed(title='Đang tìm địa chỉ IP.',color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title='Đang tìm địa chỉ IP..',color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title='Đang tìm địa chỉ IP...',color=Colour.red()))
                await sleep(0.25)
            await msg.edit(embed=nextcord.Embed(title=f"Địa chỉ IP: {random.randint(1,20)}.{random.randint(200,500)}.{random.randint(1,9)}.{random.randint(200,500)}",color=Colour.green()))
            await sleep(2)
            for i in range(2):
                await msg.edit(embed=nextcord.Embed(title="Đang tìm port trong IP bị sơ hở.",color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title="Đang tìm port trong IP bị sơ hở..",color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title="Đang tìm port trong IP bị sơ hở...",color=Colour.red()))
                await sleep(0.25)
            await msg.edit(embed=nextcord.Embed(title=f"Port IP bị sơ hở: {random.randint(10000,65535)}",color=Colour.green()))
            await sleep(2)
            for i in range(2):
                await msg.edit(embed=nextcord.Embed(title="Đang tìm port trong IP bị sơ hở...",color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title="Đang tìm port trong IP bị sơ hở...",color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title="Đang tìm port trong IP bị sơ hở...",color=Colour.red()))
                await sleep(0.25)
            await msg.edit(embed=nextcord.Embed(title="Đang phá hỏng hệ thống chống virus",color=Colour.red()))
            await sleep(2)
            await msg.edit(embed=nextcord.Embed(title="Đang phá hỏng hệ thống máy",color=Colour.red()))
            await sleep(2)
            await msg.edit(embed=nextcord.Embed(title="Đang tạo các virus máy",color=Colour.red()))
            await sleep(2)
            await msg.edit(embed=nextcord.Embed(title="Đang cải tiến các virus máy",color=Colour.red()))
            await sleep(2)
            for i in range(3):
                await msg.edit(embed=nextcord.Embed(title="Đang xâm nhập vào các tài khoản liên kết.",color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title="Đang xâm nhập vào các tài khoản liên kết..",color=Colour.red()))
                await sleep(0.25)
                await msg.edit(embed=nextcord.Embed(title="Đang xâm nhập vào các tài khoản liên kết...",color=Colour.red()))
                await sleep(0.25)
            await msg.edit(content=f"Đã hack {member} thành công",embed=None)
            random_ket_qua = ["Hack thiết bị thành công :3","Đã hack IP thành công :>","Không thu được gì ;-;","Hack đã bị chống đối :<","Hack máy chủ thành công >:)","Hack tài khoản thành công :D","Bị cảnh sát bắt ;-;","Bị tử hình ☠️"]
            ketqua = random.choice(random_ket_qua)
            await msg.edit(f"Kết quả: {ketqua}")

def setup(client):
    client.add_cog(Hack(client))
