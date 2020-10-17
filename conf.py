import os
from dotenv import load_dotenv, find_dotenv

DISCORD_TOKEN = 'DISCORD_TOKEN'

if find_dotenv():
    load_dotenv()

token = os.getenv(DISCORD_TOKEN)
if token is None:
    raise ValueError(f'No {DISCORD_TOKEN} environment variable found')
