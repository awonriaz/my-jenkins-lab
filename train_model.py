import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load past build data
data = {
    'Build_Time': [15, 12, 10, 20, 18, 11, 14, 22, 16, 9, 13, 17, 19, 21, 8, 25, 23, 7, 24, 10,
                   16, 14, 11, 20, 15, 12, 9, 18, 22, 13, 17, 10, 21, 8, 24, 19, 11, 15, 23, 12],
    'Tests_Passed': [50, 45, 55, 40, 48, 52, 47, 38, 51, 58, 53, 46, 42, 39, 60, 35, 37, 62, 36, 56,
                     49, 54, 57, 41, 50, 44, 59, 43, 37, 52, 47, 55, 40, 61, 38, 45, 53, 51, 39, 46],
    'Tests_Failed': [2, 5, 0, 7, 3, 1, 4, 8, 2, 0, 1, 4, 6, 8, 0, 10, 9, 0, 9, 1,
                     3, 1, 0, 6, 2, 5, 0, 4, 8, 2, 3, 0, 7, 0, 9, 5, 1, 2, 7, 4],
    'Build_Outcome': [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1,
                      1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0] # 1: Success, 0: Failure
}
df = pd.DataFrame(data)

# Features and target
X = df[['Build_Time', 'Tests_Passed', 'Tests_Failed']]
y = df['Build_Outcome']

# Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Model Accuracy: {accuracy:.2f}')

# Save the trained model
joblib.dump(model, 'build_outcome_model.pkl')
print("Model 'build_outcome_model.pkl' saved.")
