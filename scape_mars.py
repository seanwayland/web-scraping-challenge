import time
from splinter import Browser
from bs4 import BeautifulSoup

import pandas as pd
import requests
#executable path

def tryNasa(retries=10):


        #executable_path = {'executable_path': 'chomedriver.exe'}
        executable_path = {'executable_path': 'chromedriver.exe'}
        browser = Browser('chrome', **executable_path, headless=True)
        url = 'https://mars.nasa.gov/news/?'
        browser.visit(url)
        html = browser.html
        time.sleep(5)
        # Parse HTML with Beautiful Soup
        soup = BeautifulSoup(html, 'html.parser')
        try:
            #get and print the latest news title and teaser paragraph
            latest_news_title = soup.find(class_='list_text').find('a').text
            #print(latest_news_title)
            latest_teaser = soup.find('div', class_='list_text').find('div', class_='article_teaser_body').text
            #print(latest_teaser)

        except AttributeError as err:
            print(err)
            if retries < 1:
                raise ValueError('No more retries!')
            return tryNasa(retries - 1)



def scrape():

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)
    # HTML object

    tryNasa()





    url = 'https://mars.nasa.gov/news/?'
    browser.visit(url)
    html = browser.html
    time.sleep(5)
    # Parse HTML with Beautiful Soup
    soup = BeautifulSoup(html, 'html.parser')

    #get and print the latest news title and teaser paragraph
    latest_news_title = soup.find(class_='list_text').find('a').text
    #print(latest_news_title)
    latest_teaser = soup.find('div', class_='list_text').find('div', class_='article_teaser_body').text
    #print(latest_teaser)




    url2 = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url2)
    time.sleep(3)
    browser.click_link_by_partial_text('FULL IMAGE')
    html = browser.html
    time.sleep(3)
    # Parse HTML with Beautiful Soup

    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a', class_= 'fancybox')
    images = []
    for val in a:
        images.append(val.get('data-fancybox-href'))

    imgURL = images[1]
    baseURL = 'https://www.jpl.nasa.gov'
    fullURL = baseURL + imgURL

    #print(fullURL)


    twitter_url = 'https://twitter.com/marswxreport?lang=en'
    result = requests.get(twitter_url)
    #print(result)
    html = result.text

    #create BeautifulSoup object and parse
    soup = BeautifulSoup(html, 'html.parser')
    #get the weather from the newest tweet
    mars_weather = soup.find(class_='tweet-text').get_text()
    #print(mars_weather)


    facts_url = 'https://space-facts.com/mars/'
    data = pd.read_html(facts_url)
    #print(data)
    data = pd.DataFrame(data)

    #convert the data to a HTML table string
    html_table = data.to_html()


    html_table = html_table.replace('\n', '')

    #print(html_table)



    hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemisphere_url)
    time.sleep(2)
    #html = browser.html
    imageURLS = []

    for i in range(4):

        links_found = browser.links.find_by_partial_text('Enhanced')
        time.sleep(2)
        links_found[i].click()
        soup = BeautifulSoup(browser.html, 'html.parser')
        title = (soup.find('h3').text).replace(' Enhanced', '')
        #find the full image
        im = soup.find('a', text='Sample')
        #get the images url
        img_url = im['href']

        #make a dictionary and append to the list
        imageURLS.append({'title': title, 'img_url': img_url})

        #go back
        browser.back()

    #print(imageURLS)
    result = { "latest_news_title": latest_news_title,"latest_teaser": latest_teaser,
               "latest_image": fullURL, "weather_tweet": mars_weather, "Facts_table": html_table, "Images_URLS": imageURLS}

    browser.quit()

    return result


#print(scrape())



