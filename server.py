from flask import Flask, jsonify, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load model
model = joblib.load('house_price_model.pkl')

# Expected columns (same as training)
expected_cols = [
    "total_sqft", "bath", "balcony",
    "area_type", "availability", "location",
    "size", "society"
]

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Create DataFrame with correct column order
    df = pd.DataFrame([[data.get(col) for col in expected_cols]], columns=expected_cols)

    # Predict
    prediction = model.predict(df)[0]

    return jsonify({'predicted_price': float(prediction)})

if __name__ == '__main__':
    app.run(debug=True)