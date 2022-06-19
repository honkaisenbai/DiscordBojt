import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Mute(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_messages=True,manage_roles=True)
    @commands.bot_has_permissions(manage_messages=True,manage_roles=True)
    @commands.guild_only()
    async def mute(self,ctx, member: nextcord.Member=None, *, reason="Không có lý do"):
        guild = ctx.guild
        mutedRole = nextcord.utils.get(guild.roles,name="Muted")
        if not mutedRole:
            mutedRole = await guild.create_role(name="Muted")
            for channel in guild.channels:
                await channel.set_permissions(mutedRole, send_messages=False, read_message_history=True, read_messages=True,create_public_threads=False,create_private_threads=False,send_messages_in_threads=False)
            await member.add_roles(mutedRole, reason=reason)
            embed = nextcord.Embed(color=Colour.green(),title=f"""{member} đã bị tắt tiếng
Lý do: `{reason}`""",timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            embed = nextcord.Embed(title=f"""Bạn đã bị tắt tiếng trong máy chủ {guild.name}
Lý do: `{reason}`""",color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await member.send(embed=embed)
        elif member == ctx.author:
            embed = nextcord.Embed(title="❌ Bạn không thể tự tắt tiếng chính mình!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif member == None:
            embed = nextcord.Embed(title="❌ Không rõ thành viên!",color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        elif mutedRole in member.roles:
            embed = nextcord.Embed(title='❌ Thành viên này hiện đã bị tắt tiếng!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            await member.add_roles(mutedRole, reason=f'{ctx.author} đã tắt tiếng {member} với lý do `{reason}`')
            embed = nextcord.Embed(color=Colour.green(),title=f"""{member} đã bị tắt tiếng
Lý do: `{reason}`""",timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)
            embed = nextcord.Embed(title=f"""Bạn đã bị tắt tiếng trong máy chủ {guild.name}
Lý do: `{reason}`""",color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await member.send(embed=embed)

def setup(client):
    client.add_cog(Mute(client))
