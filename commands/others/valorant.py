import nextcord
from nextcord.ext import commands
from nextcord import Colour
import requests


url_agents = requests.get("https://valorant-api.com/v1/agents/").json()
url_weapons = requests.get("https://valorant-api.com/v1/weapons/").json()
uuid_agents = {}
uuid_weapons = {}
for agent in url_agents["data"]:
    uuid_agents[str(agent["displayName"])] = str(agent["uuid"])
for weapon in url_weapons["data"]:
    if weapon["displayName"] != "Melee":
        uuid_weapons[str(weapon["displayName"])] = str(weapon["uuid"])

class Valorant(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    @commands.cooldown(1,5,commands.BucketType.user)
    async def valorant(self,ctx):
        valorant_help = f'''```md
### Valorant ###

# Các lệnh
Agents: Thông tin về các vị tướng trong Valorant
Weapons: Thông tin về các loại vũ khí có trong Valorant
# Lệnh
{self.client.command_prefix}valorant agents
{self.client.command_prefix}valorant weapons
```'''
        await ctx.send(valorant_help)

    @valorant.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def agents(self,ctx):
        selectOption = []
        for name in uuid_agents:
            selectOption.append(nextcord.SelectOption(label=name,description=f'Thông tin tướng Valorant {name}'))
        choose = nextcord.ui.Select(placeholder='Chọn nhân vật Valorant',min_values=1,max_values=1,options=selectOption)
        view = nextcord.ui.View(timeout=60)
        async def embed(interaction,uuid):
            agent = requests.get(f'https://valorant-api.com/v1/agents/{uuid}?language=vi-VN').json()
            if agent["data"]["characterTags"] == None:
                type_agent = 'Không rõ'
            else:
                agent_type_join = [typ for typ in agent["data"]["characterTags"]]
                type_agent = ', '.join(agent_type_join)
            agent_abilities_join = [abilitie for abilitie in agent["data"]["abilities"]]
            abilities = ', '.join([ability['displayName'] for ability in agent_abilities_join])
            embed = nextcord.Embed(title=f'Thông tin nhân vật - {agent["data"]["displayName"]}',description=f'[Tổng quan](https://playvalorant.com/vi-vn/agents/{agent["data"]["displayName"].replace("/","-").lower()}/ "Thông tin nhân vật {agent["data"]["displayName"]}")\n{agent["data"]["description"]}',color=Colour.blurple(),timestamp=ctx.message.created_at)
            embed.add_field(name='Tên',value=agent["data"]["displayName"],inline=True)
            embed.add_field(name='Loại',value=type_agent,inline=True)
            embed.add_field(name='Các kỹ năng',value=abilities,inline=False)
            embed.set_thumbnail(url=agent["data"]["displayIcon"])
            embed.set_image(url=agent["data"]["fullPortraitV2"])
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await interaction.response.send_message(embed=embed,ephemeral=True)
        async def callback(interaction:nextcord.Interaction):
            for name in uuid_agents:
                if choose.values[0] == name:
                    uuid = uuid_agents[name]
                    await embed(interaction,uuid)
        choose.callback = callback
        view.add_item(choose)
        await ctx.send(f'Các nhân vật trong Valorant',view=view)

    @valorant.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def weapons(self,ctx):
        selectOption = []
        for name in uuid_weapons:
            selectOption.append(nextcord.SelectOption(label=name,description=f'Thông tin vũ khí Valorant {name}'))
        choose = nextcord.ui.Select(placeholder='Chọn vũ khí Valorant',min_values=1,max_values=1,options=selectOption)
        view = nextcord.ui.View(timeout=60)
        async def embed(interaction,uuid):
            weapon = requests.get(f'https://valorant-api.com/v1/weapons/{uuid}?language=vi-VN').json()
            embed = nextcord.Embed(title=f'Thông tin vũ khí - {weapon["data"]["displayName"]}',description=f'[Thông tin](https://playvalorant.com/vi-vn/arsenal/ "Thông tin vũ khí")',color=Colour.blurple(),timestamp=ctx.message.created_at)
            embed.add_field(name='Tên',value=weapon["data"]["displayName"],inline=True)
            embed.add_field(name='Loại',value=weapon["data"]["shopData"]["category"],inline=True)
            embed.add_field(name='Số đạn',value=str(weapon["data"]["weaponStats"]["magazineSize"])+" viên",inline=True)
            embed.add_field(name='Tốc độ bắn',value=weapon["data"]["weaponStats"]["fireRate"],inline=True)
            embed.add_field(name='Thời gian trang bị',value=str(weapon["data"]["weaponStats"]["equipTimeSeconds"])+" giây",inline=True)
            embed.add_field(name='Thời gian nạp đạn',value=str(weapon["data"]["weaponStats"]["reloadTimeSeconds"])+" giây",inline=True)
            embed.add_field(name='Giá tiền',value=weapon["data"]["shopData"]["cost"],inline=True)
            embed.set_image(url=weapon["data"]["displayIcon"])
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await interaction.response.send_message(embed=embed,ephemeral=True)
        async def callback(interaction:nextcord.Interaction):
            for name in uuid_weapons:
                if choose.values[0] == name:
                    uuid = uuid_weapons[name]
                    await embed(interaction,uuid)
        choose.callback = callback
        view.add_item(choose)
        await ctx.send(f'Các loại vũ khí trong Valorant',view=view)

def setup(client):
    client.add_cog(Valorant(client))
