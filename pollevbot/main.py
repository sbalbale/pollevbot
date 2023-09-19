from pollbot import PollBot
from dotenv import load_dotenv
load_dotenv()
import os




def main():
    usrName = os.getenv('USER')
    passwrd = os.getenv('PASSWORD')
    pollHost = os.getenv('HOST')
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
