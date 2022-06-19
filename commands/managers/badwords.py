import nextcord
from nextcord.ext import commands
import json
from nextcord import Colour


class Badwords(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    @commands.has_permissions(manage_messages=True)
    @commands.guild_only()
    async def badwords(self,ctx):
        badwords_help = f'''```md
### Bad Words ###

# Các lệnh
On: Bật ngôn từ xấu cho máy chủ
Off: Tắt ngôn từ xấu cho máy chủ
Add: Thêm ngôn từ xấu cho máy chủ
Remove: Xóa ngôn từ xấu khỏi máy chủ
List: Hiện tất cả ngôn từ xấu của máy chủ
# Lệnh
{self.client.command_prefix}badwords on|off|add|remove|list
{self.client.command_prefix}badwords on
{self.client.command_prefix}badwords off
{self.client.command_prefix}badwords add <Ngôn từ xấu>
{self.client.command_prefix}badwords remove <Ngôn từ xấu>
{self.client.command_prefix}badwords list
```'''
        await ctx.send(badwords_help)

    @badwords.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def on(self,ctx):
        with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'r',encoding='utf-8') as f:
            guilds = json.load(f)
        if guilds[str(ctx.guild.id)]["bad_words"] == True:
            embed = nextcord.Embed(title='❌ Ngôn từ xấu hiện đang bật trong máy chủ!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            guilds[str(ctx.guild.id)]["bad_words"] = True
            with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'w',encoding='utf-8') as f:
                json.dump(guilds,f,indent=4,ensure_ascii=False)
            embed = nextcord.Embed(title='Đã bật ngôn từ xấu cho máy chủ',description=f'Thêm các ngôn từ xấu cho máy chủ dùng lệnh\n{self.client.command_prefix}badwords add <Ngôn từ xấu>',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

    @badwords.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def off(self,ctx):
        with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'r',encoding='utf-8') as f:
            guilds = json.load(f)
        if guilds[str(ctx.guild.id)]["bad_words"] == False:
            embed = nextcord.Embed(title='❌ Ngôn từ xấu hiện đang tắt trong máy chủ!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            guilds[str(ctx.guild.id)]["bad_words"] = False
            with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'w',encoding='utf-8') as f:
                json.dump(guilds,f,indent=4,ensure_ascii=False)
            embed = nextcord.Embed(title='Đã tắt ngôn từ xấu cho máy chủ',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

    @badwords.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def add(self,ctx,*,badwords=None):
        badwords = badwords.lower()
        with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'r',encoding='utf-8') as f:
                guilds = json.load(f)
        if badwords == None:
            embed = nextcord.Embed(title='❌ Không rõ ngôn từ xấu cần thêm cho máy chủ!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif badwords in guilds[str(ctx.guild.id)]["list_bad_words"]:
            embed = nextcord.Embed(title='❌ Ngôn từ xấu hiện đã có trong máy chủ!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            guilds[str(ctx.guild.id)]["list_bad_words"].append(badwords)
            with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'w',encoding='utf-8') as f:
                json.dump(guilds,f,indent=4,ensure_ascii=False)
            embed = nextcord.Embed(title=f'''Đã thêm từ ngữ xấu cho máy chủ
Từ ngữ: `{badwords}`''',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

    @badwords.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def remove(self,ctx,*,badwords=None):
        badwords = badwords.lower()
        with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'r',encoding='utf-8') as f:
                guilds = json.load(f)
        if badwords == None:
            embed = nextcord.Embed(title='❌ Không rõ ngôn từ xấu cần gỡ bỏ khỏi máy chủ!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif badwords not in guilds[str(ctx.guild.id)]["list_bad_words"]:
            embed = nextcord.Embed(title='❌ Ngôn từ xấu hiện không có trong máy chủ!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            guilds[str(ctx.guild.id)]["list_bad_words"].remove(badwords)
            with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'w',encoding='utf-8') as f:
                json.dump(guilds,f,indent=4,ensure_ascii=False)
            embed = nextcord.Embed(title=f'''Đã gỡ bỏ từ ngữ xấu khỏi máy chủ
Từ ngữ: `{badwords}`''',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed,delete_after=3)

    @badwords.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def list(self,ctx):
        with open(__file__.replace('commands\managers\\badwords.py','data\\badwords.json'),'r',encoding='utf-8') as f:
                guilds = json.load(f)
        if not guilds[str(ctx.guild.id)]["list_bad_words"]:
            embed = nextcord.Embed(title='❌ Máy chủ vẫn chưa có từ ngữ xấu nào!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            list_badwords = [badword for badword in guilds[str(ctx.guild.id)]["list_bad_words"]]
            badwords = ', '.join([badword for badword in list_badwords])
            embed = nextcord.Embed(title='Danh sách các từ ngữ xấu của máy chủ',description=badwords,color=Colour.green())
            embed.set_thumbnail(url=ctx.guild.icon)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Badwords(client))
