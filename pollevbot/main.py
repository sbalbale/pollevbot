from pollbot import PollBot


def main():
    user = 'balbale.s'
    password = '41HillcrestRoad!'
    host = 'vasilikilyko643'

    # If you're using a non-neu PollEv account,
    # add the argument "login_type='pollev'"
    login_type = 'neu'
    with PollBot(user, password, host) as bot:
        bot.run()


if __name__ == '__main__':
    main()
