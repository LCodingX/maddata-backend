#Document your dependencies in a requirements.txt file, which you can generate using pip freeze > requirements.txt 
#and recreate using pip install -r requirements.txt.
#Include the virtual environment directory in your .gitignore file 
#(or equivalent for other version control systems) to avoid committing it to version control.
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client
import json
from xdict import xdict

# gets the average cost of the product per control unit for all countries
def get_avg_all_countries(product_res, product, control="usd", control_res=[]):
    country_dict_product = {}
    for dict in product_res:
        if (dict[product] == None) or (dict[product] == "nan"): 
            continue
        if dict["country"] not in country_dict_product.keys():
            country_dict_product[dict["country"]]=[1, float(dict[product])]
        else:
            country_dict_product[dict["country"]][0]+=1
            country_dict_product[dict["country"]][1]+=float(dict[product])
    final_res = {}
    final_res_control={}
    for country in country_dict_product.keys():
        final_res[country]=country_dict_product[country][1]/country_dict_product[country][0]
    print(final_res["United States"])
    if len(control_res)>0:    
        country_dict_control = {}
        for dict in control_res:
            if (dict[control] == None) or (dict[control] == "nan"): 
                continue
            if dict["country"] not in country_dict_control.keys():
                country_dict_control[dict["country"]]=[1, float(dict[control])]
            else:
                country_dict_control[dict["country"]][0]+=1
                country_dict_control[dict["country"]][1]+=float(dict[control])
        final_res_control = {}
        for country in country_dict_control.keys():
            final_res_control[country]=(country_dict_control[country][1]/country_dict_control[country][0])   
    else:
        return final_res    
    for country in country_dict_product.keys():
        if country not in final_res_control.keys():
            del final_res[country]
        else:
            final_res[country] /= final_res_control[country]
    print(final_res_control["United States"])
    print(final_res["United States"])
    return final_res

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

        xdict[product] #if key doesn't exist, an error will be thrown
        control = request.args.get('control')
        if control is None:
            control = 'usd'
        elif (control!='usd'):
            xdict[control] #same thing here

        country = request.args.get('country')
        if country is None:
            country = 'all'
        
        if country == 'all':
            res = []
            response = supabase.table('cost-of-living').select(f"country, {substitute_product_to_index(product)}").execute().data
            
            if (control!='usd'):
                control_response=supabase.table('cost-of-living').select(f"country, {substitute_product_to_index(control)}").execute().data
                res = get_avg_all_countries(response, substitute_product_to_index(product), substitute_product_to_index(control), control_response)
            else:
                res = get_avg_all_countries(response, substitute_product_to_index(product))
            return jsonify(res)
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