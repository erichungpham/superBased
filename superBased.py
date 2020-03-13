import discord
import time
import asyncio

messages = joined = 0

def read_token():
        with open("token.txt", "r") as f:
            lines = f.readlines()
            return lines[0].strip()

token = read_token()

client = discord.Client()

async def update_stats():
        await client.wait_until_ready()
        global messages, joined

        while not client.is_closed():
            try:
                with open("stats.txt", "a") as f:
                    f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

                messages = 0
                joined = 0

                await asyncio.sleep(5)
            except Exception as e:
                print(e)
                await asyncio.sleep(5)


@client.event
async def on_message(message):
    global messages # ADD TO TOP OF THIS FUNCTION
    messages += 1 # ADD TO TOP OF THIS FUNCTION

    id = client.get_guild(324053448096088064)
    channels = ["ironic-sanic-posts"]
    #valid_users = [""] #only users in this list can

    if str(message.channel) in channels: #and str(message.author) in valid_users: #checks if in correct channel
        if message.content.find("<hello") != -1:
            await message.channel.send("Hi")
        if message.content.find("<paramore") != -1:
            await message.channel.send("https://open.spotify.com/playlist/70yS9AYFzjM7JJrbtw2v2K?si=GBz7DQGCTEi6XVlW_hpNpg -a")
        elif message.content == "<users":
            await message.channel.send(f"""# of Members: {id.member_count}""")


@client.event
async def on_member_join(member):
    global joined # ADD TO TOP OF THIS FUNCTION
    joined += 1 # ADD TO TOP OF THIS FUNCTION
    for channel in member.guild.channels:
        if str(channel) == "general": #making sure we are sending the message in "x" channel
            await channel.send_message(f"""Welcome to our channel bruvs. {member.mention}""")

#server id = 324053448096088064
client.loop.create_task(update_stats())
client.run(token)