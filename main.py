# Ultimate Bot - Discord Bot

# @author: honkaisenbai
# @bot: PuraGH
# @botID: 913700803628384306
# @code: Python
# @botLanguage: Vietnamese
# @botVersion: v1.3
# @botPrefix: $
# @from: Vietnam
# @mainModuleCode: nextcord


import datetime
import nextcord
from nextcord.ext import commands
from asyncio import sleep
from nextcord import Colour
import os
import json
import colorama
from colorama import Fore
from io import BytesIO
from PIL import Image,ImageFont,ImageDraw
colorama.init(autoreset=True)


config = json.load(open('./config.json','r',encoding='utf-8'))
intents = nextcord.Intents.all()
client = commands.Bot(command_prefix=config["prefix"],intents=intents,owner_id=770612800552042508,case_insensitive=True,description='PuraGH tạo bởi honkaisenbai')
client.remove_command('help')


async def status():
    with open('members.json','r',encoding='utf-8') as f:
        members = json.load(f)
    time = 5
    while True:
        await client.wait_until_ready()
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(name=f'với {len(members):,} người'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Activity(type=nextcord.ActivityType.listening,name=f'{client.command_prefix}help'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(name=f'với {len(client.guilds)} máy chủ'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(name='Secret Command'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Streaming(name='Youtube',url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))
        await sleep(32)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(name=f'Ping: {round(client.latency * 1000)}ms'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Activity(type=nextcord.ActivityType.listening,name=f'{client.command_prefix}update'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(name='BruhCraft'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(name='Discord'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Activity(type=nextcord.ActivityType.listening,name=f'{len(client.all_commands)} lệnh'))
        await sleep(time)
        await client.change_presence(status=nextcord.Status.online,activity=nextcord.Game(name='Minecraft'))
        await sleep(time)

@client.event
async def on_connect():
    print(Fore.YELLOW+'Connecting to Discord Server...\n')

@client.event
async def on_ready():
    print(Fore.GREEN+'Connected to Bot')
    print('-------------------------')
    print(f'User: {client.user}')
    print(f'Id: {client.user.id}')
    print(f'Prefix: {client.command_prefix}')
    print(f'Server: {len(client.guilds)}')
    print(f'Commands: {len(client.commands)}')
    print('-------------------------\n')
    while True:
        for guild in client.guilds:
            for member in guild.members:
                with open('members.json','r',encoding='utf-8') as f:
                    members = json.load(f)
                if not member.bot:
                    members.append(member.id)
                with open('members.json','w',encoding='utf-8') as f:
                    json.dump(members,f,indent=4)
        await sleep(216000)
client.loop.create_task(status())

@client.event
async def on_guild_join(guild:nextcord.Guild):
    channel_text = guild.text_channels[0]
    invite = await channel_text.create_invite(reason='Đừng xóa invite này ;-;')
    guild_support = client.get_guild(934727632933781535)
    channel = guild_support.get_channel(956531605894225920)
    embed = nextcord.Embed(title=f'Đã vào máy chủ {guild.name} - {guild.id}',colour=Colour.green())
    embed.set_thumbnail(url=guild.icon.url)
    embed.set_footer(text=guild.name,icon_url=guild.icon.url)
    await channel.send(content=invite.url,embed=embed)

@client.event
async def on_guild_remove(guild:nextcord.Guild):
    with open('./data/badwords.json','r',encoding='utf-8') as f:
        guilds = json.load(f)
    guilds.pop(str(guild.id))
    with open('./data/badwords.json','w',encoding='utf-8') as f:
        json.dump(guilds,f,indent=4,ensure_ascii=False)
    guild_support = client.get_guild(934727632933781535)
    channel = guild_support.get_channel(956531605894225920)
    embed = nextcord.Embed(title=f'Đã thoát máy chủ {guild.name} - {guild.id}',colour=Colour.red())
    embed.set_thumbnail(url=guild.icon.url)
    embed.set_footer(text=guild.name,icon_url=guild.icon.url)
    await channel.send(embed=embed)

@client.event
async def on_message(message:nextcord.Message):
    await client.process_commands(message)
    with open('./data/badwords.json','r',encoding='utf-8') as f:
        badwords = json.load(f)
    with open('./data/levels.json','r',encoding='utf-8') as f:
        levels = json.load(f)
    with open('./data/moneys.json','r',encoding='utf-8') as f:
        moneys = json.load(f)
    if not badwords.get(str(message.guild.id)):
        badwords[str(message.guild.id)] = {"bad_words":True,"list_bad_words":[]}
        with open('./data/badwords.json','w',encoding='utf-8') as f:
            json.dump(badwords,f,indent=4,ensure_ascii=False)
    elif badwords[str(message.guild.id)]["bad_words"] == True:
        bad = []
        for badwords in badwords[str(message.guild.id)]["list_bad_words"]:
            if badwords in message.content.casefold():
                bad.append(True)
        if True == any(bad):
            await message.channel.send(f'{message.author.mention}, cẩn thận từ ngữ trước khi nói!',delete_after=3)
    if message.author.bot:
        return
    elif not levels.get(str(message.author.id)):
        levels[str(message.author.id)] = {"level":1,"exp":0}
        with open('./data/levels.json','w',encoding='utf-8') as f:
            json.dump(levels,f,indent=4)
        if not moneys.get(str(message.author.id)):
            moneys[str(message.author.id)] = {"moneys":100000}
            with open('./data/moneys.json','w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
    else:
        levels[str(message.author.id)]["exp"] += 1
        with open('./data/levels.json', 'w',encoding='utf-8') as f:
            json.dump(levels,f,indent=4)
        if levels[str(message.author.id)]["exp"] == levels[str(message.author.id)]["level"] * 100:
            levels[str(message.author.id)]["level"] += 1
            levels[str(message.author.id)]["exp"] = 0
            moneys[str(message.author.id)]["moneys"] += levels[str(message.author.id)]["level"] * 100000
            with open('./data/moneys.json','w',encoding='utf-8') as f:
                json.dump(moneys,f,indent=4)
            with open('./data/levels.json','w',encoding='utf-8') as f:
                json.dump(levels,f,indent=4)
            base = Image.open('./data/level_up.png').convert('RGBA')
            pfp = message.author.display_avatar.with_size(128)
            data = BytesIO(await pfp.read())
            pfp = Image.open(data).convert('RGBA')
            pfp = pfp.resize((225,225),Image.LANCZOS).convert('RGBA')
            draw = ImageDraw.Draw(base)
            font = ImageFont.truetype('./data/arial.ttf',size=60)
            level_font = ImageFont.truetype('./data/arial.ttf',size=120)
            font_money = ImageFont.truetype('./data/arial.ttf',size=50)
            money_add = levels[str(message.author.id)]["level"] * 100000
            draw.text((304,22),'Tăng Cấp!',font=font)
            draw.text((389,110),str(levels[str(message.author.id)]["level"]),font=level_font)
            draw.text((631,33),f"+ {money_add:,} PuraCN",font=font_money)
            base.paste(pfp,(31,23),pfp)
            with BytesIO() as a:
                base.save(a,'PNG')
                a.seek(0)
                file = nextcord.File(a,'level_up.png')
                await message.channel.send(file=file)

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        embed = nextcord.Embed(title=f'❌ Không rõ lệnh cần dùng!',color=Colour.red())
        await ctx.reply(embed=embed,delete_after=3)
    elif isinstance(error,commands.NoPrivateMessage):
        embed9 = nextcord.Embed(title=f'❌ Lệnh chỉ có thể dùng trong máy chủ!',color=Colour.red())
        await ctx.reply(embed=embed9,delete_after=3)
    elif isinstance(error,commands.PrivateMessageOnly):
        embed10 = nextcord.Embed(title='❌ Lệnh chỉ có thể dùng trong nhắn riêng!',color=Colour.red())
        await ctx.reply(embed=embed10,delete_after=3)
    elif isinstance(error,commands.MissingPermissions):
        embed3 = nextcord.Embed(title=f'❌ Bạn không có quyền để dùng lệnh đó!',description=f'Dùng `{client.command_prefix}perms` để biết quyền cần thiết của lệnh',color=Colour.red())
        await ctx.reply(embed=embed3,delete_after=3)
    elif isinstance(error,commands.BotMissingPermissions):
        embed5 = nextcord.Embed(title=f'❌ Tôi không có quyền để làm việc đó!',description=f'Dùng `{client.command_prefix}perms` để biết quyền cần thiết của lệnh',color=Colour.red())
        await ctx.reply(embed=embed5,delete_after=3)
    elif isinstance(error,commands.MemberNotFound):
        embed1 = nextcord.Embed(title=f'❌ Không rõ thành viên!',color=Colour.red())
        await ctx.reply(embed=embed1,delete_after=3)
    elif isinstance(error,commands.UserNotFound):
        embed2 = nextcord.Embed(title=f'❌ Không rõ người dùng!',color=Colour.red())
        await ctx.reply(embed=embed2,delete_after=3)
    elif isinstance(error,commands.RoleNotFound):
        embed4 = nextcord.Embed(title=f'❌ Không rõ vai trò!',color=Colour.red())
        await ctx.reply(embed=embed4,delete_after=3)
    elif isinstance(error,commands.NotOwner):
        embed7 = nextcord.Embed(title=f'❌ Không rõ lệnh cần dùng!',color=Colour.red())
        await ctx.reply(embed=embed7,delete_after=3)
    elif isinstance(error,commands.DisabledCommand):
        embed8 = nextcord.Embed(title=f'❌ Lệnh hiện đang bảo trì!',color=Colour.red())
        await ctx.reply(embed=embed8,delete_after=3)
    elif isinstance(error,commands.BadArgument):
        embed6 = nextcord.Embed(title=f'❌ Không rõ cú pháp!',color=Colour.red())
        await ctx.reply(embed=embed6,delete_after=3)
    elif isinstance(error,commands.CommandOnCooldown):
        embed11 = nextcord.Embed(title=f'❌ Đang trong thời gian chờ, vui lòng chờ {str(error).replace("You are on cooldown. Try again in ","")}!',color=Colour.red())
        await ctx.reply(embed=embed11,delete_after=3)
    elif isinstance(error,commands.ChannelNotFound):
        embed11 = nextcord.Embed(title=f'❌ Không rõ kênh!',color=Colour.red())
        await ctx.reply(embed=embed11,delete_after=3)
    else:
        guild = client.get_guild(934727632933781535)
        channel = guild.get_channel(956478425302982727)
        embed = nextcord.Embed(title='Lỗi!',description=error,color=Colour.red(),timestamp=ctx.message.created_at)
        await channel.send(embed=embed)
        raise error

@client.event
async def on_message_delete(message:nextcord.Message):
    with open('./data/sniped_messages.json','r',encoding='utf-8') as f:
        sniped_messages = json.load(f)
    if not message.author.bot:
        content = str(message.content)
        author = message.author.id
        time = datetime.datetime.now()
        time = f"{time.day}/{time.month}/{time.year} - {time.hour}:{time.minute}:{time.second}"
        if not sniped_messages.get(str(message.guild.id)):
            sniped_messages[str(message.guild.id)] = {str(message.channel.id):{"content":content,"author":author,"time":time}}
            with open('./data/sniped_messages.json','w',encoding='utf-8') as f:
                json.dump(sniped_messages,f,indent=4)
        elif not sniped_messages[str(message.guild.id)].get(str(message.channel.id)):
            with open('./data/sniped_messages.json','r',encoding='utf-8') as f:
                sniped_messages = json.load(f)
            sniped_messages[str(message.guild.id)][str(message.channel.id)] = {"content":content,"author":author,"time":time}
            with open('./data/sniped_messages.json','w',encoding='utf-8') as f:
                json.dump(sniped_messages,f,indent=4)
        else:
            with open('./data/sniped_messages.json','r',encoding='utf-8') as f:
                sniped_messages = json.load(f)
            sniped_messages[str(message.guild.id)][str(message.channel.id)]["content"] = content
            sniped_messages[str(message.guild.id)][str(message.channel.id)]["author"] = author
            sniped_messages[str(message.guild.id)][str(message.channel.id)]["time"] = time
            with open('./data/sniped_messages.json','w',encoding='utf-8') as f:
                json.dump(sniped_messages,f,indent=4)

@client.command()
async def wqueioruieowerw(ctx):
    await ctx.message.add_reaction('✅')
    embed = nextcord.Embed(title='Test',description='Test again',color=Colour.random())
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('✅')

@client.command()
async def buttonokdsjka(ctx):
    test = nextcord.ui.Button(label='Link',url='https://www.youtube.com/watch?v=NtoMyB8XcQU',style=nextcord.ButtonStyle.link)
    test2 = nextcord.ui.Button(label='Button 2',style=nextcord.ButtonStyle.green)
    async def callback(interaction:nextcord.Interaction):
        await interaction.response.send_message('test2',ephemeral=True)
    test2.callback = callback
    view = nextcord.ui.View(timeout=10)
    view.add_item(test)
    view.add_item(test2)
    await ctx.send('BUTTONNNNN',view=view)

@client.command()
async def dropdjsalds(ctx):
    selectOption = [
        nextcord.SelectOption(label='Python',value='script.py',description='Code Python'),
        nextcord.SelectOption(label='JavaScript',value='script.js',description='Code JavaScript')
    ]
    DropDown = nextcord.ui.Select(placeholder='Select your language',min_values=1,max_values=1,options=selectOption)
    view = nextcord.ui.View(timeout=60)
    async def dropdown_callback(interaction:nextcord.Interaction):
        if DropDown.values[0] == 'script.py':
            await interaction.response.send_message('Python')
        elif DropDown.values[0] == 'script.js':
            await interaction.response.send_message('JavaScript')
    DropDown.callback = dropdown_callback
    view.add_item(DropDown)
    await ctx.send(f'Code',view=view)

@client.command()
async def formatdt(ctx):
    await ctx.send(nextcord.utils.format_dt(datetime.datetime.now(),'R'))

@client.command()
@commands.is_owner()
async def reload(ctx,type_command=None):
    if type_command == None:
        list_dir = [dire for dire in os.listdir('./commands')]
        dirs = ', '.join([typecommand for typecommand in list_dir])
        embed = nextcord.Embed(title='Danh sách các loại lệnh',description=dirs,color=Colour.green())
        await ctx.send(embed=embed)
    else:
        if not os.path.isdir(f'./commands/{type_command}'):
            embed = nextcord.Embed(title='❌ Không rõ loại lệnh!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            reloaded_commands = []
            for command in os.listdir(f'./commands/{type_command}'):
                if command.endswith('.py'):
                    client.reload_extension(f'commands.{type_command}.{command[:-3]}')
                    reloaded_commands.append(command)
            listcommands = [command for command in reloaded_commands]
            commands_list = ', '.join([command[:-3] for command in listcommands])
            await ctx.message.delete()
            embed = nextcord.Embed(title=f'Đã reload tất cả các lệnh loại {type_command}',description=commands_list,color=Colour.green())
            await ctx.send(embed=embed,delete_after=3)

import asyncio
@client.command()
async def wait(ctx):
    message = '**Waiting for multiple events**\n'
    response = await ctx.send(content=message)
    await response.add_reaction("🔄")
    while True:
        tasks = [
            asyncio.create_task(client.wait_for("reaction_add",check=lambda reaction,user:reaction.message.id == response.id,timeout=10),name="radd"),
            asyncio.create_task(client.wait_for("reaction_remove",check=lambda reaction,user:reaction.message.id == response.id,timeout=10),name="rrem"),
            asyncio.create_task(client.wait_for("message",timeout=10),name="mes")
        ]
        done,pending = await asyncio.wait(tasks,return_when=asyncio.FIRST_COMPLETED)
        finished:asyncio.Task = list(done)[0]
        for task in pending:
            try:
                task.cancel()
            except asyncio.CancelledError:
                pass
        action = finished.get_name()
        try:
            result = finished.result()
        except asyncio.TimeoutError:
            await response.edit(content=message+"----Timed Out----")
            return
        if action == "radd":
            reaction,user=result
            message+=f"{reaction} added by {user}\n"
            await response.edit(content=message)
        elif action == "rrem":
            reaction,user=result
            message+=f"{reaction} removed by {user}\n"
            await response.edit(content=message)
        elif action == "mes":
            msg:nextcord.Message=result
            message+=f'**{msg.content}** sent by {msg.author}\n'
            await response.edit(content=message)


if __name__ == '__main__':
    try:
        total_commands = []
        for type_commands in os.listdir('commands'):
            for command in os.listdir(f'commands/{type_commands}'):
                if command.endswith('.py'):
                    client.load_extension(f'commands.{type_commands}.{command[:-3]}')
                    total_commands.append(command[:-3])
        print(Fore.YELLOW+f'Loaded total {len(total_commands)} commands\n')
    except Exception as error:
        print(Fore.RED+f'Lỗi không thể load: {error}')
    client.run(config["token"])