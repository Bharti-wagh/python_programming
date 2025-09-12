#EXPLORE THE 'FLASK' MODULE AND CREATE A WEB SERVER USING FLASK AND PYTHON 
from flask import Flask

# Create Flask app
app = Flask(__name__)

# Define a route (homepage)
@app.route("/")
def home():
    return "<h1>Hello, Flask!</h1><p>Welcome to my web server.</p>"

# Run the server
if __name__ == "__main__":
    app.run(debug=True)
