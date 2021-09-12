from typing import Union
import discord
from discord.app import message_command, user_command, ApplicationContext
from discord.ext import commands


class ContextMenuCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @message_command(name='Echo')
    async def _echo_msg_context(self, ctx: ApplicationContext, msg: discord.Message):
        msg_author = msg.author
        await ctx.send(f'{msg_author.mention} said: {msg.content}')

    @user_command(name='Say Name')
    async def _say_name_user(self, ctx: commands.Context, user: discord.Member):
        await ctx.send(f'The user name is: {user.display_name}')


def setup(bot: commands.Bot):
    bot.add_cog(ContextMenuCog(bot))
