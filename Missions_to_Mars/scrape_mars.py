# Import dependencies
from converted_file import scrape
from flask import Flask
import pymongo

# Make a connection to Mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# Define a data base
db = client.scrape_db

# Create the collection
collection = db.scrape_db

# Create the app
app = Flask(__name__)

# Create the /scrape route
@app.route("/scrape")
def Scrape():

    # Return it into a Mongo DB
    collection.insert_one(scrape)

    # Print the dictionary
    return print(scrape)

if __name__ == "__main__":
    app.run(debug=True)