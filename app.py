#Document your dependencies in a requirements.txt file, which you can generate using pip freeze > requirements.txt 
#and recreate using pip install -r requirements.txt.
#Include the virtual environment directory in your .gitignore file 
#(or equivalent for other version control systems) to avoid committing it to version control.
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client
import json
from xdict import xdict
def get_average(data):
    sum = 0
    for i in data:
        sum += i
    return sum / len(data)


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

@app.route("/api/products/<product>/", methods=['GET'])
def getProducts(product):
    try:
        control = request.args.get('control')
        if control is None:
            control = 'USD'

        country = request.args.get('country')
        if country is None:
            country = 'All'
        
        if country == 'All':
            response = supabase.table('cost-of-living').select("country", ).eq("", product).execute()



        index = product # TODO: set index
        response = supabase.table('cost-of-living').select(index).execute()
        print(response)
        return jsonify(response.data)
    except Exception as e:
        print("Error fetching data:", str(e))
        return jsonify({"error": "Failed to fetch data"}), 500




# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)