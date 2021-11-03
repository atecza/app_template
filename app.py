#IMPORT NECESSARY LIBRARIES
import joblib  #for importing your machine learning model
from flask import Flask, render_template, request, jsonify, make_response, url_for, redirect, session
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
url = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY')

#print(url)

#use the url from heroku
#url = os.environ.get("URL")
#url = os.environ.get("SECRET_KEY")

engine = create_engine(f'{url}')


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
EnvironmentData = Base.classes.envdata

# create instance of Flask app
app = Flask(__name__)

#set secret key
app.secret_key = SECRET_KEY

#model = joblib.load("<filepath to saved model>")

#check that you have your model 
#print(model)


# create route that renders index.html template
@app.route("/", methods=["GET","POST"])
def home():
    
    
    if session.get('outcome'):
        
        outcome = session['outcome']
        
        session.pop('outcome')
        
        return render_template("index.html", outcome=outcome)
    
    else:
        outcome = 'What Will Your Value Be?' 
         
        return render_template("index.html", outcome=outcome)


@app.route("/runmodel", methods=["POST"])
def model():
    
    if request.method == 'POST': 
        
        input_1 = request.form.get("dropdown")
        
        if input_1.isnumeric():
            
            variable_1 = int(input_1)

            outcome = variable_1*2
            
        else:
            outcome = None
        
        session['outcome'] = outcome
        
        return redirect(url_for('home'))
    
    return ('this is not the page you are looking for')

#make an endpoint for data you are using in charts. You will use JS to call this data in
#using d3.json("/api/data")
@app.route("/api/data")
def data():
    
    
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    #Query Database
    

    EData = session.query(EnvironmentData).all()
    myData = []

    for x in EData:

        fullEdata = {}

        fullEdata = {
            "Country": x.Country,
            "HDI":x.HDI,
            "Footprint_Crop":x.Footprint_Crop,
            "Footprint_Graze":x.Footprint_Graze,
            "Footprint_Forest":x.Footprint_Forest,
            "Footprint_Carbon":x.Footprint_Carbon,
            "Footprint_Fish":x.Footprint_Fish,
            "Footprint_Total":x.Footprint_Total,
            "Land_Urban":x.Land_Urban,
            "Emission_CO2":x.Emissions_CO2,
            "BioCap":x.Biocapacity_Total,
            "BioCap_RD":x.BioCap_RD,
            "Data_Quality":x.Data_Quality
        }

        myData.append(fullEdata)
        
    session.close()
    
    #Return the JSON representation of your dictionary
    return (jsonify(myData))

if __name__ == '__main__':
    app.run(debug=True)
