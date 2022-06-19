import nextcord
from nextcord.ext import commands
from nextcord import Colour
import os
from datetime import datetime
import json


config = json.load(open(__file__.replace('commands\others\\file.py','config.json'),'r',encoding='utf-8'))
premiums_users = json.load(open(__file__.replace('commands\others\\file.py','premiums.json'),'r',encoding='utf-8'))

class File(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    @commands.dm_only()
    async def file(self,ctx):
        file_help = f'''```md
### File ###

# Các lệnh
Add: Thêm tập tin vào thư viện tập tin của bạn
Delete: Xóa tập tin khỏi thư viện tập tin của bạn
Show: Hiện tập tin cần hiện trong thư viện tập tin của bạn
List: Hiện tất cả tập tin trong thư viện tập tin của bạn
Log: Hiện nhật ký chỉnh sửa thư viện tập tin của bạn
# Lưu ý
Đính kèm tập tin cùng với lệnh để lưu tập tin
# Lệnh
{self.client.command_prefix}file add|delete|show|list|log
{self.client.command_prefix}file add
{self.client.command_prefix}file delete <Tên tập tin cần xóa>
{self.client.command_prefix}file show <Tên tập tin cần hiện>
{self.client.command_prefix}file list
{self.client.command_prefix}file log
```'''
        await ctx.send(file_help)

    @file.command()
    @commands.dm_only()
    async def add(self,ctx):
        if ctx.author.id not in premiums_users:
            embed = nextcord.Embed(title='❌ Bạn không có đặc quyền `Premium` để có thể dùng lệnh này!',description='Vào máy chủ trợ giúp để hiểu rõ hơn về premium',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            if not os.path.isdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                os.mkdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}'))
                for attachment in ctx.message.attachments:
                    if os.path.isfile(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}\{attachment.filename}')):
                        embed = nextcord.Embed(title=f'❌ Tập tin `{attachment.filename}` hiện đang tồn tại trong thư viện tập tin của bạn!',description='Đổi tên tập tin khác với tập tin hiện đang có để có thể lưu',color=Colour.red())
                        await ctx.reply(embed=embed,delete_after=3)
                    elif len(os.listdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}'))) > 4:
                        embed = nextcord.Embed(title='❌ Bạn không thể lưu thêm tập tin vào thư viện tập tin của bạn!',description='Giới hạn tập tin không được nhiều hơn 5 tập tin',color=Colour.red())
                        await ctx.reply(embed=embed,delete_after=3)
                    else:
                        await attachment.save(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}\{attachment.filename}'))
                embed = nextcord.Embed(title='Đã lưu tập tin vào thư viện tập tin của bạn',color=Colour.green())
                await ctx.reply(embed=embed,delete_after=3)
                with open(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}.log'),'a',encoding='utf-8') as f:
                    f.write(f'[{datetime.now().strftime("%d-%m-%Y - %H:%M:%S")}]: Bạn đã thêm tập tin `{attachment.filename}` vào thư viện tập tin của bạn\n')
            elif len(os.listdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}'))) > 4:
                embed = nextcord.Embed(title='❌ Bạn không thể lưu thêm tập tin vào thư viện tập tin của bạn!',description='Giới hạn tập tin không được nhiều hơn 5 tập tin',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            elif not ctx.message.attachments:
                embed = nextcord.Embed(title='❌ Không có tập tin cần lưu trữ!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                for attachment in ctx.message.attachments:
                    if os.path.isfile(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}\{attachment.filename}')):
                        embed = nextcord.Embed(title=f'❌ Tập tin `{attachment.filename}` hiện đang tồn tại trong thư viện tập tin của bạn!',description='Đổi tên tập tin khác với tập tin hiện đang có để có thể lưu',color=Colour.red())
                        await ctx.reply(embed=embed,delete_after=3)
                    elif len(os.listdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}'))) > 4:
                        embed = nextcord.Embed(title='❌ Bạn không thể lưu thêm tập tin vào thư viện tập tin của bạn!',description='Giới hạn tập tin không được nhiều hơn 5 tập tin',color=Colour.red())
                        await ctx.reply(embed=embed,delete_after=3)
                    else:
                        await attachment.save(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}\{attachment.filename}'))
                        embed = nextcord.Embed(title='Đã lưu tập tin vào thư viện tập tin của bạn',color=Colour.green())
                        await ctx.reply(embed=embed,delete_after=3)
                        with open(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}.log'),'a',encoding='utf-8') as f:
                            f.write(f'[{datetime.now().strftime("%d-%m-%Y - %H:%M:%S")}]: Bạn đã thêm tập tin `{attachment.filename}` vào thư viện tập tin của bạn\n')

    @file.command()
    @commands.dm_only()
    async def list(self,ctx):
        if ctx.author.id not in premiums_users:
            embed = nextcord.Embed(title='❌ Bạn không có đặc quyền `Premium` để có thể dùng lệnh này!',description='Vào máy chủ trợ giúp để hiểu rõ hơn về premium',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            if not os.path.isdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                embed = nextcord.Embed(title='❌ Bạn chưa lưu trữ tập tin đầu tiên nào!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            elif not os.listdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                embed = nextcord.Embed(title='❌ Bạn hiện chưa lưu trữ tập tin nào!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                list_files = [file for file in os.listdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}'))]
                file_list = ', '.join([file for file in list_files])
                embed = nextcord.Embed(title='Tất cả các tập tin của bạn',description=file_list,color=Colour.green())
                await ctx.send(embed=embed)

    @file.command()
    @commands.dm_only()
    async def delete(self,ctx,*,filename=None):
        if ctx.author.id not in premiums_users:
            embed = nextcord.Embed(title='❌ Bạn không có đặc quyền `Premium` để có thể dùng lệnh này!',description='Vào máy chủ trợ giúp để hiểu rõ hơn về premium',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            if not os.path.isdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                embed = nextcord.Embed(title='❌ Bạn chưa lưu trữ tập tin đầu tiên nào!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            elif filename == None:
                embed = nextcord.Embed(title='❌ Không rõ tên tập tin!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            elif filename not in os.listdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                embed = nextcord.Embed(title=f'❌ Không rõ tập tin `{filename}` trong thư viện tập tin của bạn!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                os.remove(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}\{filename}'))
                embed = nextcord.Embed(title=f'Đã xóa tập tin `{filename}` khỏi thử viện tập tin của bạn',color=Colour.green())
                await ctx.send(embed=embed)
                with open(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}.log'),'a',encoding='utf-8') as f:
                    f.write(f'[{datetime.now().strftime("%d-%m-%Y - %H:%M:%S")}]: Bạn đã xóa tập tin `{filename}` khỏi thư viện tập tin của bạn\n')

    @file.command()
    @commands.dm_only()
    async def show(self,ctx,*,filename=None):
        if ctx.author.id not in premiums_users:
            embed = nextcord.Embed(title='❌ Bạn không có đặc quyền `Premium` để có thể dùng lệnh này!',description='Vào máy chủ trợ giúp để hiểu rõ hơn về premium',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            if not os.path.isdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                embed = nextcord.Embed(title='❌ Bạn chưa lưu trữ tập tin đầu tiên nào!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            elif filename == None:
                embed = nextcord.Embed(title='❌ Không rõ tên tập tin!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            elif filename not in os.listdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                embed = nextcord.Embed(title=f'❌ Không rõ tập tin `{filename}` trong thư viện tập tin của bạn!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                file = nextcord.File(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}\{filename}'))
                await ctx.send(file=file)
                with open(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}.log'),'a',encoding='utf-8') as f:
                    f.write(f'[{datetime.now().strftime("%d-%m-%Y - %H:%M:%S")}]: Bạn đã mở tập tin `{filename}` trên thư viện tập tin của bạn\n')

    @file.command()
    async def log(self,ctx):
        if ctx.author.id not in premiums_users:
            embed = nextcord.Embed(title='❌ Bạn không có đặc quyền `Premium` để có thể dùng lệnh này!',description='Vào máy chủ trợ giúp để hiểu rõ hơn về premium',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            if not os.path.isdir(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}')):
                embed = nextcord.Embed(title='❌ Bạn chưa lưu trữ tập tin đầu tiên nào!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            elif not os.path.isfile(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}.log')):
                embed = nextcord.Embed(title='❌ Không có nhật ký chỉnh sửa nào!',description='Thường do bạn chưa lưu tập tin nào',color=Colour.red())
                await ctx.send(embed=embed,delete_after=3)
            else:
                log_file = nextcord.File(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}.log'))
                await ctx.send(file=log_file)
                with open(__file__.replace('commands\others\\file.py',f'data\\files\{ctx.author.id}.log'),'a',encoding='utf-8') as f:
                    f.write(f'[{datetime.now().strftime("%d-%m-%Y - %H:%M:%S")}]: Bạn đã mở nhật ký chỉnh sửa thư viện tập tin của bạn\n')

def setup(client):
    client.add_cog(File(client))
