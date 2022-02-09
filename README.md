# Flask Project

## Steps

#### 1) Create a new virtual conda environment, activate that environment
This is not necessary, but will make deploying to heroku more efficient. When you pip freeze your requierment's file, you
will only capture the libraries necessary to run your app. 

#### 2) pip install requirements
Likely Need
- flask
- python-dotenv
- pandas
- gunicorn

if you are using postgres
- sqlalchemy
- psycopg2 (if this gives you an error, try psycopg2-binary)

#### 3) pip freeze > requirements.txt 
This step has already been done for you. Only repeat if you have add new libraries not included here

#### 4) delete the dataclasse library from the requirements.txt
If you remake the requirements.txt file, delete the dataclasse library. It throws an error in Heroku

### 5) in Heroku add a config variable that is your database url 

The config variable called DATABASE_URL that automatically populates with the Heroku Postgres Add-on is missing 'ql' at the end of 'postgres' at the start of the url. You can not edit this directly. So you need to make a new key:value pair below it. 

For this app I called the new DATABASE_URL just URL. 

### 6) Make sure you have a .env file on the same level as thr app.py. Assign the url for the postgres database to the same variable name as you did in Heroku. For this app, my .env contains:

URL = postgresql://.....(full url from heroku postgres config variables)

