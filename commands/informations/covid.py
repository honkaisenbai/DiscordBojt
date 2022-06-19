import nextcord
from nextcord.ext import commands
from nextcord import Colour
import requests


class Covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(invoke_without_command=True)
    async def covid(self,ctx,*, countryName=None):
        if countryName is None:
            embed = nextcord.Embed(title="❌ Vui lòng điền tên quốc gia!", color=Colour.red)
            await ctx.send(embed=embed,delete_after=3)
        else:
            url = f"https://disease.sh/v3/covid-19/countries/{countryName}"
            try:
                stats = requests.get(url)
                json_stats = stats.json()
                country = json_stats["country"]
                totalCases = json_stats["cases"]
                todayCases = json_stats["todayCases"]
                totalDeaths = json_stats["deaths"]
                todayDeaths = json_stats["todayDeaths"]
                recovered = json_stats["recovered"]
                todayRecovered = json_stats["todayRecovered"]
                flag_country = json_stats["countryInfo"]["flag"]
            except:
                embed = nextcord.Embed(title="❌ Không rõ tên quốc gia hoặc tên quốc gia không phù hợp!", color=Colour.red())
                embed.add_field(name=':bookmark: Ví dụ',value='vietnam, vn, japan, thailand, uk, usa, ...')
                await ctx.reply(embed=embed,delete_after=3)
            embed = nextcord.Embed(title=f"Tình trạng Covid-19 ở {country}", description="Thông tin này có thể sẽ không chính xác ngay bây giờ(vì qua một thời gian số lượng có thể sẽ tăng lên)", color=Colour.blurple(), timestamp=ctx.message.created_at)
            embed.add_field(name="Tổng số trường hợp", value=totalCases, inline=True)
            embed.add_field(name="Số trường hợp hôm nay", value=todayCases, inline=True)
            embed.add_field(name="Tổng số người chết", value=totalDeaths, inline=True)
            embed.add_field(name="Số người chết hôm nay", value=todayDeaths, inline=True)
            embed.add_field(name="Số người được chữa trị hôm nay", value=todayRecovered, inline=True)
            embed.add_field(name="Tổng số người được chữa trị", value=recovered, inline=True)
            embed.set_thumbnail(url=flag_country)
            embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
            await ctx.send(embed=embed)

    @covid.command()
    async def all(self,ctx):
        url = "https://disease.sh/v3/covid-19/all"
        stats = requests.get(url)
        json_stats = stats.json()
        totalCases = json_stats["cases"]
        todayCases = json_stats["todayCases"]
        totalDeaths = json_stats["deaths"]
        todayDeaths = json_stats["todayDeaths"]
        recovered = json_stats["recovered"]
        todayRecovered = json_stats["todayRecovered"]
        embed = nextcord.Embed(title=f"Tình trạng Covid-19 thế giới", description="Thông tin này có thể sẽ không chính xác ngay bây giờ(vì qua một thời gian số lượng có thể sẽ tăng lên)", color=Colour.blurple(), timestamp=ctx.message.created_at)
        embed.add_field(name="Tổng số trường hợp", value=totalCases, inline=True)
        embed.add_field(name="Số trường hợp hôm nay", value=todayCases, inline=True)
        embed.add_field(name="Tổng số người chết", value=totalDeaths, inline=True)
        embed.add_field(name="Số người chết hôm nay", value=todayDeaths, inline=True)
        embed.add_field(name="Số người được chữa trị hôm nay", value=todayRecovered, inline=True)
        embed.add_field(name="Tổng số người được chữa trị", value=recovered, inline=True)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/944030840302755841/944031757345357864/2Q.png")
        embed.set_footer(text=ctx.author,icon_url=ctx.author.display_avatar)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Covid(client))
