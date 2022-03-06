import pickle
from flask import Flask, jsonify, request

from Converted_predict_service import predict_single

app = Flask('Converted-predict')

with open('modelo/converted-modelo.pck', 'rb') as f:
    dv, model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()
    converted, prediction = predict_single(customer, dv, model)

    result = {
        'Converted': bool(converted),
        'Converted_probability': float(prediction),
    }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=8000)