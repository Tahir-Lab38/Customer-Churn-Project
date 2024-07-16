import pickle
import numpy as np

# Load your trained model (make sure the path is correct)
with open('churn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict_churn(feature1, feature2):
    # Prepare input data for the model
    input_data = np.array([[feature1, feature2]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Convert prediction to human-readable form
    if prediction[0] == 1:
        return "Churn"
    else:
        return "Not Churn"
