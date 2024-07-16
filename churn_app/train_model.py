import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load your dataset
df = pd.read_csv('customer_churn.csv')

# Check column names
print(df.columns)

# Use the correct feature columns
X = df[['MonthlyCharges', 'tenure']]  # Update with actual column names
y = df['Churn']  # Use the target column

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model in the churn_app directory
joblib.dump(model, 'churn_model.joblib')
