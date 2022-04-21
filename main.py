import requests
import json
import colorama
import random
from colorama import Fore
from time import time, sleep


class Bot:
    def __init__(self, name, token, channel, message):
        self.message = message
        self.token = token
        self.channel_id = channel
        self.headers = {'Authorization': token}
        self.name = name

    def run(self):
        try:
            proxy_file = open('proxy.json')
            proxy = json.load(proxy_file)
            proxies = {"https": proxy[random.randint(0, len(proxy)-1)]}

            req = requests.post(
                f'https://discordapp.com/api/v9/channels/{self.channel_id}/messages', headers=self.headers, json={'content': self.message}, proxies=proxies)
            if(req.status_code == 200):
                print(f"[{self.name}]{Fore.GREEN} OK - Message Sent{Fore.WHITE}")
            else:
                print(
                    f"[{self.name}] {Fore.RED} FAILED ENDPOINT CALL - Message not sent{Fore.WHITE}")
        except Exception as e:
            print(
                f"[{self.name}] {Fore.RED} FAILED EXECUTION - Message not sent: {e}{Fore.WHITE}")


def main():
    timeout = 5  # Seconds
    bot_list = []

    accounts_file = open('accounts.json')

    accounts = json.load(accounts_file)

    print("Loading Bots...")
    for i in range(len(accounts)):
        bot_token = accounts[i]['token']
        bot_message = accounts[i]['message']
        bot_name = accounts[i]['name']
        bot = Bot(bot_name, bot_token, "724627878699860029", bot_message)
        bot_list.append(bot)

    print("Starting the spam...")

    while True:
        bot_idx = random.randint(0, len(bot_list)-1)
        bot = bot_list[bot_idx]
        bot.run()
        sleep(timeout - time() % timeout)


if __name__ == '__main__':
    main()
