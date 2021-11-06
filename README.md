# Final Project

## Steps

#### 1) Create a new environment

#### 2) pip install requirements
Likely Need
- flask
- python-dotenv
- pandas
- gunicorn

if you are using postgres
- sqlalchemy
- psycopg2 (if this gives you an error, try psycopg2-binary)

#### 3) pip freeze > requirements.txt (delete the data requirement)

#### 4) delete the dataclasse library from the requirements.txt

### 4) in Heroku add a config variable that is your database url 

The config variable called DATABASE_URL that automatically populates with the Heroku Postgres Add-on is missing 'ql' at the end of 'postgres' at the start of the url. You can not edit this directly. So you need to make a new key:value pair below it. 
