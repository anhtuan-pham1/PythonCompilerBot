import os
import discord
from discord.ext import commands
import setting
import argparse
from compiler import jdoodle_compiler

# initialize toke and client url
TOKEN = os.getenv("TOKEN")
CLIENT_URL = os.getenv("CLIENT_URL")
# initialize channel ID
WELCOME_CHANNEL_ID = int(os.getenv("WELCOME_CHANNEL_ID"))
LEAVE_CHANNEL_ID = int(os.getenv("LEAVE_CHANNEL_ID"))

client = commands.Bot(command_prefix="#",
                      intents=discord.Intents.all())

client1 = discord.Client()

# Login bot account
@client.event
async def on_ready():
    print("Logged in as "+client.user.name)

@client.event
async def on_member_join(member):
    await client.wait_until_ready()
    try:
        channel = client.get_channel(WELCOME_CHANNEL_ID)
        try:
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(
                name="Welcome", value="Chào mừng bé " + member.mention + "đến với " + member.guild.name + "\nCảm ơn bé đã vào động gay của duck!", inline=False)
            embed.set_thumbnail(url=member.guild.icon_url)
            await channel.send(embed=embed)
        except Exception as e:
            print(e)
            raise e
    except Exception as e:
        print(e)
        raise e
        
@client.event
async def on_member_remove(member):
    await client.wait_until_ready()
    try:
        channel = client.get_channel(LEAVE_CHANNEL_ID)
        try:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=member.name, icon_url=member.avatar_url)
            embed.add_field(
                name="Good Bye", value="Nhà đang yên ổn " + member.mention + " đừng về ", inline=False)
            embed.set_thumbnail(url=member.guild.icon_url)
            await channel.send(embed=embed)
        except Exception as e:
            print(e)
            raise e
    except Exception as e:
        print(e)
        raise e


@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    msg = message.content
    if msg.lower().startswith("!python"):
        args = msg.split("```")
        print(len(args))
        if len(args) != 3:
            await message.channel.send("Invalid Command! Please try again as !testing argument")
        else:
            resp, response = jdoodle_compiler(args[1])   
            result = response['output']
            mem = response['memory']
            time = response['cpuTime']
            
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.add_field(name="Result", value="stdout:  " + result + '\n' + "memory: " + mem + '\n' + "time "+ time, inline=False)
            await message.channel.send(embed=embed)
client.run(TOKEN)
