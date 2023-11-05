
TOKEN = 'YOUR_TOKEN_GOES_HERE'
import discord
from random import randint as god
from random import choice as god_choice
from discord.ext import commands
from jokeapi import Jokes
import aiohttp
import os
from PIL import Image, ImageDraw
import wave
from webserver import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="t!", intents=intents, help_command=None)

print(os.getcwd())
def make_list(file: str, seperator: str, encoding: str = "utf8"):
    with open(file, 'r', encoding=encoding) as f:
        list_of_words = f.read().split(seperator)
        f.close()
        print(f"read file: {file} with len: {len(list_of_words)}")
    return list_of_words

@client.event
async def on_ready():
  print ("Połączono z Bogiem.")
  await client.change_presence(status=discord.Status.idle, activity=discord.Game('Yeah, I killed a CIA nigger with my car in 1999. Score one for the good guys.'))

@client.command()
async def num(ctx, number=10):
    await ctx.send(god(1, number))

@client.command()
async def feel(ctx):
    await ctx.send(god_choice(make_list("Data/Smileys.TXT", "\n")))

@client.command(aliases=['God', 'gw'])
async def words(ctx, number=10):
    gods_word = ""
    if number >= 101:
        await ctx.send("kys CIA nigger")
        return
    wordlist = make_list("Data/Vocab.TXT", "\n")
    for x in range(number):
        gods_word += god_choice(wordlist).replace("\n", "") + " "
    await ctx.send(gods_word)

@client.command()
async def happy(ctx, number=10):
    gods_word = ""
    if number >= 101:
        await ctx.send("kys CIA nigger")
        return
    wordlist = make_list("Data/Happy.TXT", "\n") 
    for x in range(number):
        gods_word += f"{god_choice(wordlist).strip()} "
    await ctx.send(gods_word)

@client.command()
async def recipe(ctx, number=10):
    recipe = ""
    if number >= 101:
        await ctx.send("kys CIA nigger")
        return
    wordlist = make_list("Data/Ingredients.TXT", "\n", "cp1252") 
    for x in range(number):
        recipe += f"{god_choice(wordlist).strip()}, "
    await ctx.send(recipe)

@client.command(aliases=["oracle"])
async def bible(ctx, text=None):
    if text is not None:
        for verse in make_list("kjv.txt", "\n"):
            if text in verse:
                await ctx.send(verse)
                return
    else:
        await ctx.send(god_choice(make_list("kjv.txt", "\n")))
        return
    await ctx.send("There shall be no word of god with this text!")
          
@client.command(aliases=["tquote"])
async def tadquote(ctx):
    await ctx.send(god_choice(make_list("Data/CleanTweets.TXT", "\n")))

@client.command()
async def joke(ctx):
  j = await Jokes()
  joke = await j.get_joke(response_format="txt")
  await ctx.send(joke)

@client.command()
async def quote(ctx):
    with open(f"Fortunes/{god(1,443)}", "r", encoding='utf8') as f:
        await ctx.send(f.read())
        f.close()

@client.command()
async def godmusic(ctx):
    song = []
    for x in range(god(40,90)):
        print(f"added nr. {x}")
        w = wave.open(f"notes/key{god(1,16)}.wav")
        song.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()
    output = wave.open("god-song.wav", "wb")
    output.setparams(song[0][0])
    for i in range(len(song)):
        output.writeframes(song[i][1])
    output.close()
    await ctx.send(file=discord.File(r"god-song.wav"))
    
@client.command(pass_context=True)
async def elephant(ctx):
    embed = discord.Embed(title="", description='"I like elephants and God likes elephants, and yeah, a realistic elephant."')

    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/elephants/new.json?sort=new') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [god(0, 25)]['data']['url'])
            await ctx.send(embed=embed)

@client.command()
async def help(ctx):
    await ctx.send(file=discord.File(r"terry.mp4"))

@client.command(aliases=["drawing", "god_drawing"])
async def goddrawing(ctx):
    img = Image.new("RGB",(640,480),'white')
    dr = ImageDraw.Draw(img)
    for x in range(god(180, 360)):
        x0 = god(1,640)
        y0 = god(1, 480)
        start = god(1, 180)
        if god(1,100) <= 90:
            dr.arc((x0, y0, god(x0,640), god(y0,480)), start, god(start,360), fill=(god(1,255), god(1,255), god(1,255)), width=god(1,3))
        elif god(1,100) <= 51:
            dr.rectangle((x0, y0, god(x0,640), god(y0,480)), fill=(god(1,255), god(1,255), god(1,255)), width=1)
        else:
            dr.ellipse((x0, y0, god(x0,640), god(y0,480)), fill=(god(1,255), god(1,255), god(1,255)), width=1)
        print(x)
    img.save("god-drawing.png", bitmap_format='png')
    await ctx.send(file=discord.File(r"god-drawing.png"))

keep_alive()
client.run(TOKEN)