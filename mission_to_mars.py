def scrape():
    import pandas as pd
    import pymongo
    import requests
    import json
    from splinter import Browser
    from bs4 import BeautifulSoup as bs
    from webdriver_manager.chrome import ChromeDriverManager
    
    # Setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    # Import Packages
    # Identify HTML code for redplanetscience
    url = 'https://redplanetscience.com/'

    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Pull first title and paragraph from news article
    news_title = soup.find_all('div', class_='content_title')[0].text
    news_paragraph = soup.find_all('div', class_='article_teaser_body')[0].text

    # Identify HTML code for spaceimages-mars
    url = 'https://spaceimages-mars.com/'

    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Pull url extention and add it to url
    image_url = url + soup.find_all('img', class_='thumbimg')[0]['src']

    # Identify HTML code for spaceimages-mars
    url = 'https://galaxyfacts-mars.com/'
    table = pd.read_html(url)

    # Identify HTML code for marshemispheres
    url = 'https://marshemispheres.com/'

    browser.visit(url)
    html = browser.html
    soup = bs(html, 'html.parser')

    # Pull list of url extensions
    url_list = []
    for i in range(0, 8):
        ext = soup.find_all('a', class_='itemLink product-item')[i]['href']
        url_list.append(ext)

    # Step through each link and access each image url
    title_list = []
    image_url_list = []

    for i in range(0, 8, 2):
        browser.visit(url + url_list[i])
        html = browser.html
        soup = bs(html, 'html.parser')

        tif_url = url + soup.find_all('a')[6]['href']
        image_title = soup.find_all('h2', class_='title')[0].text

        image_url_list.append(tif_url)
        title_list.append(image_title)
    # creates a dictionary with all the scraped information
    mars_dict = {
        "title": news_title,
        "paragraph": news_paragraph,
        "image url": image_url,
        "facts1": list(table[0][0]),
        "facts2": list(table[0][1]),
        "image url list": image_url_list,
        "title list": title_list
    }    
    browser.quit()

    return mars_dict
