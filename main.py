import pickle

import pandas as pd
from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from sklearn.linear_model import LinearRegression

# cspell:ignore jsonify
app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

calorie_model = pickle.load(open('calorias.pkl', 'rb'))
steps_model = pickle.load(open('passos.pkl', 'rb'))


@app.route('/calorias', methods=['GET'])
@cross_origin()
def calories():
    workout_type = request.args.get('workout_type')
    time = request.args.get('time')
    df = pd.DataFrame({
        'workout_type': workout_type,
        'time': time
    }, index=[0])
    print(df)
    prediction = calorie_model.predict(df)

    return jsonify({'prediction': prediction[0]})


@app.route('/passos', methods=['GET'])
@cross_origin()
def steps():
    workout_type = request.args.get('workout_type')
    time = request.args.get('time')
    distance = request.args.get('distance')
    df = pd.DataFrame({
        'workout_type': workout_type,
        'time': time,
        'distance': distance
    }, index=[0])

    prediction = steps_model.predict(df)

    return jsonify({'prediction': prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)
