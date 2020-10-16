import discord

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} is ready')


@client.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="general")
    await channel.send(f"{member} has arrived!")
