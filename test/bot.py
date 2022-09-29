# bot.py 
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
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)

#-------         Events         -------

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    #-------         Instant Gaming         -------
    driver.get(f'https://www.instant-gaming.com/en/search/?query={message.content}')
    element=driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div[1]')
    element.click()
    services.update({'ig' : [f"[Instant-Gaming]({driver.current_url})", driver.find_element(By.CLASS_NAME, 'total').text.replace('\n', ' ')] })
    
    #-------         Eneba         -------
    driver.get(f'https://www.eneba.com/store?page=1&platforms[]=STEAM&text={message.content}')
    element=driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/section/div[2]/div[2]/div[1]/div/div[3]/a')
    element.click()
    services.update({'eneba' : [f"[Eneba]({driver.current_url})", driver.find_element(By.XPATH, '/html/body/div[1]/main/div/div/section/div[2]/div[2]/div[1]/div/div[3]/a/div/span[2]/span').text.replace('\n', ' ')] })
    
    #-------         Final Embed         -------
    nigger=discord.Embed(title="Key Finder", description="Here is a list of keys sorted by price.", color=0x5D3FD3)
    nigger.add_field(name="Service", value='\n'.join([services[key][0] for key in services]), inline=True)
    nigger.add_field(name="Price", value='\n'.join([services[key][1] for key in services]), inline=True)
    #nigger.image(url='https://s3.gaming-cdn.com/images/products/2360/616x353/escape-from-tarkov-pc-game-cover.jpg?v=1656682867', height=400, width=229)
    await message.channel.send(embed=nigger)

client.run(TOKEN)

#quando il prezzo viene scritto la valuta viene scritta a capo, bisogna fare in modo che i siti vengano ordinati in ordine di prezzo.