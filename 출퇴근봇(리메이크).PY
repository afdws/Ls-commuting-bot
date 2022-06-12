from time import sleep
import discord
import datetime
import requests, random, time
from discord.ext import commands
import os
from os import system

title = '출퇴근봇 실행중...ㅣCommuting bot running...'
system(f'title {title}')

client = discord.Client()
bot = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('===============================================')
    print(client.user.name)
    time.sleep(0.5)
    print(client.user.id)
    print('출퇴근봇이 정상적으로 실행되었습니다!')
    time.sleep(0.5)
    print('===============================================')
    time.sleep(0.5)
    game = discord.Game("출퇴근 대기")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author.bot:
        return None
    id = message.author.id
    if message.content.startswith("!출근"):
        embed = discord.Embed(title="관리자 출근 알림", description="<@{0}>님이 출근상태이십니다!".format(id), color=0x0027ff, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="\n", value="관리자가 출근하였습니다 문의 처리 시작합니다\n", inline=True)
        embed.set_footer(text="출근 시간")
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        await message.delete()
        role = discord.utils.get(message.guild.roles, name="🔫 = = 출근 수방사 인원 = = 🔫")
        await message.author.add_roles(role)
        role2 = discord.utils.get(message.guild.roles, name="인간")
        await message.author.remove_roles(role2)

    if message.content.startswith("!퇴근"):
        embed = discord.Embed(title="관리자 퇴근 알림", description="<@{0}>님이 퇴근상태이십니다!".format(id), color=0xff0000, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="\n", value="관리자가 퇴근하였습니다 문의 처리 못합니다\n", inline=True)
        embed.set_footer(text="퇴근 시간")
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        await message.delete()
        role = discord.utils.get(message.guild.roles, name="인간")
        await message.author.add_roles(role)
        role2 = discord.utils.get(message.guild.roles, name="🔫 = = 출근 수방사 인원 = = 🔫")
        await message.author.remove_roles(role2)
        
    if message.content.startswith("!자리비움"):
        embed = discord.Embed(title="관리자 자리비움 알림", description="<@{0}>님이 자리비움이십니다!".format(id), color=0xfdff00, timestamp=datetime.datetime.utcnow())
        embed.add_field(name="\n", value="관리자가 자리를 비웠습니다 문의 처리 늦게 시작합니다\n", inline=True)
        embed.set_footer(text="자리비움 시간")
        embed.set_author(name=message.author, icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)
        await message.delete()
        role = discord.utils.get(message.guild.roles, name="🔫 = = 출근 수방사 인원 = = 🔫")
        await message.author.add_roles(role)
        role2 = discord.utils.get(message.guild.roles, name="인간")
        await message.author.remove_roles(role2)


client.run("")