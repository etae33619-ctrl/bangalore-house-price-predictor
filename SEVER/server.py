from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_cors import CORS  # Uncommented CORS
import util

app = Flask(__name__)
CORS(app)  # Activated CORS to stop cross-origin browser blocks
util.load_saved_artifacts()


@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    # Changed key to 'locations' (plural) to perfectly match your original app.js code
    response = jsonify({
        'locations': util.get_location_names()
    })
    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])  # Added missing quotes around 'bhk'
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    return response  # Added the crucial missing return statement!


if __name__ == '__main__':
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()  # Added this line so your model and options load up!
    app.run()