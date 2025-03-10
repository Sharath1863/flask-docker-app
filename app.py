from flask import Flask, jsonify

# Create a Flask app instance
app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return jsonify(message="Hello, Flask API!")  # Return a JSON response

# Run the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
