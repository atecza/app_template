#IMPORT NECESSARY LIBRARIES
import joblib  #for importing your machine learning model
from flask import Flask, render_template,request, jsonify, make_response, url_for, redirect
import pandas as pd 



# SQLALCHEMY SETUP
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import psycopg2

#os allows you to call in environment variables
# we will set the remote environment variables in heroku 
import os 


#################################################
# Database Setup
#################################################

#make sure you have your own .env on your computer

#pg_user = os.getenv("DB_USER")
#pg_pwd = os.getenv("DB_PASSWORD")
#pg_port = "5432"
#rds = os.getenv("DB_ADDRESS")

#database = '<name of your database>'

#url = f"postgresql://{pg_user}:{pg_pwd}@{rds}:{pg_port}/{database}"


#engine = create_engine(f'{url}')

# reflect an existing database into a new model
#Base = automap_base()

# reflect the tables
#Base.prepare(engine, reflect=True)

# Save reference to the table
#tablename = Base.classes.tablename

# create instance of Flask app
app = Flask(__name__)

#model = joblib.load("<filepath to saved model>")

#check that you have your model 
#print(model)

# create route that renders index.html template
@app.route("/", methods=["GET"])
def home():
    
    return render_template("index.html")


# route to make prediction off of model
@app.route("/predict", methods=["POST"])
def results():      
      
    # if you are plugging user values into a model
    # get the variables from your html form. these always come in as string
    # you will need to have form inputs in your html with a name attribute
    variable_1= int(request.form.get("variable_1"))  
    variable_2= request.form.get("variable_2")   
       
     
    # line up values to match model values and predict
    outcome = model.predict([[variable_1,variable_2]])
   
   #you may need to do some things to the outcome before retuning it
    
    #need to double check that passing variable works with redirect
    return redirect(url_for('app.home', outcome=outcome))
    

#make an endpoint for data you are using in charts. You will use JS to call this data in
#using d3.json("/api/data")
@app.route("/api/data")
def data():
    
    
    # Create our session (link) from Python to the DB
    #session = Session(engine)
    
    #Query Database
    #your_query = session.query()
    
    lat_long = [(-12.35,24),()]

    
    #Convert Query to json object
    #Consider how you want your data to be structured to easily pass into visuals
    #final sturcture should be in a list or dictionary
    
    #example: in this case the list of values would be derived from your query
    my_data = {'map_array':lat_long}
        
    #session.close()
    
    #Return the JSON representation of your dictionary
    return (jsonify(my_data))

if __name__ == '__main__':
    app.run(debug=True)