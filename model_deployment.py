
# Importing Required Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import numpy as np
import warnings

def run():
    st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="wide")
    warnings.simplefilter(action='ignore', category=FutureWarning)

    select_page = st.sidebar.radio('Select page', ['Analysis', 'Model Classification', 'About'])

    if select_page == 'Analysis':
        cleaned_data = pd.read_csv('clean_heart.csv')
        st.image('https://th.bing.com/th/id/OIP.nCkh1m-FQ0zwXAv0-9HY6QHaFi?rs=1&pid=ImgDetMain', width=700)
        st.write('### Dataset Overview')
        st.dataframe(cleaned_data.head(10))

        # Create tabs for analysis
        tab1, tab2, tab3 = st.tabs(['Univariate Analysis', 'Bivariate Analysis', 'Multivariate Analysis'])

        # Univariate Analysis for Categorical Features
        tab1.write('### Univariate Analysis with Histogram for Categorical Features')
        categorical_cols = ['Sex', 'ChestPainType', 'RestingECG', 'ExerciseAngina', 'ST_Slope']
        for col in categorical_cols:
            fig = px.histogram(cleaned_data, x=col, color=col)
            tab1.plotly_chart(fig, use_container_width=True)

        # Bivariate and Multivariate Analysis for Numerical Features
        numerical_cols = ['Age', 'RestingBP', 'Cholesterol', 'MaxHR', 'Oldpeak']
        tab2.write('### Bivariate Analysis: Numerical Features vs Heart Disease')
        select_feature = tab2.selectbox('Select Feature', numerical_cols)
        fig2 = px.box(cleaned_data, x='HeartDisease', y=select_feature, color='HeartDisease')
        tab2.plotly_chart(fig2, use_container_width=True)

        tab3.write('### Correlation Heatmap for Numerical Features')
        corr_matrix = cleaned_data[numerical_cols].corr()
        fig3 = px.imshow(corr_matrix, text_auto=True, color_continuous_scale='RdBu_r')
        tab3.plotly_chart(fig3, use_container_width=True)

    elif select_page == 'Model Classification':
        st.title('Heart Disease Prediction Model')
        st.image('stroke.jpg', width=700)

        # Load the model
        model = joblib.load('HeartDisease.pkl')

        # Input fields for model prediction
        inputs = collect_user_input()

        if st.button('Predict'):
            df = pd.DataFrame([inputs])
            result = model.predict(df)[0]
            display_prediction(result)

    elif select_page == 'About':
        display_about_info()

    
    display_footer()

def collect_user_input():
    st.sidebar.header('Enter Your Health Details:')
    inputs = {
        'Sex': st.sidebar.selectbox('Sex', ['M', 'F']),
        'Age': st.sidebar.slider('Age', 28, 77, 54),
        'ChestPainType': st.sidebar.selectbox('Chest Pain Type', ['ASY', 'NAP', 'ATA', 'TA']),
        'RestingBP': st.sidebar.slider('Resting Blood Pressure', 90, 170, 130),
        'Cholesterol': st.sidebar.slider('Cholesterol', 33, 408, 224),
        'FastingBS': st.sidebar.selectbox('Fasting Blood Sugar > 120 mg/dl', [0, 1]),
        'RestingECG': st.sidebar.selectbox('Resting ECG', ['Normal', 'LVH', 'ST']),
        'MaxHR': st.sidebar.slider('Maximum Heart Rate Achieved', 66, 202, 139),
        'ExerciseAngina': st.sidebar.selectbox('Exercise Induced Angina', ['N', 'Y']),
        'Oldpeak': st.sidebar.slider('ST Depression Induced by Exercise', -2.25, 3.75, 0.6),
        'ST_Slope': st.sidebar.selectbox('Slope of the Peak Exercise ST Segment', ['Up', 'Flat', 'Down'])
    }
    return inputs

def display_prediction(result):
    if result == 1:
        st.error("Prediction: High risk of heart disease.")
        st.markdown(health_advice(True))
    else:
        st.success("Prediction: Low risk of heart disease.")
        st.markdown(health_advice(False))

def health_advice(high_risk):
    if high_risk:
        return """
        ### Health Advice for High-Risk Individuals
        If you're at high risk of heart disease, it's crucial to consult with a healthcare provider for a detailed assessment and personalized advice. Consider adopting a heart-healthy lifestyle:
        - Maintain a balanced diet low in saturated fats, cholesterol, and sodium.
        - Engage in regular physical activity.
        - Avoid smoking and limit alcohol intake.
        - Monitor and manage your blood pressure, cholesterol levels, and diabetes.
        """
    else:
        return """
        ### Health Advice for Low-Risk Individuals
        To maintain a low risk of heart disease, continue practicing a healthy lifestyle:
        - Eat a diet rich in fruits, vegetables, and whole grains.
        - Stay active with regular exercise.
        - Avoid smoking and excessive alcohol consumption.
        - Keep up with regular health check-ups.
        """

def display_about_info():
    st.title('About Heart Disease Prediction')
    st.markdown("""
        ## Background and Problem Statement

        Heart disease is a major global health issue, leading to significant morbidity and mortality. Early detection and management can greatly improve outcomes for individuals at risk. This app aims to leverage machine learning to predict heart disease risk based on health and lifestyle factors, facilitating early intervention and awareness.
    """)

def display_footer():
    st.image("Ibrahim.jpg", width=200)
    st.markdown("Developed by Ibrahim Abdelnasar Yakout.")
    st.markdown("[LinkedIn](https://www.linkedin.com/in/ibrahim-abdelnasar/) | [Facebook](https://www.facebook.com/profile.php?id=100005030929252&mibextid=sCpJLy)")

if __name__ == '__main__':
    run()
