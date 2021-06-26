import pandas as pd
import pymongo

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
from mission_to_mars import *

app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'
mongo = PyMongo(app, uri=conn)

@app.route("/")
def home():
    mars_data = mongo.db.mars.find_one()
    return render_template('index.html', mars_data = mars_data)

@app.route("/scrape")
def mars_scrape():
    
    data = [scrape()]
    
    mongo.db.mars.drop()
    mongo.db.mars.update({}, data, upsert=True)  

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
    
    
    
# Create and Clean Dataframe
#table_df = pd.DataFrame(table[0])
#table_df = table_df[table_df.columns[0:2]]
#table_df.columns = table_df.iloc[0]
#table_df = table_df[1:]