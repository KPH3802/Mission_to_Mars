
# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    player_dictionary = {"player_1": "Jessica",
                         "player_2": "Mark"}
    return render_template("index.html", dict=player_dictionary)



# Import dependencies
def scrape():
    mission_to_mars_dict = {}

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



    # NASA MARS NEWS:
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    # Find title and place it into a variable
    news_title = soup.find('div', class_="content_title").text

    # Find paragraph text and put it into a variable
    news_p = soup.find('div', class_="article_teaser_body").text

    # Put variables into dictionary
    mission_to_mars_dict["news_title"] = news_title
    mission_to_mars_dict["news_p"] = news_p



    # JPL Mars Space Images - Featured Image

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
    # Add to apps dictionary
    mission_to_mars_dict["featured_image_url"] = featured_image_url




    # MARS WEATHER
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_weather = soup.select('span', class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
    # Add to apps dictionary
    mission_to_mars_dict["mars_weather"] = mars_weather



    # MARS FACTS

    # Set url
    url = 'https://space-facts.com/mars/'
    # Use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    table = pd.read_html(url)

    # Use Pandas to convert the data to a HTML table string. 
    table_html_string = table[1].to_html()
    # Add to apps dictionary
    mission_to_mars_dict["table_html_string"] = table_html_string




    # MARS HEMISPHERE
    # Go to url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    hemi_attributes_list = soup.find_all('a', class_="itemLink product-item")
    print(hemi_attributes_list[1]['href'])

    hemisphere_image_urls = []
    for hemi_img in hemi_attributes_list:
        if hemi_img.find('h3') == None:
            pass
        else:
            img_title = hemi_img.find('h3').text
            #print(img_title)
            link_to_img = "https://astrogeology.usgs.gov/" + hemi_img['href']
            #print(link_to_img)
            img_request = req.get(link_to_img)
            soup = BeautifulSoup(img_request.text, 'lxml')
            img_tag = soup.find('div', class_='downloads')
            img_url = img_tag.find('a')['href']
            hemisphere_image_urls.append({"title": img_title, "img_url": img_url})
    
    # Add to apps dictionary
    mission_to_mars_dict["hemi_image_dict"] = hemisphere_image_urls
    
    
    browser.quit()


    return render_template("index.html", dict=player_dictionary)


if __name__ == "__main__":
    app.run(debug=True)

