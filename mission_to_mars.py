import time
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd
import requests
#executable path
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
# HTML object
url = 'https://mars.nasa.gov/news/?'
browser.visit(url)
html = browser.html
time.sleep( 5 )
# Parse HTML with Beautiful Soup

soup = BeautifulSoup(html, 'html.parser')
# Parse HTML with Beautiful Soup

#get and print the latest news title and teaser paragraph
latest_news_title = soup.find(class_='list_text').find('a').text
print(latest_news_title)
latest_teaser = soup.find('div', class_='list_text').find('div', class_='article_teaser_body').text
print(latest_teaser)





'''
results = []
filtered = []
for x in  soup.find_all( class_='list_text'):
    results.append(x.text)
for y in results:
    print(y)

'''
'''
results = soup.find_all('div', class_="slide")
for result in results:
    titles = result.find('div', class_="content_title")
    title = titles.find('a').text
    bodies = result.find('div', class_="rollover_description")
    body = bodies.find('div', class_="rollover_description_inner").text
    print('----------------')
    print(title)
    print(body)

'''
