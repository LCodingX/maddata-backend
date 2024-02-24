#Document your dependencies in a requirements.txt file, which you can generate using pip freeze > requirements.txt 
#and recreate using pip install -r requirements.txt.
#Include the virtual environment directory in your .gitignore file 
#(or equivalent for other version control systems) to avoid committing it to version control.
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client
import json
from xdict import xdict

# Define a function to get the average of a list of numbers
def get_average(data):
    sum = 0
    for i in data:
        sum += i
    return sum / len(data)

# Define a function to substitute a product name to an index in the form of xn
def substitute_product_to_index(product):
    return None

# Define a function to calculate the price of a pizza
def pizza_price(bread, cheese, tomato):
    pizza = 0.5 * bread + 1 * cheese + 0.3 * tomato
    return pizza

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
            response = supabase.table('cost-of-living').select("country", substitute_product_to_index(product)).execute()
            # implement average
        else:
            response = supabase.table('cost-of-living').select("country", substitute_product_to_index(product)).eq('country', country).execute()

        # TODO: add control currency conversion
        controlled_data = []

        return jsonify(controlled_data)
    except Exception as e:
        print("Error fetching data:", str(e))
        return jsonify({"error": "Failed to fetch data"}), 500




# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)