
# import necessary libraries
from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/Mission_to_Mars_DB"
mongo = PyMongo(app)


# Import scrape_mars
import scrape_mars

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/")
def index():
    mars_data = mongo.db.mars_mongo.find_one()
    print(mars_data)
    return render_template("index.html", data=mars_data)



# Import dependencies
@app.route("/scrape")
def scrape_all():
    scrapped_data = scrape_mars.scrape()
    mongo.db.mars_mongo.update({}, scrapped_data, upsert=True)
    return "Finished scrapping"


if __name__ == "__main__":
    app.run(debug=True)

