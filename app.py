#Document your dependencies in a requirements.txt file, which you can generate using pip freeze > requirements.txt 
#and recreate using pip install -r requirements.txt.
#Include the virtual environment directory in your .gitignore file 
#(or equivalent for other version control systems) to avoid committing it to version control.
from flask import Flask, render_template, request, redirect, url_for, jsonify
from supabase import create_client



# Create a Flask app
app = Flask(__name__)
app.config.from_prefixed_env()
# Create a Supabase client
supabase = create_client(
    app.config["DATABASE_URL"],
    app.config["DATABASE_KEY"]
)

# Define a route to get all users
@app.route("/hello-world", method=["GET"])
def hello():
    return "hello world"

@app.route("/", method=["GET"])
def get():
    data = supabase.table("cost-of-living").select("city").eq("city", "Seoul").execute()
    return jsonify(data)


# Start the Flask app
if __name__ == "__main__":
    app.run(debug=True)