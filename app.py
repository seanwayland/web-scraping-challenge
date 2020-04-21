
from flask import Flask, render_template, jsonify

from scape_mars import scrape

from database import getLatest, update

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

#update()
#index
@app.route('/')
def index():
    mars = getLatest()
    return render_template('index.html', mars = mars )

@app.route('/scrape')
def scrapethatbadboy():
    update()

    return index()

#run the app
if __name__ == '__main__':
    app.run(debug=True)

