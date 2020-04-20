import time
from splinter import Browser
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd
import requests
#executable path


executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)
# HTML object
url = 'https://mars.nasa.gov/news/?'
browser.visit(url)
html = browser.html
time.sleep(5)
# Parse HTML with Beautiful Soup
'''
soup = BeautifulSoup(html, 'html.parser')
# Parse HTML with Beautiful Soup

#get and print the latest news title and teaser paragraph
latest_news_title = soup.find(class_='list_text').find('a').text
print(latest_news_title)
latest_teaser = soup.find('div', class_='list_text').find('div', class_='article_teaser_body').text
print(latest_teaser)


'''





url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
browser.visit(url2)
time.sleep(5)
browser.click_link_by_partial_text('FULL IMAGE')
html = browser.html
time.sleep(5)
# Parse HTML with Beautiful Soup

soup = BeautifulSoup(html, 'html.parser')
a = soup.find_all('a', class_= 'fancybox')
images = []
for val in a:
    images.append(val.get('data-fancybox-href'))

imgURL = images[1]
baseURL = 'https://www.jpl.nasa.gov'
fullURL = baseURL + imgURL

print(fullURL)

'''
imgURL = a.get('data-fancybox-href')
baseURL = 'https://www.jpl.nasa.gov'
fullURL = baseURL+ imgURL
print(fullURL)
'''



