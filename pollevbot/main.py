from pollbot import PollBot
from dotenv import load_dotenv
import os
from pathlib import Path  # python3 only

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
usrName = os.getenv('USER')
passwrd = os.getenv('PASSWORD')
pollHost = os.getenv('HOST')

# print(usrName + ", " + passwrd + ", " + pollHost)


def main():
    user = usrName
    password = passwrd
    host = pollHost

    # If you're using a non-neu PollEv account,
    # add the argument "login_type='pollev'"
    login_type = 'neu'
    with PollBot(user, password, host) as bot:
        bot.run()


if __name__ == '__main__':
    main()
