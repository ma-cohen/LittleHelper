import random
import discord
from little_helper import (
    error_message,
    lh_commands,
    roles,
    exceptions,
    user_messages
)
from discord.ext import commands
from logger import logger

bot = commands.Bot(command_prefix=lh_commands.command_prefix)


@bot.event
async def on_command_error(ctx, error):
    logger.error(f'on command error {error}')
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(error_message.false_role)
    elif isinstance(error.original, exceptions.ChannelNameNotFound):
        await ctx.send(error_message.channel_not_found)


@bot.command(name=lh_commands.create_channel, help=user_messages.help_create_channel)
@commands.has_role(roles.admin)
async def create_channel(ctx, channel_name: str = None):
    if channel_name is None:
        raise exceptions.ChannelNameNotFound
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
    if not existing_channel:
        await guild.create_text_channel(channel_name)
        await ctx.send(user_messages.channel_was_created.format(channel_name))


@bot.event
async def on_ready():
    logger.info(f'{bot.user} is ready')


@bot.command(name='karo-joke',
             help='Response with a random joke on karo you can choose number of jokes. e.g !karo=joke 2')
async def karo_jokes(ctx, n: int = 1):
    karo_jokes_list = [
        'Once Karo drank beer',
        'מה זה דוחה יתושים ? לא זה דוחה אנשים',
        'מה קארו שותל בגינה ? מזלגות אלא מה',
        'זה מטוס? לא , זה ציפור? לא אז מה זה ? זה קארו בפארק שבעת החבלים',
        'למה קארו לא לוקח פיתה לטיול ? כי זה לא נפחי'
        'איך קארו בחר לטוס לויאטנם? רק לשם הוא קיבל אקסל מפורט של הוצאות'
    ]
    response = ''
    for i in range(n):
        response += f'{random.choice(karo_jokes_list)}\n'

    await ctx.send(response)


@bot.command(name='joke-by-author',
             help='Response with a random joke on karo you can choose number of jokes. e.g !karo=joke 2')
async def joke_by_author(ctx, author: str = 'matan'):
    jokes_by_author = {
        'daniel': ['איך קארו בחר לטוס לויאטנם? רק לשם הוא קיבל אקסל מפורט של הוצאות'
            , 'ריהוט לגיטימי לסלון? כלוב סקוואט',
                   'אפשר לגדל צמחים? רק כאלה אכילים'],
        'matan': [
            'Once Karo drank beer',
            'מה זה דוחה יתושים ? לא זה דוחה אנשים',
            'מה קארו שותל בגינה ? מזלגות אלא מה',
            'זה מטוס? לא , זה ציפור? לא אז מה זה ? זה קארו בפארק שבעת החבלים',
            'למה קארו לא לוקח פיתה לטיול ? כי זה לא נפחי'

        ]
    }
    if author in jokes_by_author:
        response = ''
        for jokes in jokes_by_author[author]:
            response += f'{jokes}\n'
        await ctx.send(response)


@bot.command(name='joke-of-the-day',
             help='Get the joke of the day')
async def joke_by_author(ctx):
    await ctx.send(
        'אז יושבים פה? לא יש פה מטוגן, אז יושבים פה ? לא יש פה גם אוכל מטוגן, טוב אז פה , סבבה . אחרי חמש דקות טוב יש פה רק אוכל מטוגן')
