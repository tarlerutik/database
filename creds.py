import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class cred():
    BOT_TOKEN = os.getenv("7379603551:AAGs6_lVJhn7aIdyEHUWv_Ycczn5T5D6pU4") #From botfather
    API_ID = os.getenv("28295266") #"Get this value from my.telegram.org! Please do not steal"
    API_HASH = os.getenv("3818a2a8eef52ac465eb375f2b6688dd") #"Get this value from my.telegram.org! Please do not steal"