from discord.ext import commands

bot = commands.Bot(command_prefix='n!')

# Load directly for demo
bot.load_extension('cogs.simple')
bot.load_extension('cogs.context_menu')

with open('token.txt', 'r') as fp:
    TOKEN = fp.read().rstrip()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    total_app = len(list(bot.application_commands.keys()))
    print(f'Registered {total_app} app commands')

bot.run(TOKEN)
