# bot.py 
# https://www.scrapingbee.com/blog/selenium-python/ source 

#-------         Imports         -------
import os, discord
from discord import app_commands
from discord.ext import commands
from dotenv import load_dotenv
from collections import OrderedDict
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#-------         Functions         -------
image_link=""

def valuta(p):
    if 'EUR' in p:
        p=p.replace('EUR', '')
        p=p.replace(",", ".")
        p=f"{float(p)*10.8:07.2f}"
        p+=" kr"
    if '€' in p:
        p=p.replace('€', '')
        p=p.replace(",", ".")
        p=f"{float(p)*10.8:07.2f}"
        p+=" kr"
    if 'SEK' in p:
        p=p.replace('SEK ', '')
        p=f"{float(p):07.2f} kr"
    if 'kr.' in p:
        p=p.replace('kr.', "")
        p=f"{float(p):07.2f} kr"

    return p

def scraping(link, message, game, price, name):
    try:
        driver.get(f'{link}{message}')
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, game)))
    except:
        services.update({name : [f"```css\n[{name}]\n```", "```css\n[Unvaiable]\n```"] })
        return

    final_price=driver.find_element(By.XPATH, price).text

    if(name=="K4G"):
        final_price=str.split(str(driver.find_element(By.XPATH, price).text), "\n")[0]
    elif(name == "Steam"):
        global image_link
        image_link=f"https://cdn.cloudflare.steamstatic.com/steam/apps/{driver.find_element(By.XPATH, game).get_attribute('data-ds-appid')}/header.jpg"
        if(driver.find_element(By.XPATH, price).text==""):
            final_price=driver.find_element(By.XPATH, '//*[@id="search_resultsRows"]/a[2]/div[2]/div[4]/div[2]').text.replace('\n', ' ')
            game='//*[@id="search_resultsRows"]/a[2]'
        if("\n" in final_price):
            final_price=str.split(str(driver.find_element(By.XPATH, price).text), "\n")[1]
            
        
    services.update({name : [f"[```{name}```]({driver.find_element(By.XPATH, game).get_attribute('href')})", valuta(final_price)] })

#-------         Discord Intents         -------
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)


#-------         Variables         -------
services={
}


#-------         Env Stuff         -------
load_dotenv()

#-------         Selenium Stuff         -------
options = Options()
options.headless = False
options.add_argument("--window-size=640,480")
driver = webdriver.Chrome(options=options)

#-------         Events         -------

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.tree.command(name = "key")
@app_commands.describe(name = "Name of the videogame? Please be specific")
async def key(interaction: discord.Interaction, name: str):
    #-------         Placeholder         -------
    await interaction.response.send_message(f"I am now searching for `{name}` keys!", ephemeral=True)
       
    #-------         Steam         -------
    scraping('https://store.steampowered.com/search/?term=', name, '//*[@id="search_resultsRows"]/a[1]', '//*[@id="search_resultsRows"]/a[1]/div[2]/div[4]/div[2]', 'Steam')
       
    #-------         Humble Bundle         -------
    scraping('https://www.humblebundle.com/store/search?sort=bestselling&search=', name, '//*[@id="mm-0"]/div[1]/div[6]/div[2]/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/ul/li[1]/div/div/a', '//*[@id="mm-0"]/div[1]/div[6]/div[2]/section/div[2]/div[2]/div/div/div[2]/div/div[2]/div[1]/div/ul/li[1]/div/div/div/div[2]/div/div[2]/span[1]', 'Humble Bundle')
    
    #-------         Instant Gaming         -------
    scraping('https://www.instant-gaming.com/en/search/?query=', name, '/html/body/div[5]/div/div/div[1]/a', '/html/body/div[5]/div/div/div[1]/div/div[2]', 'Instant-Gaming')
    
    #-------         K4G         -------
    scraping('https://k4g.com/store?q=', name, '//*[@id="k4g-root"]/div/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[1]/a', '//*[@id="k4g-root"]/div/div[3]/div/div[3]/div[2]/div[1]/div[2]/div[1]/div[2]/div[1]/div[2]', 'K4G')
    
    #-------         Eneba         -------
    scraping('https://www.eneba.com/store?text=', name, '//*[@id="app"]/main/div/div/section/div[2]/div[2]/div[1]/div/div[3]/a', '//*[@id="app"]/main/div/div/section/div[2]/div[2]/div[1]/div/div[3]/a/div/span[2]/span', 'Eneba')
    
    #-------         Final Embed         -------
    FinalEmbed=discord.Embed(title="Key Finder", description="Here is a list of keys sorted by price.", color=0x5D3FD3)
    global services
    services=OrderedDict(sorted(services.items(), key=lambda x: x[1][1]))
    FinalEmbed.add_field(name="Service", value='\n'.join([services[key][0] for key in services]), inline=True)
    FinalEmbed.add_field(name="Price", value='\n'.join([f"```{services[key][1].lstrip('0')}```" for key in services]), inline=True)
    FinalEmbed.set_image(url=image_link)
    
    await interaction.edit_original_response(content=f"Hey {interaction.user.name}, these are the keys i found for `{name}`.", embed=FinalEmbed)

    #-------         Commands Sync         -------
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command/s")
    except Exception as e:
        print(e)

bot.run(os.getenv('DISCORD_TOKEN'))


#quando il prezzo viene scritto la valuta viene scritta a capo, bisogna fare in modo che i siti vengano ordinati in ordine di prezzo.
