import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Guild(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    async def guild(self,ctx):
        guild:nextcord.Guild = ctx.guild
        if guild.icon == None:
            icon_guild = 'https://cdn.discordapp.com/attachments/944030840302755841/945223221576364083/New_Bitmap_image.bmp'
        else:
            icon_guild = guild.icon
        embed = nextcord.Embed(title=f'Thông tin máy chủ - {guild.name}',description=f'Dùng `{self.client.command_prefix}guild roles` để xem tất cả các vai trò trong máy chủ\nDùng `{self.client.command_prefix}guild icon` để xem ảnh máy chủ',color=Colour.blurple())
        embed.add_field(name='Tên máy chủ',value=guild.name,inline=True)
        embed.add_field(name='ID',value=guild.id,inline=True)
        embed.add_field(name='Chủ máy chủ',value=guild.owner,inline=True)
        embed.add_field(name='Thành viên',value=guild.member_count,inline=True)
        embed.add_field(name='Vai trò',value=len(guild.roles),inline=True)
        embed.add_field(name='Emojis',value=len(guild.emojis),inline=True)
        embed.add_field(name='Stickers',value=len(guild.stickers),inline=True)
        embed.add_field(name='Nâng cấp máy chủ',value=guild.premium_subscription_count,inline=True)
        embed.add_field(name='Tạo máy chủ vào ngày',value=guild.created_at.strftime('%d/%m/%Y'),inline=True)
        embed.add_field(name=f'Kênh ({len(guild.channels)})',value=f'{len(guild.text_channels)} kênh chat | {len(guild.voice_channels)} kênh thoại | {len(guild.categories)} danh mục',inline=False)
        embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
        embed.set_thumbnail(url=icon_guild)
        await ctx.send(embed=embed)

    @guild.command()
    @commands.guild_only()
    async def roles(self,ctx):
        guild:nextcord.Guild = ctx.guild
        roles = [role for role in guild.roles]
        roless = ', '.join([role.mention for role in roles])
        embed = nextcord.Embed(title='Tất cả vai trò trong máy chủ',description=roless,color=Colour.green())
        embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)
    
    @guild.command()
    async def icon(self,ctx):
        guild:nextcord.Guild = ctx.guild
        if guild.icon == None:
            embed = nextcord.Embed(title='❌ Máy chủ hiện chưa có biểu tượng!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            webp = guild.icon.with_format('webp')
            png = guild.icon.with_format('png')
            jpg = guild.icon.with_format('jpg')
            embed = nextcord.Embed(title=f'Icon {guild}',color=Colour.blurple())
            embed.add_field(name='URL',value=f'[WEBP]({webp} "Ảnh định dạng WEBP")|[PNG]({png} "Ảnh định dạng PNG")|[JPG]({jpg} "Ảnh định dạng JPG")',inline=False)
            embed.set_image(url=guild.icon)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Guild(client))
