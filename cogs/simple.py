from discord.app import slash_command, option, ApplicationContext
from discord.ext import commands


class SimpleCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(name='echo', description='Simple slash command')
    @option('text', str, description='Text to echo')
    async def _echo_slash(self, ctx: ApplicationContext, text: str):
        await ctx.send(text)
    
    @commands.command(name='echo')
    async def _echo_cmd(self, ctx: commands.Context, *, text: str):
        await ctx.send(text)


def setup(bot: commands.Bot):
    bot.add_cog(SimpleCog(bot))
