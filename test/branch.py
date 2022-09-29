# https://www.scrapingbee.com/blog/selenium-python/ source niggerslayer420-

#-------         Imports         -------
import os, discord
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#-------         Variables         -------
services={
    "ig" : [None, None],
    "eneba" : ["hihiha", "yoyo"],
    "kinguin" : ["hihiho", "yoyoya"]
}

#-------         Discord Intents         -------
intents = discord.Intents.default()
intents.members=True
intents.messages=True
client = discord.Client(intents=intents)

#-------         Env Stuff         -------
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#-------         Selenium Stuff         -------
DRIVER_PATH='chromedriver.exe'
options = Options()
options.headless = False
options.add_argument("--window-size=1280,720")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#-------         Events         -------

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    


client.run(TOKEN)

#quando il prezzo viene scritto la valuta viene scritta a capo, bisogna fare in modo che i siti vengano ordinati in ordine di prezzo.