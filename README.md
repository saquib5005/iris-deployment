# ⚜️Iris Dataset End-to-End Machine Learning Project 🌸

![Python Version](https://img.shields.io/badge/Python-3.10.0-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-green)

## 🌟Overview

This repository contains an end-to-end machine learning project using the famous **Iris Dataset**. The goal of this project is to classify iris flowers into one of three species (Setosa, Versicolor, or Virginica) based on their sepal and petal dimensions. The project includes data preprocessing, model training, evaluation, and deployment using **Streamlit** for a user-friendly interface.

---

## 📑Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)

---

## Project Description

The Iris Dataset is a classic dataset in machine learning and statistics. It contains 150 samples of iris flowers, with four features:
- **Sepal Length**
- **Sepal Width**
- **Petal Length**
- **Petal Width**

The target variable is the species of the flower, which can be one of the following:
- 🌸 **Setosa**
- 🌼 **Versicolor**
- 🌷 **Virginica**

In this project:
1. **Data Preprocessing**: Cleaned and prepared the dataset for training.
2. **Model Training**: Trained the classification model using Logistic Regression.
3. **Evaluation**: Evaluated the model using metrics like accuracy, precision, recall, and F1-score.
4. **Deployment**: Deployed the trained model using **Streamlit**, allowing users to input features and predict the species of an iris flower.

---

## 💻Technologies Used

- **Programming Language**: Python 3.10.0 🐍
- **Machine Learning Libraries**: Scikit-learn, Pandas, NumPy 🤖
- **Data Visualization**: Matplotlib, Seaborn 📊
- **Deployment Framework**: Streamlit 🚀
- **Version Control**: Git, GitHub 🌐

---

## 🛠️Installation

To run this project locally, follow these steps:

1. **Clone the Repository**📥:
   ```bash
   git clone https://github.com/<your-username>/iris-deployment.git
   cd iris-deployment
   ```
   
2. **Set Up a Virtual Environment**🌱:
   ```bash
   python3 -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**📦:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit App**🚀:
   ```bash
   streamlit run app.py
   ```
---
## **Deployment**

The application is deployed using **Streamlit**🌐. You can access the live app at the following link: https://iris-deployment-saquib.streamlit.app/

---

If you want to deploy your own version of the app, follow the [Streamlit Deployment Guide]([https://docs.streamlit.io/library/deploy](https://docs.streamlit.io/?spm=a2ty_o01.29997173.0.0.6c1ec921jmKg03).

### Usage:
* Open the deployed Streamlit app in your browser🌐.
* Input the value of the iris flower using sliders
* Click the "Predict" button to see the predicted species of the flower🌸.
  
### Acknowledgments
Dataset Source: The Iris Dataset is available in the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/53/iris)📚

Streamlit Documentation: [Streamlit Docs](https://docs.streamlit.io/?spm=a2ty_o01.29997173.0.0.6c1ec921jmKg03)📖

**Inspiration**: This project was inspired by the need to demonstrate a complete machine learning pipeline from data preprocessing to deployment.

### 📄License
This project is licensed under the MIT License.








