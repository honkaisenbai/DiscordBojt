import nextcord
from nextcord.ext import commands
import requests
from nextcord import Colour
from io import BytesIO


class Skins(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def skins(self,ctx,*,name=None):
        if name == None:
            embed = nextcord.Embed(title='❌ Không rõ tên người dùng!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            try:
                info = requests.get(url=f'https://api.mojang.com/users/profiles/minecraft/{name}').json()
                name = info["name"]
                id = info["id"]
            except:
                embed = nextcord.Embed(title='❌ Không tìm thấy người dùng!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            avatar = f'https://crafatar.com/avatars/{id}'
            skin = f'https://crafatar.com/renders/body/{id}'
            skin_button = nextcord.ui.Button(style=nextcord.ButtonStyle.green,label='Tải Skin')
            cape_button = nextcord.ui.Button(style=nextcord.ButtonStyle.green,label='Tải Áo Choàng')
            view = nextcord.ui.View(timeout=60)
            async def cape_callback(interaction:nextcord.Interaction):
                cape_download = requests.get(url=f'https://crafatar.com/capes/{id}')
                with open(__file__.replace('commands\informations\skins.py','data\capes.png'),'wb') as f:
                    f.write(cape_download.content)
                file = nextcord.File(__file__.replace('commands\informations\skins.py','data\capes.png'))
                await interaction.response.send_message(f'Áo choàng - {name}',file=file,ephemeral=True)
            async def skin_callback(interaction:nextcord.Interaction):
                skin_download = requests.get(url=f'https://crafatar.com/skins/{id}')
                with open(__file__.replace('commands\informations\skins.py','data\skins.png'),'wb') as f:
                    f.write(skin_download.content)
                file = nextcord.File(__file__.replace('commands\informations\skins.py','data\skins.png'))
                await interaction.response.send_message(f'Skin - {name}',file=file,ephemeral=True)
            skin_button.callback = skin_callback
            view.add_item(skin_button)
            if not requests.get(f'https://crafatar.com/capes/{id}'):
                pass
            else:
                cape_button.callback = cape_callback
                view.add_item(cape_button)
            embed = nextcord.Embed(title=f'Skin người dùng - {name}',color=Colour.blurple(),timestamp=ctx.message.created_at)
            embed.set_thumbnail(url=avatar)
            embed.set_image(url=skin)
            await ctx.send(embed=embed,view=view)

def setup(client):
    client.add_cog(Skins(client))
