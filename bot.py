# import discord

# from pass_gen import gen_pass

# Variabel intents menyimpan hak istimewa bot
# intents = discord.Intents.default()
# Mengaktifkan hak istimewa message-reading
# intents.message_content = True
# Membuat bot di variabel klien dan mentransfernya hak istimewa
# client = discord.Client(intents=intents)
# @client.event
# async def on_ready():
#     print(f'Kita telah masuk sebagai {client.user}')
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if message.content.startswith('$halo'):
#         await message.channel.send("Hi!")
#     elif message.content.startswith('$bye'):
#         await message.channel.send("\\U0001f642")
#     elif message.content.startswith('$genpass'):
#         await message.channel.send(gen_pass(10))    
#     else:
#         await message.channel.send(message.content)

# client.run("")

import discord
from discord.ext import commands
import random
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def guess(ctx):
    await ctx.send('Guess a number between 1 and 10.')

@bot.command()
async def mem(ctx):
    imagess = os.listdir('images')
    with open('images/'+random.choice(imagess), 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
    # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    words = [
        "Your Daily Meme is Here",
        "Get up and be ready lads",
        "Let's do it",
        "Keep it up!",
        "Don't forget your 3R",
    ]
    await ctx.send(random.choice(words), file=picture)


@bot.command()
async def answer(ctx,n):
    if n == random.randint(1,10):
        await ctx.send('Good Job!')
    else:
        await ctx.send('Try Again!')

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Setelah kita memanggil perintah bebek (duck), program akan memanggil fungsi get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

bot.run("")
 
