from discord.ext import commands

bot = commands.Bot(command_prefix='n!')

# Load directly for demo
bot.load_extension('cogs.simple')

with open('token.txt', 'r') as fp:
    TOKEN = fp.read().rstrip()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.run(TOKEN)
