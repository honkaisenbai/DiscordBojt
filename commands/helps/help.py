import nextcord
from nextcord.ext import commands
from nextcord import Colour
import json


config = json.load(open(__file__.replace('commands\helps\help.py','config.json'),'r',encoding='utf-8'))

class Help(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        guild_support = self.client.get_guild(934727632933781535)
        l_help = '`,`'.join([command for command in config["commandsHelp"]["helps"]])
        l_fun = '`,`'.join([command for command in config["commandsHelp"]["funs"]])
        l_money = '`,`'.join([command for command in config["commandsHelp"]["moneys"]])
        l_information = '`,`'.join([command for command in config["commandsHelp"]["informations"]])
        l_other = '`,`'.join([command for command in config["commandsHelp"]["others"]])
        l_manager = '`,`'.join([command for command in config["commandsHelp"]["managers"]])
        await ctx.message.add_reaction('✅')
        embed = nextcord.Embed(description=f'Cần tìm hiểu rõ hơn về lệnh?\nTham gia máy chủ trợ giúp [{guild_support.name}]({config["guildlink"]} "Máy chủ trợ giúp")\nDùng `{self.client.command_prefix}help <Lệnh>`',color=Colour.yellow())
        embed.set_author(name=f'Tất cả các lệnh của bot - {self.client.user}',icon_url=ctx.author.display_avatar)
        embed.add_field(name="❓ Help",value=l_help,inline=False)
        embed.add_field(name='😆 Fun',value=l_fun,inline=False)
        embed.add_field(name='🪙 Tiền',value=l_money,inline=False)
        embed.add_field(name=f'📃 Thông tin',value=l_information,inline=False)
        embed.add_field(name='🎲 Khác',value=l_other,inline=False)
        embed.add_field(name='⚙️ Quản lý',value=l_manager,inline=False)
        embed.set_thumbnail(url=self.client.user.avatar)
        await ctx.send(embed=embed)

    # <>

    @help.command()
    async def update(self,ctx):
        update_help = f'''```md
### Update ###

# Thông tin
Hiện cập nhập của bot về lệnh, sửa lỗi, nhật ký cập nhập,.v.v...
# Lệnh
{self.client.command_prefix}update
```'''
        await ctx.send(update_help)

    @help.command()
    async def request(self,ctx):
        request_help = f'''```md
### Request ###

# Thông tin
Gửi yêu cầu/ý kiến tới hệ thống để xem xét và trả lời
# Lưu ý
Không được gửi yêu cầu khi không cần thiết, gửi là chết à nhen;-;
# Lệnh
{self.client.command_prefix}request <Yêu cầu/Ý kiến>
# Ví dụ
{self.client.command_prefix}request Đây là yêu cầu (Không nên bắt chước)
```'''
        await ctx.send(request_help)

    @help.command()
    async def trans(self,ctx):
        trans_help = f'''```md
### Translate ###

# Thông tin
Dịch nội dung sang ngôn ngữ cần dịch
# Lưu ý
Mã ngôn ngữ là ngôn ngữ cần dịch từ nội dung qua ngôn ngữ đó
# Lệnh
{self.client.command_prefix}trans <Mã ngôn ngữ> <Nội dung>
{self.client.command_prefix}trans lang
# Ví dụ
{self.client.command_prefix}trans vi Hello everyone
{self.client.command_prefix}trans en Chào mọi người
```'''
        await ctx.send(trans_help)

    @help.command()
    async def info(self,ctx):
        info_help = f'''```md
### Info ###

# Thông tin
Hiện thông tin về bot
# Lệnh
{self.client.command_prefix}info
```'''
        await ctx.send(info_help)

    @help.command()
    async def credits(self,ctx):
        credits_help = f'''```md
### Credits ###

# Thông tin
Hiện tất cả người đóng góp xây dựng bot
# Lệnh
{self.client.command_prefix}credits
```'''
        await ctx.send(credits_help)

    @help.command()
    async def perms(self,ctx):
        perms = f'''```md
### Perms ###

# Thông tin
Hiện quyền cần thiết của những lệnh cần quyền
# Lưu ý
Những quyền hiện ra là những quyền cần thiết cho người dùng lệnh và cho cả Bot để thực thi lệnh
# Lệnh
{self.client.command_prefix}perms
```'''
        await ctx.send(perms)

    @help.command()
    async def meme(self,ctx):
        meme_help = f'''```md
### Meme ###

# Thông tin
Ngẫu nhiên meme được lấy từ Reddit
# Lệnh
{self.client.command_prefix}meme
```'''
        await ctx.send(meme_help)

    @help.command()
    async def profile(self,ctx):
        profile_help = f'''```md
### Profile ###

# Thông tin
Hiện thông tin người dùng của thành viên
# Lệnh
{self.client.command_prefix}profile <Thành viên>
{self.client.command_prefix}profile
# Ví dụ
{self.client.command_prefix}profile {ctx.author.name}
```'''
        await ctx.send(profile_help)

    @help.command()
    async def avatar(self,ctx):
        avatar_help = f'''```md
### Avatar ###

# Thông tin
Hiện avatar người dùng của thành viên
# Lệnh
{self.client.command_prefix}avatar <Thành viên>
{self.client.command_prefix}avatar
# Ví dụ
{self.client.command_prefix}avatar {ctx.author.name}
```'''
        await ctx.send(avatar_help)

    @help.command()
    async def roll(self,ctx):
        roll_help = f'''```md
### Roll ###

# Thông tin
Ngẫu nhiên con số từ 1 đến 100
# Lệnh
{self.client.command_prefix}roll
```'''
        await ctx.send(roll_help)

    @help.command()
    async def reminder(self,ctx):
        reminder_help = f'''```md
### Reminder ###

# Thông tin
Đặt lời nhắc nhở
# Thời gian
1s(1 giây), 1m(1 phút), 1h(1 giờ), 1d(1 ngày)
# Lệnh
{self.client.command_prefix}reminder <Thời gian> <Lời nhắc>
{self.client.command_prefix}reminder <Thời gian>
# Ví dụ
{self.client.command_prefix}reminder 1m Ping @everyone:> (Khuyến cáo không nên làm theo nếu trong server có nhiều người ._.)
```'''
        await ctx.send(reminder_help)
    
    @help.command()
    async def timeout(self,ctx):
        timeout_help = f'''```md
### Timeout ###

# Thông tin
Bật hạn chế thời gian cho thành viên
# Thời gian
1s(1 giây), 1m(1 phút), 1h(1 giờ), 1d(1 ngày)
# Lệnh
{self.client.command_prefix}timeout <Thành viên> <Thời gian> <Lý do>
{self.client.command_prefix}timeout <Thành viên> <Thời gian>
# Ví dụ
{self.client.command_prefix}timeout {ctx.author.name} 1m Spam là chết:)
```'''
        await ctx.send(timeout_help)

    @help.command()
    async def untimeout(self,ctx):
        untimeout_help = f'''```md
### UnTimeout ###

# Thông tin
Tắt hạn chế thời gian cho thành viên
# Lệnh
{self.client.command_prefix}untimeout <Thành viên>
# Ví dụ
{self.client.command_prefix}untimeout {ctx.author.name}
```'''
        await ctx.send(untimeout_help)

    @help.command()
    async def invite(self,ctx):
        add_help = f'''```md
### Invite ###

# Thông tin
Hiện đường dẫn thêm bot vào máy chủ
# Lệnh
{self.client.command_prefix}invite
```'''
        await ctx.send(add_help)

    @help.command()
    async def seedmc(self,ctx):
        seedmc_help = f'''```md
### SeedMC ###

# Thông tin
Ngẫu nhiên một seed map minecraft
# Lệnh
{self.client.command_prefix}seedmc
```'''
        await ctx.send(seedmc_help)

    @help.command()
    async def nick(self,ctx):
        nick_help = f'''```md
### Nick ###

# Thông tin
Đặt biệt danh cho thành viên
# Lệnh
{self.client.command_prefix}nick <Thành viên> <Biệt danh>
{self.client.command_prefix}nick <Thành viên>
# Ví dụ
{self.client.command_prefix}nick {ctx.author.name} Im GAY
```'''
        await ctx.send(nick_help)

    @help.command()
    async def ban(self,ctx):
        ban_help = f'''```md
### Ban ###

# Thông tin
Cấm người dùng khỏi máy chủ
# Lệnh
{self.client.command_prefix}ban <Người dùng> <Lý do>
{self.client.command_prefix}ban <Người dùng>
# Ví dụ
{self.client.command_prefix}ban {ctx.author.name} Thích vậy ó:>
```'''
        await ctx.send(ban_help)

    @help.command()
    async def unban(self,ctx):
        unban_help = f'''```md
### Unban ###

# Thông tin
Gỡ cấm người dùng nào đó trên máy chủ
# Lệnh
{self.client.command_prefix}unban <ID Người dùng>
# Ví dụ
{self.client.command_prefix}unban {ctx.author.id}
```'''
        await ctx.send(unban_help)

    @help.command()
    async def kick(self,ctx):
        kick_help = f'''```md
### Kick ###

# Thông tin
Đá thành viên khỏi máy chủ
# Lệnh
{self.client.command_prefix}kick <Thành viên> <Lý do>
{self.client.command_prefix}kick <Thành viên>
# Ví dụ
{self.client.command_prefix}kick {ctx.author.name} Ehehe:>
```'''
        await ctx.send(kick_help)

    @help.command()
    async def mute(self,ctx):
        mute_help = f'''```md
### Mute ###

# Thông tin
Tắt tiếng thành viên trong máy chủ
# Lệnh
{self.client.command_prefix}mute <Thành viên> <Lý do>
{self.client.command_prefix}mute <Thành viên>
# Ví dụ
{self.client.command_prefix}mute {ctx.author.name} Buồn đi:>
```'''
        await ctx.send(mute_help)

    @help.command()
    async def unmute(self,ctx):
        unmute_help = f''''```md
### UnMute ###

# Thông tin
Gỡ tắt tiếng thành viên đã bị tắt tiếng
# Lệnh
{self.client.command_prefix}unmute <Thành viên>
# Ví dụ
{self.client.command_prefix}unmute {ctx.author.name}
```'''
        await ctx.send(unmute_help)

    @help.command()
    async def lock(self,ctx):
        lock_help = f'''```md
### Lock ###

# Thông tin
Khóa kênh nhắn tin
# Lệnh
{self.client.command_prefix}lock
```'''
        await ctx.send(lock_help)

    @help.command()
    async def unlock(self,ctx):
        unlock_help = f'''```md
### UnLock ###

# Thông tin
Gỡ khóa kênh nhắn tin
# Lệnh
{self.client.command_prefix}unlock
```'''
        await ctx.send(unlock_help)

    @help.command()
    async def hack(self,ctx):
        hack_help = f'''```md
### Hack ###

# Thông tin
Trở thành hacker 🧑‍💻 và đi hack người khác:> (Dùng chơi cho vui :3)
# Lệnh
{self.client.command_prefix}hack <Thành viên>
# Ví dụ
{self.client.command_prefix}hack {ctx.author.name}
```'''
        await ctx.send(hack_help)

    @help.command()
    async def ping(self,ctx):
        ping_help = f'''```md
### Ping ###

# Thông tin
Xem độ trễ của bot (Ping bot)
# Lệnh
{self.client.command_prefix}ping
```'''
        await ctx.send(ping_help)

    @help.command()
    async def anime(self,ctx):
        anime_help = f'''```md
### Anime ###

# Thông tin
Xem thông tin về tên bộ anime cần tìm
# Lệnh
{self.client.command_prefix}anime <Tên bộ anime>
# Ví dụ
{self.client.command_prefix}anime SLIME đó:>
```'''
        await ctx.send(anime_help)

    @help.command()
    async def animechar(self,ctx):
        animechar_help = f'''```md
### AnimeChar ###

# Thông tin
Xem thông tin về tên nhân vật anime
# Lệnh
{self.client.command_prefix}animechar <Tên nhân vật anime>
# Ví dụ
{self.client.command_prefix}animechar SAKURA;-;
```'''
        await ctx.send(animechar_help)

    @help.command()
    async def animenew(self,ctx):
        animenew_help = f'''```md
### AnimeNew ###

# Thông tin
Xem thông tin về bộ anime mới nhất
# Lệnh
{self.client.command_prefix}animenew
```'''
        await ctx.send(animenew_help)

    @help.command()
    async def covid(self,ctx):
        covid_help = f'''```md
### Covid ###

# Thông tin
Xem tình trạng covid-19 ở một vùng nào đó
# Lệnh
{self.client.command_prefix}covid <Tên vùng>
# Ví dụ
{self.client.command_prefix}covid VIỆT NAM
```'''
        await ctx.send(covid_help)

    @help.command()
    async def svmc(self,ctx):
        svmc_help = f'''```md
### SvMC ###

# Thông tin
Xem thông tin về máy chủ minecraft theo IP
# Lưu ý
Sẽ có vài máy chủ minecraft mà bot không tìm được, có thể là do IP máy chủ không đúng hoặc máy chủ thuộc cái gì đó như heromc.net hay minefc.com ;-;
# Lệnh
{self.client.command_prefix}svmc <Địa chỉ máy chủ>
# Ví dụ
{self.client.command_prefix}svmc hypixel.net
```'''
        await ctx.send(svmc_help)

    @help.command()
    async def guild(self,ctx):
        guild_help = f'''```md
### Guild ###

# Thông tin
Xem thông tin về máy chủ
# Lệnh
{self.client.command_prefix}guild
```'''
        await ctx.send(guild_help)

    @help.command()
    async def role(self,ctx):
        role_help = f'''```md
### Role ###

# Thông tin
Quản lý vai trò máy chủ, thành viên
# Lệnh
{self.client.command_prefix}role
```'''
        await ctx.send(role_help)

    @help.command()
    async def badwords(self,ctx):
        badwords_help = f'''```md
### Bad Words ###

# Thông tin
Quản lý ngôn từ khi nhắn trong máy chủ
# Lệnh
{self.client.command_prefix}badwords
```'''
        await ctx.send(badwords_help)

    @help.command()
    async def math(self,ctx):
        math_help = f'''```md
### Math ###

# Thông tin
Dùng để tính toán gần giống với máy tính
# Lưu ý
Chỉ cộng trừ nhân chia thui ;-;
# Lệnh
{self.client.command_prefix}math <Phép tính>
# Ví dụ
{self.client.command_prefix}math 12*2
{self.client.command_prefix}math (50+20)-60
```'''
        await ctx.send(math_help)

    @help.command()
    async def clear(self,ctx):
        clear_help = f'''```md
### Clear ###

# Thông tin
Xóa số lượng tin nhắn trên kênh tin nhắn
# Lưu ý
Không xóa lượng trên 100 tin nhắn được đâu à nhe:3
# Lệnh
{self.client.command_prefix}clear <Số lượng tin nhắn>
# Ví dụ
{self.client.command_prefix}clear 100
```'''
        await ctx.send(clear_help)

    @help.command()
    async def qrcode(self,ctx):
        qrcode_help = f'''```md
### QR Code ###

# Thông tin
Tạo mã QR Code với đường dẫn/tin nhắn(link, url, text)
# Lưu ý
Đừng tạo mã với đường dẫn độc, không thì chết ráng chịu -_-
# Lệnh
{self.client.command_prefix}qrcode <Đường dẫn/Tin nhắn>
# Ví dụ
{self.client.command_prefix}qrcode I LOVE YOU
```'''
        await ctx.send(qrcode_help)

    @help.command()
    async def file(self,ctx):
        file_help = f'''```md
### File ###

# Thông tin
Lưu trữ tập tin vào thư viện máy chủ của bạn
# Lưu ý
Nếu mất tập tin gì đó thì lỗi do hệ thống hoặc bạn;-;
# Lệnh
{self.client.command_prefix}file
```'''
        await ctx.send(file_help)

    @help.command()
    async def cash(self,ctx):
        cash_help = f'''```md
### Cash ###

# Thông tin
Hiện số tiền của bạn
# Lệnh
{self.client.command_prefix}cash
```'''
        await ctx.send(cash_help)

    @help.command()
    async def slots(self,ctx):
        slots_help = f'''```md
### Slots ###

# Thông tin
Chơi số may mắn để kiếm tiền:>
# Lệnh
{self.client.command_prefix}slots <Số tiền>
# Ví dụ
{self.client.command_prefix}slots 1000
```'''
        await ctx.send(slots_help)

    @help.command()
    async def give(self,ctx):
        give_help = f'''```md
### Give ###

# Thông tin
Tặng số tiền cho thành viên
# Lệnh
{self.client.command_prefix}give <Thành viên> <Số tiền>
# Ví dụ
{self.client.command_prefix}give {ctx.author.name} 20000
```'''
        await ctx.send(give_help)

    @help.command()
    async def cfg(self,ctx):
        cfg_help = f'''```md
### Coin Flip(G) ###

# Thông tin
Chơi mặt trên/dưới của đồng xu để kiếm tiền >_<
# Lệnh
{self.client.command_prefix}cfg <Số tiền> <Mặt xu>
# Ví dụ
{self.client.command_prefix}cfg 1000 u
{self.client.command_prefix}cfg 1000 d
```'''
        await ctx.send(cfg_help)

    @help.command()
    async def skins(self,ctx):
        skins_help = f'''```md
### Skins ###

# Thông tin
Tìm skin(hoặc áo choàng) theo tên người dùng trong Minecraft
# Lệnh
{self.client.command_prefix}skins <Tên người dùng>
# Ví dụ
{self.client.command_prefix}skins Dream
```'''
        await ctx.send(skins_help)

    @help.command()
    async def level(self,ctx):
        level_help = f'''```md
### Level ###

# Thông tin
Xem cấp độ của bạn
# Lệnh
{self.client.command_prefix}level
```'''
        await ctx.send(level_help)

    @help.command()
    async def valorant(self,ctx):
        valorant_help = f'''```md
### Valorant ###

# Thông tin
Xem thông tin về những thứ thuộc game Valorant(Tướng, vũ khí,...)
# Lệnh
{self.client.command_prefix}valorant
```'''
        await ctx.send(valorant_help)

    @help.command()
    async def activity(self,ctx):
        voices = [voice for voice in ctx.guild.voice_channels]
        voice_exam = voices[0]
        activity_help = f'''```md
### Activity ###

# Thông tin
Tạo hoạt động cho kênh thoại
# Lệnh
{self.client.command_prefix}activity <Kênh thoại>
# Ví dụ
{self.client.command_prefix}activity {voice_exam}
```'''
        await ctx.send(activity_help)

    @help.command()
    async def snipe(self,ctx):
        snipe_help = f'''```md
### Snipe ###

# Thông tin
Hiển thị tin nhắn đã xóa gần đây nhất của kênh dùng lệnh
# Lệnh
{self.client.command_prefix}snipe
```'''
        await ctx.send(snipe_help)

def setup(client):
    client.add_cog(Help(client))