from telethon import TelegramClient
from telethon.sync import TelegramClient
from telethon import functions
from datetime import datetime
import time


def bot():
    while 2 > 1:
        api_id = 123456789
        api_hash = 'qazwsxedcrfvtgbyhnujmikolp123456789'
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        with TelegramClient("name", api_id, api_hash) as client:
            result = client(functions.account.UpdateProfileRequest(
                first_name=f'{current_time}'
            ))
            time.sleep(15)
            print(now.strftime("%H:%M:%S"))


if __name__ == "__main__":
    bot()
