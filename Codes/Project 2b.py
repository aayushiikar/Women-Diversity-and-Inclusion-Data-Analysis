import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load your dataset
df = pd.read_csv(r"C:\Users\aayus\Downloads\Higher Education.csv")
df = df.dropna()

# Sidebar title
st.sidebar.title("Higher Education Regression App")

# Display raw data if checkbox is selected
if st.sidebar.checkbox("Show Raw Data"):
    st.write(df)

# Sample code (modify based on your dataset)
# Data preprocessing
# ... (handle missing data, encode categorical variables)

# Feature selection
features = ['Level - Ph.d', 'Level - M.Phil', 'Level - Post Graduate', 'Level - Under Graduate', 'Level - PG Diploma', 'Level - Diploma', 'Level - Certificate', 'Level - Integrated']

# Split the data
X = df[features]
y = df['Level - Total']  # Assuming 'Level - Total' is the target variable (GPI)

# Train the model
model = RandomForestRegressor()
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Calculate MSE
mse = mean_squared_error(y, y_pred)

# Streamlit UI
st.title("Higher Education Regression Model")
st.subheader("Predicting 'Level - Total' (GPI)")

# Add sliders for user input
st.sidebar.subheader("Input Features for Prediction")
feature_sliders = {}
for feature in features:
    feature_sliders[feature] = st.sidebar.slider(f"Select {feature}", float(df[feature].min()), float(df[feature].max()), float(df[feature].mean()))

# Predict button
if st.sidebar.button("Predict"):
    # Create a DataFrame from the user input
    user_input = pd.DataFrame([feature_sliders])
    
    # Make predictions
    prediction = model.predict(user_input)

    # Display the prediction
    st.subheader("Prediction")
    st.write(f"The predicted 'Level - Total' (GPI) is: {prediction[0]:.2f}")

# Display evaluation metrics
st.sidebar.subheader("Model Evaluation")
st.sidebar.write(f"Mean Squared Error: {mse:.4f}")

# Display feature importances
# Display feature importances
# Display feature importances
st.subheader("Feature Importances")
feature_importances_df = pd.DataFrame({'Feature': features, 'Importance': model.feature_importances_})
st.bar_chart(feature_importances_df.set_index('Feature'))


