from django.shortcuts import render
from rest_framework.decorators import api_view
import joblib
import os

# Load the saved model from the churn_app directory
model_path = os.path.join(os.path.dirname(__file__), 'churn_model.joblib')
model = joblib.load(model_path)

@api_view(['GET', 'POST'])
def predict(request):
    prediction = None
    error = None
    try:
        if request.method == 'POST':
            feature1 = float(request.POST.get('feature1'))
            feature2 = float(request.POST.get('feature2'))

            # Create input array for prediction
            input_features = [[feature1, feature2]]

            # Perform prediction using the loaded model
            prediction = model.predict(input_features)[0]

        return render(request, 'index.html', {'prediction': prediction, 'error': error})
    except Exception as e:
        error = str(e)
        return render(request, 'index.html', {'prediction': prediction, 'error': error})
