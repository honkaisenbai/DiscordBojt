import nextcord
from nextcord.ext import commands
from nextcord import Colour
import sympy
import numpy


class Math(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def math(self,ctx,*,arg=None):
        if arg == None:
            embed = nextcord.Embed(title='❌ Không rõ phép tính!',color=Colour.red())
            await ctx.reply(embed=embed,delete_after=3)
        else:
            try:
                answer = sympy.N(arg)
                ans = numpy.format_float_positional(answer,trim='-')
                embed = nextcord.Embed(title=f'{arg} = {ans}',color=Colour.green())
            except:
                embed = nextcord.Embed(title='❌ Không rõ phép tính!',color=Colour.red())
                await ctx.reply(embed=embed,delete_after=3)
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Math(client))
