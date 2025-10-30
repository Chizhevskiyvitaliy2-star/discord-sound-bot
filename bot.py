import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot is online as {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("🔊 Зайшов в голосовий канал.")
    else:
        await ctx.send("❗ Ти не в голосовому каналі!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Вийшов з голосового каналу.")
    else:
        await ctx.send("❗ Я не в голосовому каналі.")

@bot.command()
async def play(ctx):
    voice = ctx.voice_client

    if not voice:
        return await ctx.send("❗ Спочатку напиши `!join`")

    source = discord.FFmpegPCMAudio("sound.mp3")
    voice.play(source)
    await ctx.send("🎶 Відтворюю звук!")
bot.run(7986165513:AAErq4a0HZg7CoyzyX0JRFHK-lso8uJg00Y_)
