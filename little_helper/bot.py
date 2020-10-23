import random
import discord
from little_helper import (
    error_message,
    lh_commands,
    roles,
    exceptions,
    user_messages
)
from fire_base_handler import fire_base_handler
from discord.ext import commands
from jokes import Joke, jokes
import logging

logging.basicConfig(level=logging.INFO)

# TODO - fix logging

bot = commands.Bot(command_prefix=lh_commands.COMMAND_PREFIX)


@bot.event
async def on_command_error(ctx, error):
    logging.error(f'on command error {error}')
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send(error_message.FALSE_ROLE)
    elif isinstance(error.original, exceptions.ChannelNameNotFound):
        await ctx.send(error_message.CHANNEL_NOT_FOUND)


@bot.command(name=lh_commands.CREATE_CHANNEL, help=user_messages.HELP_CREATE_CHANNEL)
@commands.has_role(roles.admin)
async def create_channel(ctx, channel_name: str = None):
    if channel_name is None:
        raise exceptions.ChannelNameNotFound
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.text_channels, name=channel_name)
    if not existing_channel:
        await guild.create_text_channel(channel_name)
        await ctx.send(user_messages.CHANNEL_WAS_CREATED.format(channel_name))


#TODO add some tests to see if all edge cases are covered

@bot.group()
async def joke(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(error_message.INVALID_JOKE_COMMAND)


@joke.command(help=user_messages.HELP_JOKE_ADD)
async def add(ctx, joke_to_add: str, category: str = 'General'):
    author = ctx.message.author.name
    new_joke = Joke(author, joke_to_add, category)
    jokes.append(new_joke)
    await ctx.send(user_messages.JOKE_WAS_ADDED.format(new_joke))


@joke.command(help=user_messages.HELP_JOKES_CHANGES)
async def changes(ctx):
    await ctx.send(user_messages.JOKES_CHANGES.format(jokes))


@joke.command()
async def save(ctx):
    logging.info("save")


@bot.event
async def on_ready():
    print('ready')
    logging.info(f'{bot.user} is ready')


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


# @bot.command(name='joke',
#              help='test')
# async def karo_jokes(ctx):
#     docs = fire_base_handler.get_all_docs('jokes')
#     res = ''
#     for doc in docs:
#         res += doc.to_dict().get('joke')
#
#     await ctx.send(res)


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
