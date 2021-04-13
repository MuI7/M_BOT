import discord
import asyncio
import random
import os

client = discord.Client()

access_token = os.environ["BOT_TOKEN"]
token = access_token

@client.event
async def on_ready():

    print(client.User.name)
    print('무냥봇 로그인했다냥!')
    game = discord.Game('안하는중')
    await client.change_presence(status=discord/status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "무냥봇":
        await message.channel.send("왜부르냥!")

    if message.content == "무냥봇 바보":
        await message.channel.send("나 바보 아니다냥!!!:pouting_cat:")

    if message.content == "무냥봇 돈줘":
        await message.channel.send("싫다냥~:smirk_cat:")

    if message.content == "무냥봇 안녕":
        await message.channel.send("안녕하다냥~")

    if message.content == "무냥봇 정체":
        embed = discord.Embed(title="무냥봇", description="THE AI", color=0x3a99ff)
        embed.add_field(name="생일", value="2021.4.13일약 7시",inline=False)
        embed.add_field(name="이름", value="무냥봇",inline=False)
        embed.set_footer(text="제작자 무이")
        await message.channel.send(embed=embed)

    if message.content == "무냥봇 아침":
        ran = random.randint(0,14)
        if ran == 0:
            breakfast = "토스트 어떠냥....?"
        if ran == 1:
            breakfast = "밥과 국은 어떠냥?"
        if ran == 2:
            breakfast = "음.. 씨리얼! 우유에 씨리얼 어떠나냥?"
        if ran == 3:
            breakfast = "기다리라냥!(냠냠쩝쩝)"
        if ran == 4:
            breakfast = "계란 볶음밥도 좋을것 같다냥"
        if ran == 5:
            breakfast = "라면 먹어라냥(후르르릅 짭짭)"
        if ran == 6:
            breakfast = "김이랑 밥이랑 촵 사먹어라냥!"
        if ran == 7:
            breakfast = "달걀 후라이와 밥 먹어라냥~"
        if ran == 8:
            breakfast = "마트에서 사료 사먹어라냥!"
        if ran == 9:
            breakfast = "참치 먹어라냥"
        if ran == 10:
            breakfast = "굶는건 어떠냥"
        if ran == 11:
            breakfast = "시원한 우유 한잔 어떠냥?"
        if ran == 12:
            breakfast = "흰 쌀밥과 김치랑 먹어라냥..!"
        if ran == 13:
            breakfast = "김치볶음밥 먹어라냥.."
        if ran == 14:
            breakfast = "대충 치킨 시켜라냥!"
        await message.channel.send(breakfast)



    if message.content == "무냥봇":
        await message.channel.send("안녕하다냥~")



        

client.run(token)


