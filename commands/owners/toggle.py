import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Toggle(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def toggle(self,ctx,*,command=None):
        if command == None:
            embed = nextcord.Embed(title='❌ Không rõ lệnh!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            command = self.client.get_command(command)
            command.enabled = not command.enabled
            ternary = 'bật' if command.enabled else 'tắt'
            embed = nextcord.Embed(title=f'Đã {ternary} lệnh `{command.name}`',color=Colour.green())
            await ctx.reply(embed=embed)

def setup(client):
    client.add_cog(Toggle(client))
