from churn_app.ml_model import predict_churn

# Test the prediction function
feature1 = 100
feature2 = 75.50
prediction = predict_churn(feature1, feature2)
print(f'Prediction: {prediction}')
