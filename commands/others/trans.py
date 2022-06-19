import nextcord
from nextcord.ext import commands
from nextcord import Colour
import json
import googletrans


class Trans(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def trans(self,ctx,langcode:str=None,*,text=None):
        if langcode == None:
            embed = nextcord.Embed(title='❌ Không rõ mã ngôn ngữ!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif text == None:
            embed = nextcord.Embed(title='❌ Không rõ nội dung cần dịch!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            with open(__file__.replace('commands\others\\trans.py','data\languagecodes.json'),'r',encoding='utf-8') as f:
                dest = json.load(f)
            translator = googletrans.Translator()
            try:
                translated = translator.translate(text=text,dest=str(langcode))
            except:
                embed = nextcord.Embed(title='❌ Không rõ mã ngôn ngữ cần dịch!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            embed = nextcord.Embed(title=translated.text,description=f'Dịch từ `{text}`\nPhát hiện ngôn ngữ `{dest[str(translated.src)]}`',color=Colour.green())
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.reply(embed=embed)

    @trans.command()
    async def lang(self,ctx):
        file = nextcord.File(__file__.replace('commands\others\\trans.py','data\languagecodes.json'),spoiler=True)
        await ctx.send(content='Các mã ngôn ngữ được hỗ trợ',file=file)

def setup(client):
    client.add_cog(Trans(client))
