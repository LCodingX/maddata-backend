#Document your dependencies in a requirements.txt file, which you can generate using pip freeze > requirements.txt 
#and recreate using pip install -r requirements.txt.
#Include the virtual environment directory in your .gitignore file 
#(or equivalent for other version control systems) to avoid committing it to version control.
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client
import json



# Create a Flask app
app = Flask(__name__)
# Create a Supabase client
database_url = os.environ.get('FLASK_DATABASE_URL')
database_key = os.environ.get('FLASK_DATABASE_KEY')
print(database_url)
print(database_key)

supabase = create_client(
    database_url,
    database_key
)

# Define a route to get all users
@app.route("/hello-world")
def hello():
    return "hello world"

@app.route("/")
def get():
    data = supabase.table("cost-of-living").select("*").execute().data
    print(data)
    return json.dumps(data)


# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)