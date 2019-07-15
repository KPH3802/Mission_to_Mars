

# Import dependencies
def scrape():

    from bs4 import BeautifulSoup
    import requests
    from splinter import Browser
    from IPython.display import display_html
    import pandas as pd

    # Showing the chromdriver I'm using
    !which chromedriver

    # Executable path and fire up browser, headless set to True so the browser operates in the background invisible"
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find title and place it into a variable
    news_title = soup.find('div', class_="content_title").text

    # Find paragraph text and put it into a variable
    news_p = soup.find('div', class_="article_teaser_body").text

    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    #Use splinter to navigate the site and find the image url for the current Featured Mars Image
    browser.click_link_by_partial_text('FULL IMAGE')

    browser.click_link_by_partial_text('more info')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Assign the url string to a variable called featured_image_url.
    image = soup.find('img', class_= "main_image")
    featured_image_url = "https://www.jpl.nasa.gov" + image["src"]


    # MARS WEATHER
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.select('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")

    # MARS FACTS

    # Set url
    url = 'https://space-facts.com/mars/'
    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    table = pd.read_html(url)

    # Use Pandas to convert the data to a HTML table string. 
    table_html_string = table[1].to_html()

    # MARS HEMISPHERE
    # Go to url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Use splinter to navigate the page clicking links to hemispheres
    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')

    browser.click_link_by_partial_text('Open')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_Cerberus = soup.find('img', class_= "wide-image")

    # Go to url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Use splinter to navigate the page clicking links to hemispheres
    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')

    browser.click_link_by_partial_text('Open')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_Schiaparelli = soup.find('img', class_= "wide-image")

    # Go to url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Use splinter to navigate the page clicking links to hemispheres
    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')

    browser.click_link_by_partial_text('Open')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_Syrtis = soup.find('img', class_= "wide-image")

    # Go to url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    # Use splinter to navigate the page clicking links to hemispheres
    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')

    browser.click_link_by_partial_text('Open')

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    image_Valles = soup.find('img', class_= "wide-image")



