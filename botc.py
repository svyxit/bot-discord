import discord
import os
from discord.ext import commands
from discord.ext.commands import Bot
from discord.utils import get
from discord import FFmpegPCMAudio
from discord import TextChannel
from youtube_dl import YoutubeDL
intents = discord.Intents.all()

bot = Bot(command_prefix="!", intents=intents) #or your prefix

@bot.event
async def on_ready():
    print("Bot conectado")

    await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("Criador; syolin#0001"))



@bot.command(aliases=['clean', 'limpar'])
@commands.has_permissions(manage_messages = True)
async def clear( ctx, limit = 100 ): # or any limit you like
    await ctx.channel.purge( limit = limit )
    embed = discord.Embed(title = f'Mensagens deletadas.', description = f'Obrigado {ctx.author} por limpar o canal!')
    await ctx.send(embed = embed)    

# command to clear channel messages



bot.run("TOKEN DO SEU BOT")