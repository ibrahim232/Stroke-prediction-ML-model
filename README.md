
<h1 style="text-align:center;">Stroke Prediction</h1>
<p align="center">
  <img src="https://images.ctfassets.net/yixw23k2v6vo/3WpTUk6z52hVzvtTsPaWT/ef7c4d18a15e79f3d3533355ae380411/iStock-1168179082.jpg" width="400" height="300">
</p>

# Context

According to the World Health Organization (WHO), stroke is the 2nd leading cause of death globally, responsible for approximately 11% of total deaths. This dataset is used to predict whether a patient is likely to get a stroke based on the input parameters like gender, age, various diseases, and smoking status. Each row in the data provides relevant information about the patient.

## Attribute Information

1. **id**: Unique identifier.
2. **gender**: Gender of the patient, can be "Male", "Female", or "Other".
3. **age**: Age of the patient.
4. **hypertension**: Indicates if the patient has hypertension, where 0 means the patient doesn't have hypertension, and 1 means the patient has hypertension.
5. **heart_disease**: Indicates if the patient has any heart diseases, where 0 means the patient doesn't have any heart diseases, and 1 means the patient has a heart disease.
6. **ever_married**: Indicates if the patient has ever been married, where "No" means the patient has never been married, and "Yes" means the patient has been married.
7. **work_type**: Type of work the patient is engaged in, which can be "children", "Govt_job", "Never_worked", "Private", or "Self-employed".
8. **Residence_type**: Type of residence of the patient, which can be "Rural" or "Urban".
9. **avg_glucose_level**: Average glucose level in the blood.
10. **bmi**: Body mass index.
11. **smoking_status**: Smoking status of the patient, which can be "formerly smoked", "never smoked", "smokes", or "Unknown" (if the information is unavailable for the patient).
12. **stroke**: Indicates if the patient had a stroke, where 1 means the patient had a stroke, and 0 means the patient did not have a stroke.


1. [Importing Libraries](#importing-libraries)
2. [Data Overview](#data-overview)
3. [Data Cleaning & Preprocessing](#data-cleaning-and-preprocessing)
4. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
    - [Univariate Analysis](#univariate-analysis)
    - [Bivariate Analysis](#bivariate-analysis)
    - [Multivariate Analysis](#multivariate-analysis)
5. [Data Encoding](#data-encoding)
6. [Data Scaling](#data-scaling)
7. [Data Modeling](#data-modeling)
8. [Model Evaluation](#model-evaluation)
9. [Pipeline](#pipeline)
10. [Deployment](#deployment)
