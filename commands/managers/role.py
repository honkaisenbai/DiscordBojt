import nextcord
from nextcord.ext import commands
from nextcord import Colour


class Role(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    @commands.guild_only()
    async def role(self,ctx):
        role_help = f'''```md
### Role ###

# Các lệnh
Create: Tạo vai trò trong máy chủ với tên cần đặt
Delete: Xóa vai trò trong máy chủ
Add: Thêm vai trò cho thành viên
Remove: Bỏ vai trò khỏi thành viên
# Lệnh
{self.client.command_prefix}role create|delete|add|remove
{self.client.command_prefix}role create <Tên vai trò cần tạo>
{self.client.command_prefix}role delete <Vai trò>
{self.client.command_prefix}role add <Thành viên> <Vai trò>
{self.client.command_prefix}role remove <Thành viên> <Vai trò>
```'''
        await ctx.send(role_help)
    
    @role.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def create(self,ctx,*,rolename=None):
        if rolename == None:
            embed = nextcord.Embed(title='❌ Không rõ tên vai trò cần tạo!',color=Colour.red())
            await ctx.reply(embed=embed)
        elif len(rolename) > 100:
            embed = nextcord.Embed(title='❌ Tên vai trò đã vượt mức giới hạn tên!',description='Tên vai trò không được lớn hơn 100 ký tự',color=Colour.red())
            await ctx.reply(embed=embed)
        else:
            await ctx.guild.create_role(name=rolename,reason=f'{ctx.author} đã tạo vai trò với tên `{rolename}`')
            embed = nextcord.Embed(title=f'Đã tạo vai trò `{rolename}`',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

    @role.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def delete(self,ctx,*,role:nextcord.Role=None):
        if role == None:
            embed = nextcord.Embed(title='❌ Không rõ tên vai trò cần xóa!',color=Colour.red())
            await ctx.reply(embed=embed)
        else:
            role = nextcord.utils.get(ctx.message.guild.roles, name=role.name)
            await role.delete(reason=f'{ctx.author} đã xóa vai trò `{role.name}`')
            embed = nextcord.Embed(title=f'Đã xóa vai trò `{role.name}`',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

    @role.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def add(self,ctx,member:nextcord.Member=None,*,role:nextcord.Role=None):
        if member == None:
            embed = nextcord.Embed(title='❌ Không rõ người dùng!',color=Colour.red())
            await ctx.reply(embed=embed)
        elif role == None:
            embed = nextcord.Embed(title='❌ Không rõ vai trò cần thêm!',color=Colour.red())
            await ctx.reply(embed=embed)
        elif role in member.roles:
            embed = nextcord.Embed(title='❌ Người dùng đã có vai trò này!',color=Colour.red())
            await ctx.reply(embed=embed)
        else:
            pura_role:nextcord.Role = nextcord.utils.get(ctx.guild.roles,name='PuraGH')
            if pura_role.position < member.top_role.position:
                embed = nextcord.Embed(title="❌ Tôi không thể thêm vai trò cho thành viên này!",description='Vai trò thành viên này cao hơn vai trò của tôi',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                role_add = nextcord.utils.get(ctx.guild.roles,name=role.name)
                await member.add_roles(role_add,reason=f'{ctx.author} đã thêm vai trò `{role.name}` cho {member}')
                embed = nextcord.Embed(title=f'Đã thêm vai trò `{role}` cho {member}',color=Colour.green(),timestamp=ctx.message.created_at)
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)

    @role.command()
    @commands.guild_only()
    @commands.has_permissions(manage_roles=True)
    @commands.bot_has_permissions(manage_roles=True)
    async def remove(self,ctx,member:nextcord.Member=None,*,role:nextcord.Role=None):
        if member == None:
            embed = nextcord.Embed(title='❌ Không rõ người dùng!',color=Colour.red())
            await ctx.reply(embed=embed)
        elif role == None:
            embed = nextcord.Embed(title='❌ Không rõ vai trò cần gỡ bỏ!',color=Colour.red())
            await ctx.reply(embed=embed)
        elif role not in member.roles:
            embed = nextcord.Embed(title='❌ Người dùng không có vai trò này!',color=Colour.red())
            await ctx.reply(embed=embed)
        else:
            pura_role:nextcord.Role = nextcord.utils.get(ctx.guild.roles,name='PuraGH')
            if pura_role.position < member.top_role.position:
                embed = nextcord.Embed(title="❌ Tôi không thể gỡ vai trò khỏi thành viên này!",description='Vai trò thành viên này cao hơn vai trò của tôi',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            else:
                role_remove = nextcord.utils.get(ctx.guild.roles,name=role.name)
                await member.remove_roles(role_remove,reason=f'{ctx.author} đã gỡ bỏ vai trò `{role}` ra khỏi {member}')
                embed = nextcord.Embed(title=f'Đã gỡ bỏ vai trò `{role}` ra khỏi {member}',color=Colour.green(),timestamp=ctx.message.created_at)
                embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Role(client))
