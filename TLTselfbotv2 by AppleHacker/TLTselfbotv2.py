import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot
import asyncio
import os
import datetime
import random
from random import randint
import wikipedia

from random import choice

client = commands.Bot(command_prefix = '.', self_bot = True)
client.remove_command('help')

status = ['Selfbot in 2021!']

@client.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(embed = discord.Embed(description = text, color=0xf90101))

@client.command()
async def helpfun(ctx, text):
    embed=discord.Embed(title="Funny commands", color=0x00ff00)
    embed.add_field(name="Coinflip", value="The Coinflip Game", inline=True)
    embed.set_footer(text="You watching now fun commands")
    await ctx.send(embed=embed)

@client.command()
async def coinflip(ctx):
    choices = ["Heads", "Tails"]
    rancoin = random.choice(choices)
    await ctx.send(rancoin)

@client.command(name='ping', help='This command return the latency')
async def ping(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Ping", description=f'**Pong!** Your ping is {round(client.latency * 1000)}ms')
    await ctx.send(embed=embed)

@client.command(name='Hello', help='This command returns a random welcome message!')
async def Hello(ctx):
    await ctx.message.delete()
    responses = ['***grumble*** Why dod you wake me up?', 'Top of the morning to you lad!', 'Hello!', 'Welcome', 'Hi', 'Hello, user im like your avatar!', 'hi, pro', '**hi, you nice man**', 'Welcome to my littles friend', '**:) hello**', '**Hi, Im like your account!**']
    await ctx.send(choice(responses))


@client.command(name='Die', help='Scary message or video')
async def die(ctx):
    await ctx.message.delete()
    responses = ['**Die DIE DIE!!11**', 'https://cdn.discordapp.com/attachments/803157842739724301/805413447827324968/41PNlwyX62L.jpg', 'https://www.youtube.com/watch?app=desktop&v=7aYZVrBC7ZY **Die**']
    await ctx.send(choice(responses))

@client.command(name='bye', help='...')
async def bye(ctx):
    await ctx.message.delete()
    bye = ['https://www.youtube.com/watch?v=n0tW6bZWbS8']
    await ctx.send(choice(bye))

@client.command(name='credits', help='Here are who create me')
async def credits(ctx):
    embed=discord.Embed(title="Credits", description="Made by KokaPlusOwner#3120 and Deleted User#5360", color=0xed0707)
    embed.add_field(name="Bot version", value="1.0.0", inline=True)
    await ctx.send(embed=embed)

@client.command(name='kick', pass_context = True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, context, member: discord.Member):
    await ctx.message.delete()
    await member.kick
    await context.send('User' + member.display_name + ' has been kicked.')

    if member is None:
        embed=discord.Embed(title="Kick system", color=0xf90101)
        embed.add_field(name="Error ", value="User not found!", inline=False)
        await ctx.send(embed=embed)

@client.command(name='ban', pass_context = True)
@commands.has_permissions(kick_members=True)
async def ban(ctx, context, member: discord.Member, *, reason=None):
    await ctx.message.delete()
    await member.ban(reason=reason)
    await context('User' + member.display_name + ' has been banned.')

    if member is None:
        embed=discord.Embed(title="Ban system", color=0xf90101)
        embed.add_field(name="Error ", value="User not found!", inline=False)
        await ctx.send(embed=embed)

    if reason is None:
        embed=discord.Embed(title="Ban system", color=0xf90101)
        embed.add_field(name="Error ", value="Please set reason to ban this user!", inline=False)
        await ctx.send(embed=embed)

@client.command()
async def poll(ctx, *, message):
    emb=discord.Embed(title= " POLL", description=f"{message}")
    msg=await ctx.channel.send(embed=emb)
    await msg.add_reaction('✅')
    await msg.add_reaction('❌')


@tasks.loop(seconds=20)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help", color=0x2bff00)
    embed.add_field(name="kick", value="kick user", inline=True)
    embed.add_field(name="ban", value="ban user", inline=True)
    embed.add_field(name="help", value="show this message", inline=True)
    embed.add_field(name="bye", value="...", inline=True)
    embed.add_field(name="ping", value="This command return the latency", inline=True)
    embed.add_field(name="die", value="Scary message or video", inline=True)
    embed.add_field(name="hello", value="This command returns a random welcome message!", inline=True)
    embed.set_footer(text="prefix is %")
    await ctx.send(embed=embed)

client.run("tokn", bot = False)