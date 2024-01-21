# Data manipulation
import pandas as pd # data manipulation and dataframes

# Web scraping with Selenium
from selenium import webdriver # drives a browser
from webdriver_manager.chrome import ChromeDriverManager # installs and keeps the chrome driver updated
from selenium.webdriver.common.keys import Keys # simulates keyboard keys
from selenium.webdriver.chrome.options import Options # configures the chrome driver as incognito mode or maximizes the window

# Runtime management
from time import sleep # delay between code executions

# Python configuration
import warnings # ignores python warnings
warnings.filterwarnings('ignore')

# HTML parsing
from bs4 import BeautifulSoup

# Regular expressions
import re

# Datetime
from datetime import datetime
import calendar
from calendar import monthrange

# Configuration of the chrome driver
ops = Options()
ops.add_experimental_option('excludeSwitches', ['enable-automation'])

# Hides you as a robot
ops.add_experimental_option('useAutomationExtension', False)
ops.add_argument('--start-maximized') # starts maximized
ops.add_argument('user.data-dir=selenium') # saves cookies
ops.add_argument('--incognito') # incognito window

# Calendar info
months_names =  []
fir_day_mon_2023 = []
fir_day_mon_2024 = []
mon_len_2023 = []
mon_len_2024 = []

for number in range(1,13):

    months_names.append(calendar.month_name[number].lower()[0:3])
    fir_day_mon_2023.append(monthrange(2023,number)[0])
    fir_day_mon_2024.append(monthrange(2023,number)[0])
    mon_len_2023.append(monthrange(2023,number)[1])
    mon_len_2024.append(monthrange(2024,number)[1])

first_month_day_2023 = {}
first_month_day_2024 = {}
length_months_2023 = {}
length_months_2024 = {}

for number in range(0,12):
    first_month_day_2023[months_names[number]] = fir_day_mon_2023[number]
    first_month_day_2024[months_names[number]] = fir_day_mon_2024[number]
    length_months_2023[months_names[number]] = mon_len_2023[number]
    length_months_2024[months_names[number]] = mon_len_2024[number]

# Today
today = datetime.today().strftime('%Y-%m-%d')

# User defines date
input_date = input('Please enter a date (YYYY-MM-DD):')
travel_date = datetime.strptime(input_date, '%Y-%m-%d')
travel_day = travel_date.day
travel_month = travel_date.month
travel_month_name = calendar.month_name[travel_month].lower()[0:3]

days_to_sum = first_month_day_2023[travel_month_name]
travel_day_sum = travel_day + days_to_sum

# SELENIUM
# Opens driver
driver = webdriver.Chrome()

# Gets renfe url
driver.get('https://www.renfe.com/es/es')
driver.maximize_window()
sleep(1) # waits for cookies pop-up to load

# Accepts cookies
try:
    driver.find_element('css selector', '#onetrust-accept-btn-handler').click()
    sleep(1)

except:
    pass

# Fills origin
origin = driver.find_element('css selector', '#origin')
origin.click()
origin.send_keys('a coruña')
origin.send_keys(Keys.DOWN)
origin.send_keys(Keys.ENTER)
sleep(0.5)

# Fills destination
origin = driver.find_element('css selector', '#destination')
origin.click()
origin.send_keys('vigo')
origin.send_keys(Keys.DOWN)
origin.send_keys(Keys.ENTER)
sleep(0.5)

# One way ticket
driver.find_element('css selector', '#tripType > div > button').click()
sleep(0.1)
driver.find_element('css selector', '#tripType > div > div > ul > li:nth-child(1) > button').click()
sleep(0.5)

# Selects date
driver.find_element('css selector', '#datepicker > div > input').click()
sleep(0.5)
driver.find_element('xpath', f'//*[@id="datepicker"]/section/div[1]/div[2]/section[1]/div[3]/div[{travel_day_sum}]').click()
sleep(0.5)
driver.find_element('css selector', '#datepicker > section > div.lightpick__footer-buttons > button.lightpick__apply-action-sub').click()
sleep(0.5)

# Searchs tick∫ets
driver.find_element('css selector', '#contentPage > div > div > div:nth-child(1) > div > div > div > div > div > div > rf-header > rf-header-top > div > div.rf-header__wrap-search.grid.sc-rf-header-top > rf-search > div > div.rf-search__filters.rf-search__filters--open > div.rf-search__wrapper-button > div.rf-search__button > form > rf-button > div > div > button > div.mdc-button__touch.sc-rf-button').click()
sleep(5)

# Soup creation by parsing html information
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Aux lists with parsing info
val = soup.find_all('tr', {'class': 'trayectoRow'})

# Closes driver
driver.quit()

# SOUP
# Beautiful soup dictionary result
train_info = {'Departure': [], 'Arrival': [], 'Time': [], 'Type': [], 'Basic': [], 'Confort': [], 'Premium': []}

# Cleans scraped info with regex
val_clean = []

pattern = '\n(\s*)(.*?)\n'

for v in val:

    matches = re.findall(pattern, v.text)

    regex_result = []

    for sublist in matches:

        regex_result.append(sublist[1])

    val_clean.append(regex_result[0:-1])

# Adds info to dictionary
for sublist in val_clean:

    train_info['Departure'].append(sublist[0])
    train_info['Time'].append(sublist[1])
    train_info['Arrival'].append(sublist[2])
    train_info['Type'].append(sublist[4])
    train_info['Basic'].append(sublist[5].rstrip(' '))
    
    if len(sublist) > 6:

        train_info['Confort'].append(sublist[6])
        train_info['Premium'].append(sublist[7])

    else:

        train_info['Confort'].append('No disponible')
        train_info['Premium'].append('No disponible')

# Creates a df
df = pd.DataFrame(train_info)

df_available = df[df['Basic'] != 'Tren Completo']

# Prints
if df_available.empty:

    print('Sorry')

else:

    print('Métete a comprar mi neno')