from bot import client
import conf


def main():
    client.run(conf.token)


if __name__ == '__main__':
    main()
