from flask import Flask, jsonify, request, render_template,send_from_directory
from scripts.predict_property import predict


# Create a Flask application instance
app = Flask(__name__)    

# Define a route to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict_page')
def predict_page():
    # Your prediction logic goes here
    return send_from_directory('templates', 'prediction.html')


@app.route('/predict', methods=['POST'])
def predict_route():
    if request.method == 'POST':
        form_data = request.form
        predicted_price = predict(form_data)
        return jsonify({'predicted_price': predicted_price.tolist()}),200
    
# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
