import requests

from bs4 import BeautifulSoup
from email_alert import alert_system
from threading import Timer

URL = "https://www.amazon.in/Samsung-Galaxy-Ear-Buds-Black/dp/B08SKDXKZF/ref=sr_1_10?crid=1EC1N6VE3W2XL&keywords=samsung+earphones&qid=1658928745&sprefix=samsung+earphone%2Caps%2C253&sr=8-10"
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
'Accept-Language' : 'en-US,en;q=0.5',
'Accept-Encoding' : 'gzip',
'DNT' : '1', # Do Not Track Request Header
'Connection' : 'close'
}

set_price = 6000

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    product_title = str(title)
    product_title = product_title.strip()
    print(product_title)
  
    price=soup.find('span', attrs={'class':'a-price-whole'}).get_text()
    print(price)
    product_price = ''
    for letters in price:
        if letters.isnumeric() or letters == '.':
            product_price += letters
    print(float(product_price))
    if float(product_price) <= set_price:
        alert_system(product_title, URL)
        print('sent')
        return
    else:
        print('not sent')
    Timer(60, check_price).start()

check_price()