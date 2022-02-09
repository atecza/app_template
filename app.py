#IMPORT NECESSARY LIBRARIES
#import joblib  #for importing your machine learning model
from flask import Flask, render_template, request, jsonify, make_response
import pandas as pd 


# SQLALCHEMY SETUP
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2

#os allows you to call in environment variables
# we will set the remote environment variables in heroku 
from dotenv import load_dotenv
import os 

load_dotenv()


#################################################
# Database Setup
#################################################

#make sure you have your own .env on your computer
#comment out when you plan to deploy from heroku

url = os.getenv('URL')


#uncomment line below when you want to deploy to heroku
#url = os.environ.get("URL")


engine = create_engine(f'{url}')


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#my table in pgadmin (postgres) is named envdata
EnvironmentData = Base.classes.envdata

# create instance of Flask app
app = Flask(__name__)


# create route that renders index.html template
@app.route("/", methods=["GET","POST"])
def home():
       
    return render_template("index.html")


#make an endpoint for data you are using in charts. You will use JS to call this data in
#using d3.json("/api/data")
@app.route("/api/data")
def data():
    
    
    # Create our session (link) from Python to the DB
    #session = Session(engine)
    
    #Query Database. Check SqlAlchemy documentation for how to query
    
    #Convert your query object into a list or dictionary format so it can
    # be jsonified
    
        
    #session.close()
    
    #Return the JSON representation of your dictionary
    return ('jsonify(myData)')

if __name__ == '__main__':
    app.run(debug=True)
