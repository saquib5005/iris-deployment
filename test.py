import streamlit as st
import pandas as pd
import numpy as np

# App title
st.title("Streamlit Options Demo")

# Sidebar
st.sidebar.header("Configuration")

# Selectbox (Dropdown)
selected_fruit = st.sidebar.selectbox(
    "Choose a fruit:",
    ["Apple", "Banana", "Mango", "Strawberry"]
)
st.write("Selected fruit:", selected_fruit)

# Radio buttons
experience = st.radio("How was your experience?", ["Poor", "Average", "Good", "Very Good", "Excellent"])
st.write("You rated your experience as:", experience)

# Checkbox
subscribe = st.checkbox("Subscribe to our newsletter")
if subscribe:
    st.success("You are now subscribed to the newsletter.")

# Slider
slider_value = st.slider("Select a number:", 0, 100, 50)
st.write("Slider value:", slider_value)

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Uploaded Data:")
    st.dataframe(df.head())

# Button to generate data
st.subheader("Sample Line Chart")
if st.button("Generate Data"):
    data = pd.DataFrame({
        "X": np.linspace(0, 10, 100),
        "Y": np.sin(np.linspace(0, 10, 100)) + np.random.normal(0, 0.1, 100)
    })
    st.line_chart(data.set_index("X"))

# Multiselect
colors = st.multiselect(
    "Select your preferred colors:",
    ["Red", "Green", "Blue", "Yellow", "Orange"],
    default=["Red", "Blue"]
)
if colors:
    st.write("Selected colors:", ", ".join(colors))
else:
    st.write("No colors selected.")

# Footer
st.markdown("---")
st.caption("Basic Streamlit demo | Sarosh Baig")