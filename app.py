# app.py
import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.datasets import load_iris

# Load the trained model and scaler
model = joblib.load("iris_model.pkl")
scaler = joblib.load("scaler.pkl")

# Custom CSS to set a background GIF and create a white box for content
def set_background_and_white_box(gif_url):
    st.markdown(
        f"""
        <style>
        /* Set background GIF */
        .stApp {{
            background: url("{gif_url}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}

        /* Create a white box for all content */
        section.main > div {{
            background-color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set the background GIF (replace 'your-gif-url' with the actual URL or path)
set_background_and_white_box("https://bigthink.com/wp-content/uploads/2021/12/ezgif-4-4e46c3553db8.gif")

# App title and description
st.title("Iris Flower Type Predictor")
st.write("""
This app predicts the type of Iris flower based on the measurements you provide below.  
Please adjust the sliders to input flower features, then click **Predict** to see the result.
""")

# Create tabs for prediction and model evaluation
tab1, tab2 = st.tabs(["Make Prediction", "Model Evaluation"])

with tab1:
    # Input sliders
    sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.8)
    sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.0)
    petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 4.0)
    petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 1.2)

    # Prepare input features
    features = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    scaled_features = scaler.transform(features)

    # Predict when the button is clicked
    if st.button("Predict"):
        prediction = model.predict(scaled_features)
        # Get class names from iris dataset
        iris = load_iris()
        class_names = iris.target_names
        predicted_class = class_names[prediction[0]]
        
        st.subheader("Prediction Result")
        st.write(f"The predicted Iris flower type is: **{predicted_class}**")

with tab2:
    st.subheader("Model Evaluation Metrics")
    
    # Load iris dataset for evaluation
    iris = load_iris()
    X = iris.data
    y = iris.target
    
    # Scale the features
    X_scaled = scaler.transform(X)
    
    # Get predictions
    y_pred = model.predict(X_scaled)
    
    # Display options
    plot_options = st.multiselect(
        "Select plots to display:", 
        ["Confusion Matrix", "Classification Report"],
        default=["Confusion Matrix"]
    )
    
    if "Confusion Matrix" in plot_options:
        st.subheader("Confusion Matrix")
        cm = confusion_matrix(y, y_pred)
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=iris.target_names, yticklabels=iris.target_names)
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
        st.pyplot(fig)
        
   
    if "Classification Report" in plot_options:
        # Display classification report
        st.subheader("Classification Report")
        report = classification_report(y, y_pred, target_names=iris.target_names)
        st.text(report)