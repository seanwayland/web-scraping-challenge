from flask import Flask, jsonify, render_template

from flask import Flask, render_template

from scape_mars import scrape

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo

# Create an instance of our Flask app.
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
marsDatabase = client.marsDb

'''Define the Routes'''

#index
@app.route('/')
def index():
    mars = marsDatabase.find_one()
    return render_template('index.html', mars=mars)

@app.route('/scrape')
def scrapethatbadboy():
    mars = marsDatabase
    mars_data = scrape()
    #update the mars db w/ mars_data
    mars.update({}, mars_data, upsert=True)
    return index()

#run the app
if __name__ == '__main__':
    app.run(debug=True)

