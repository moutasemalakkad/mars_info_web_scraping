from bs4 import BeautifulSoup as soup
from splinter import Browser
import pandas as pd 
import requests 
import time





def init_browser():
    exec_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', headless=True, **exec_path)








def scrape():
    mars_info = {}

    try:
            #initialize a session
        browser = init_browser()
        
        #visit the website
        browser.visit('https://mars.nasa.gov/news/')
        
        #obtain the html content
        html = browser.html
        
        
        #create a soup object
        soup_nasa = soup(html, 'lxml')
        
        #scrape desired info
        news_title = soup_nasa.find('div', class_='content_title').find('a').text
        news_p = soup_nasa.find('div', class_='article_teaser_body').text
        
        
        #add to dictionary
        mars_info['news_title'] = news_title
        mars_info['news_paragraph'] = news_p

        time.sleep(3)



        #visit website
        browser.visit('https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars')

        #get HTML object
        html = browser.html

        # create a soup object
        soup_image = soup(html, 'lxml')

        # Get the url
        url_image = soup_image.find('a', class_="button fancybox")['data-fancybox-href']
        
        # create a full link
        featured_image_url = f"https://www.jpl.nasa.gov{url_image}"

        featured_image_url

        mars_info['image_link'] = featured_image_url


        time.sleep(3)

     
        #visit website
        browser.visit('https://twitter.com/marswxreport?lang=en')

        #get HTML object
        html = browser.html

        # create a soup object
        soup_weather = soup(html, 'lxml')

        # Get the url
        mars_weather = soup_weather.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text

        mars_info['weather'] = mars_weather


        time.sleep(3)


        #visit website
        browser.visit('https://space-facts.com/mars/')


        #read table using pandas
        table = pd.read_html('https://space-facts.com/mars/')

        # get the zeroes object (return a list - grab df)
        df_mars = table[0]

        #reset indexes to one of the values
        df_mars.set_index('Mars - Earth Comparison', inplace=True)

        # get html raw data
        html_data = df_mars.to_html()

        html_data = html_data.replace("\n", "")
        #push to dictionary
        mars_info['facts'] = html_data


        time.sleep(3)

        
        #visit website
        browser.visit('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')


        #read table using pandas
        #table = pd.read_html('https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars')

        #get HTML object
        html = browser.html

        # create a soup object
        soup_hemp = soup(html, 'lxml')

        # Scrape
        items_hem = soup_hemp.find_all('div', class_='item')

        # URL
        url_hem = 'https://astrogeology.usgs.gov'
        
        # decalare a list to push dicts to
        dic_list = []

        # loop thorugh the soup object we created earlier
        for item in items_hem:
            #print(item)
            #print('-----------------')

            # grab title
            title = item.find('h3').text
            #print(title)

            # grab partial url
            partial_url = item.find('a')['href']
            #print(partial_url)
            
            # make full url
            full_url = url_hem + partial_url
            #print(full_url)
            
            # visit full url to obatin the image
            browser.visit(full_url)
            
            #HTML object
            page_item = browser.html
            
            # scrape image info
            soup_item = soup(page_item, 'lxml')
            
            #get images' full url
            full_url = soup_item.find('div', class_='downloads').find('a')['href']
            #print(full_url)
            

            # append to global dic
            dic_list.append({'title': title,
                            'url': full_url})

            # dic within mars_info dic
        mars_info['hemp'] = dic_list


    finally:
             browser.quit() 
    


    return mars_info
        












