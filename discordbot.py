import discord
from discord.ext import commands
import asyncio
import os
import subprocess
from voice_generator import creat_WAV

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
voice_client = None

#if not discord.opus.is_loaded():
#    discord.opus.load_opus("heroku-buildpack-libopus")

@bot.event
async def on_ready():
    print('Logged in as')
    print('------')


@bot.command(aliases=["connect","summon"]) #connectやsummonでも呼び出せる
async def join(ctx):
    voice_state = ctx.author.voice
    #ルームに入っていない場合
    #if (not voice_state) or (not voice_state.channel):
    #await ctx.send("先にボイスチャンネルに入っている必要があります。")
    #return
    #voicechannelを取得
    print('#voicechannelを取得')
    vc = ctx.author.voice.channel
    #voicechannelに接続
    print('#voicechannelに接続')
    await vc.connect()

@bot.command()
async def bye(ctx):
    #切断
    print('#voicechannelから切断')
    await ctx.voice_client.disconnect()

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.event
async def on_message(message):
    msgclient = message.guild.voice_client
    if message.content.startswith('.'):
        pass

    else:
        if message.guild.voice_client:
            print(message.content)
            
            emotion = 'normal'
            filepath='/tmp/voice_message'
            creat_WAV(message.content,filepath,emotion)
            source = discord.FFmpegPCMAudio(creat_WAV(message.content,filepath,emotion))
            message.guild.voice_client.play(source)
        else:
            pass
    await bot.process_commands(message)

bot.run(token)
