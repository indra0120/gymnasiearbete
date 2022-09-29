# bot.py 
# https://www.scrapingbee.com/blog/selenium-python/ source niggerslayer420-

#-------         Imports         -------
import os, discord
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#-------         Functions         -------
def scraping(link, message, game, price, name):
    driver.get(f'{link}{message.content}')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, game))).click()
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, price)))
    services.update({name : [f"[{name}]({driver.current_url})", driver.find_element(By.XPATH, price).text.replace('\n', ' ')] })


#-------         Variables         -------
services={
    "Instant-Gaming" : [None, None],
    "K4G" : [None, None],
    "Kinguin" : [None, None]
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
    
    #-------         Instant Gaming         -------
    scraping('https://www.instant-gaming.com/en/search/?query=', message, '/html/body/div[5]/div/div/div[1]/a', '/html/body/div[4]/div/div[3]/div[2]/div[2]/div[4]/div[3]', 'Instant-Gaming')
    
    #-------         K4G         -------
    scraping('https://k4g.com/store?q=', message, '/html/body/div[1]/div/div/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[1]/a', '/html/body/div[1]/div/div/div[3]/div[1]/div[5]/div/div[2]/div/div[1]/span[3]', 'K4G')
    
    #-------         Kinguin         -------
    scraping('https://www.kinguin.net/listing?phrase=', message, '//*[@id="c-page__content"]/div/div/div/div/div[2]/div/div[2]/div[2]/div/a[1]', '//*[@id="offers-list-container"]/div/div[1]/div[1]/div/div[2]/div[2]/span[2]', 'Kinguin')
    
    #-------         Final Embed         -------
    nigger=discord.Embed(title="Key Finder", description="Here is a list of keys sorted by price.", color=0x5D3FD3)
    nigger.add_field(name="Service", value='\n'.join([services[key][0] for key in services]), inline=True)
    nigger.add_field(name="Price", value='\n'.join([services[key][1] for key in services]), inline=True)
    #nigger.image(url='https://s3.gaming-cdn.com/images/products/2360/616x353/escape-from-tarkov-pc-game-cover.jpg?v=1656682867', height=400, width=229)
    await message.channel.send(embed=nigger)

client.run(TOKEN)


#quando il prezzo viene scritto la valuta viene scritta a capo, bisogna fare in modo che i siti vengano ordinati in ordine di prezzo.
