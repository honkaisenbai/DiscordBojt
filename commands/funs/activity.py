import nextcord
from nextcord.ext import commands
from nextcord.ext.activities import Activity as activities
from nextcord import Colour


class Activity(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.cooldown(1,5,commands.BucketType.user)
    async def activity(self,ctx,channel:nextcord.VoiceChannel=None):
        free_games = {
            "betrayal.io": activities.betrayal,
            "fishington.io": activities.fishington,
            "youtube": activities.youtube,
            "doodle": activities.doodle,
            "sketch": activities.sketch,
            "word_snacks": activities.word_snacks,
            "blazing_8s": activities.blazing,
            "putt_party": activities.putt_party,
            "land-io": activities.land_io
        }
        boosted_games = {
            "poker_night": activities.poker,
            "chess_in_the_park": activities.chess,
            "checkers_in_the_park": activities.checker,
            "spellCast": activities.spellcast,
            "letter_league": activities.letter_league,
            "awkword": activities.awkword
        }
        if channel == None:
            embed = nextcord.Embed(title='❌ Không rõ kênh thoại!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            selectOptions = []
            for game in free_games:
                selectOptions.append(nextcord.SelectOption(label=game.replace('_',' ').title(),description='Game miễn phí'))
            for game in boosted_games:
                selectOptions.append(nextcord.SelectOption(label=game.replace('_',' ').title(),description='Game cần một nâng cấp máy chủ'))
            select = nextcord.ui.Select(placeholder='Chọn hoạt động',min_values=1,max_values=1,options=selectOptions)
            view = nextcord.ui.View(timeout=60)
            async def create_invite(interaction,game_choice):
                invite_link = await channel.create_activity_invite(game_choice)
                embed = nextcord.Embed(title='Tham gia hoạt động',url=invite_link.url,color=Colour.green())
                await interaction.response.send_message(embed=embed)
            async def callback(interaction:nextcord.Interaction):
                for game in free_games:
                    if select.values[0] == game.replace('_',' ').title():
                        await create_invite(interaction,free_games[game])
                for game in boosted_games:
                    if select.values[0] == game.replace('_',' ').title():
                        await create_invite(interaction,boosted_games[game])
            select.callback = callback
            view.add_item(select)
            await ctx.send(f'Hoạt động kênh thoại `{channel.name}`',view=view)

def setup(client):
    client.add_cog(Activity(client))
