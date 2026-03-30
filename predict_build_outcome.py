import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load('build_outcome_model.pkl')

# New build data (for prediction)
new_build_data = pd.DataFrame({
    'Build_Time': [15],
    'Tests_Passed': [50],
    'Tests_Failed': [2]
})

# Predict the outcome
prediction = model.predict(new_build_data)
print(f"Predicted Build Outcome: {'Success' if prediction == 1 else 'Failure'}")
