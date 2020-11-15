import random
import discord
from little_helper import (
    error_message,
    lh_commands,
    roles,
    exceptions,
    user_messages
)
from fire_base_handler import fire_base_handler, collections
from discord.ext import commands
from jokes import Joke, jokes
import logging

logging.basicConfig(level=logging.INFO)
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


@bot.group()
async def joke(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send(error_message.INVALID_JOKE_COMMAND)


@joke.command(help=user_messages.HELP_JOKE_RANDOM)
async def please(ctx):
    db_jokes = fire_base_handler.get_all_docs(collections.JOKES)
    random_joke_doc = random.choice(db_jokes)
    random_joke = Joke.from_dict(random_joke_doc)
    await ctx.send(user_messages.RANDOM_JOKE.format(random_joke))


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
    if new_jokes := jokes.new_jokes:
        fire_base_handler.add_docs(collections.JOKES, new_jokes)
        await ctx.send(user_messages.JOKES_WERE_SAVED)
    else:
        await ctx.send(user_messages.NO_JOKE)


@bot.event
async def on_ready():
    logging.info(f'{bot.user} is ready')


