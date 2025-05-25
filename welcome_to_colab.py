from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import pandas as pd

# Set up headless Chrome browser (you can remove headless if you want to see the browser)
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

# URL for OLX car covers (change if needed)
url = "https://www.olx.in/items/q-car-cover"

driver.get(url)
time.sleep(5)  # wait for page to load

# Scroll down to load more items (optional, can repeat to load more)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

# Get page source and parse with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find all listing blocks
listings = soup.find_all('li', {'data-aut-id': 'itemBox'})

data = []
for item in listings:
    title_tag = item.find('span', {'data-aut-id': 'itemTitle'})
    price_tag = item.find('span', {'data-aut-id': 'itemPrice'})
    title = title_tag.text.strip() if title_tag else "N/A"
    price = price_tag.text.strip() if price_tag else "N/A"
    data.append({'Title': title, 'Price': price})

driver.quit()

# Convert to DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv('olx_car_covers.csv', index=False)

print(df.head(10))
