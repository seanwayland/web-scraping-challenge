import time
from selenium import webdriver

url = 'https://mars.nasa.gov/news/?page=0&per_page=1000&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get(url);
time.sleep(5) # Let the user actually see something!
news_title = driver.find('div', class_='list_text').a.text
print(news_title)
news_p = driver.find('div', class_='list_text').find('div', class_='article_teaser_body').text
print(news_p)

