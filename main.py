import conf

from little_helper import bot
from logger import initialize_logger


def main():
    initialize_logger()
    bot.run(conf.token)


if __name__ == '__main__':
    main()
