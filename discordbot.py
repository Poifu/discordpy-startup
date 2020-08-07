import discord
from discord.ext import commands
import subprocess
from voice_generator import creat_WAV
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
voice_client = None


@bot.event
async def on_ready():
    print('Logged in as')
    print('------')


@bot.command(aliases=["call","summon"])
async def join(ctx):
    voice_state = ctx.author.voice
    if (not voice_state) or (not voice_state.channel):
    await ctx.send("先にボイスチャンネルに入っている必要があります。")
    return
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
