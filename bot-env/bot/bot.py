import discord

client = discord.Client()

@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")

    else:
        mention = message.author.mention
        print(message.author.top_role)
        print("Activities: " + message.author.activities)
        await message.channel.send(mention + " is currently called " + message.author.display_name)

client.run('Nzk3NjA5MTc0NjQ0NDI0NzE0.X_o9bg.dX4_nkNYem45L01kdwQgm8Gqdow')