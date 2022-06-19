import nextcord
from nextcord.ext import commands
from nextcord import Colour
import animec


class Anime(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def anime(self,ctx,*,query=None):
        try:
            anime = animec.Anime(str(query))
        except:
            embed = nextcord.Embed(title=f"❌ Không thể tìm bộ anime với tên `{query}`",color=Colour.red())
            await ctx.reply(embed=embed)
        if query == None:
            embed = nextcord.Embed(title='❌ Thiếu tên anime cần tìm kiếm!',color=Colour.red())
            await ctx.reply(embed=embed)
        else:
            nsfw = anime.is_nsfw()
            if nsfw == True:
                nsfw_truefalse = "Có"
                anime_poster = 'https://cdn.discordapp.com/attachments/944030840302755841/959438820514869279/unknown.png'
            else:
                anime_poster = anime.poster
                nsfw_truefalse = "Không"
            anime_status = str(anime.status)
            if anime_status == "Finished Airing":
                anime_status = "Đã xong"
            elif anime_status == "Currently Airing":
                anime_status = "Đang phát sóng"
            if anime.episodes == "Unknown":
                anime_episodes = 'Không rõ'
            else:
                anime_episodes = anime.episodes
            embed = nextcord.Embed(title=f'Thông tin về anime {anime.name}',description=f'[Thông tin]({anime.url} "Dẫn bạn đến web thông tin về anime")',color=Colour.green(),timestamp=ctx.message.created_at)
            embed.add_field(name='Trạng thái',value=anime_status,inline=True)
            embed.add_field(name='Khởi chiếu',value=anime.aired,inline=True)
            embed.add_field(name='Số tập',value=anime_episodes,inline=True)
            embed.add_field(name='Số lượt thích',value=anime.favorites,inline=True)
            embed.add_field(name='Hạng phổ biến',value=anime.popularity,inline=True)
            embed.add_field(name='NSFW? (Nội dung không an toàn)',value=nsfw_truefalse,inline=True)
            embed.set_image(url=anime_poster)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Anime(client))
