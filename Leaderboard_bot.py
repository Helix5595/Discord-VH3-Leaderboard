import subprocess
import discord
from discord.ext import commands

# set up the bot
bot = commands.Bot(command_prefix = '!', intents = discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.command()
async def update(ctx):
    # run the script using a subprocess
    script_process = subprocess.Popen(['python3', 'leaderboard_script_2.0.py'])
    script_output, _ = script_process.communicate()

    # read contents of the file
    with open('leaderboard_results.txt', 'r') as file:
        result_content = file.read()

    # post the contents in the discord channel where the command was called from
    await ctx.send(result_content)

bot.run('DISCORD_BOT_KEY_HERE')