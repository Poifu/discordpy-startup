import discord
from discord.ext import commands
import subprocess
from voice_generator import creat_WAV
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


client = commands.Bot(command_prefix='.')
voice_client = None


@bot.event
async def on_ready():
    print('Logged in as')
    print('------')


@bot.command()
async def join(ctx):
    #voicechannelを取得
    vc = ctx.author.voice.channel
    #voicechannelに接続
    await vc.connect()

@bot.command()
async def bye(ctx):
    #切断
    await ctx.voice_client.disconnect()

@bot.event
async def on_message(message):
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            print(message.content)
            creat_WAV(message.content)
            source = discord.FFmpegPCMAudio("output.wav")
            message.guild.voice_client.play(source)
        else:
            pass

bot.run(token)
