import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Avatar(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def avatar(self,ctx, member:nextcord.Member=None):
        if member == None:
            member = ctx.author
        if member.avatar == None:
            png = member.display_avatar.with_format('png')
            embed = nextcord.Embed(title=f'Ảnh đại diện {member}',color=Colour.blurple())
            embed.add_field(name='URL',value=f'[PNG]({png} "Ảnh định dạng PNG")',inline=False)
            embed.set_image(url=member.display_avatar)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
        else:
            webp = member.display_avatar.with_format('webp')
            png = member.display_avatar.with_format('png')
            jpg = member.display_avatar.with_format('jpg')
            embed = nextcord.Embed(title=f'Ảnh đại diện {member}',color=Colour.blurple())
            embed.add_field(name='URL',value=f'[WEBP]({webp} "Ảnh định dạng WEBP")|[PNG]({png} "Ảnh định dạng PNG")|[JPG]({jpg} "Ảnh định dạng JPG")',inline=False)
            embed.set_image(url=member.avatar)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Avatar(client))
