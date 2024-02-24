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

def substitute_product_to_index(product):
    """
    This function takes a product name and returns the corresponding index in the form of xn
    """
    return xdict.get(product)
    
def pizza_price(bread, cheese, tomato):
    """
    This function takes the price of bread, cheese, and tomato and returns the price of a pizza
    """
    pizza = 0.5 * bread + 1 * cheese + 0.3 * tomato
    return pizza

def convert_currency(usd_price, control_price):
    """
    This function takes a price in USD and a price in the control currency and returns the price in the control currency
    """
    return usd_price/control_price

def get_currency_price(data, country, control):
    pass

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
        data = []
        control = request.args.get('control')
        if control is None:
            control = 'usd'
        else:
            control = control.lower()

        country = request.args.get('country')
        if country is None:
            country = 'all'
        
        if country == 'all':
            data = supabase.table('cost-of-living').select(f"country", (substitute_product_to_index(product))).execute()
            # implement average
        else:
            data = supabase.table('cost-of-living').select(f"country", (substitute_product_to_index(product)), (substitute_product_to_index(control))).eq('country', country).execute()
            
        if control == 'usd':
            controlled_data = data
        else:
            controlled_data = convert_currency(data, get_currency_price(data, country, substitute_product_to_index(control)))

        return jsonify(controlled_data)
    except Exception as e:
        print("Error fetching data:", str(e))
        return jsonify({"error": "Failed to fetch data"}), 500




# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)