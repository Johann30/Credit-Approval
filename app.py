import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo RandomForestClassifier desde el archivo pkl
model = joblib.load('my_model.pkl')

# Titulo de la aplicación
st.title("CREDIT APPROVAL")

# Sección de entrada de características
st.subheader("Ingrese las Caracteristicas")

# Crea una entrada de texto para cada característica
gender = st.radio("Gender: ",('b', 'a'))
if gender == 'b':
    valor_gender = 1
else:
    valor_gender = 0

age = st.number_input("Age: ",  min_value=0.0)
debt = st.number_input("Debt: ",  min_value=0.0)
married = st.radio("Married: ",('u', 'y', 'l', 't'))
if married == 'u':
    valor_married = 0
elif married == 'y':
    valor_married = 1
elif married == 'l':
    valor_married = 2
else:
    valor_married = 3

bank_coustomer = st.radio("Bank Customer: ",('g', 'p', 'gg'))
if bank_coustomer == 'g':
    valor_bank_coustomer = 0
elif bank_coustomer == 'p':
    valor_bank_coustomer = 1
else:
    valor_bank_coustomer = 3

education_level = st.radio("Education Level: ",('c', 'd', 'cc', 'i', 'j', 
                                                    'k', 'm', 'r', 'q', 'w',
                                                    'x', 'e', 'aa', 'ff'))
if education_level == 'c':
    valor_education_level = 0
elif education_level == 'd':
    valor_education_level = 1
elif education_level == 'cc':
    valor_education_level = 2
elif education_level == 'i':
    valor_education_level = 3
elif education_level == 'j':
    valor_education_level = 4
elif education_level == 'k':
    valor_education_level = 5
elif education_level == 'm':
    valor_education_level = 6
elif education_level == 'r':
    valor_education_level = 7
elif education_level == 'q':
    valor_education_level = 8
elif education_level == 'w':
    valor_education_level = 9
elif education_level == 'x':
    valor_education_level = 10
elif education_level == 'e':
    valor_education_level = 11
elif education_level == 'aa':
    valor_education_level = 12
else:
    valor_education_level = 13

ethnicity= st.radio("Ethnicity: ",('v', 'h', 'bb', 'j', 'n', 'z', 
                                       'dd', 'ff','o'))
if ethnicity == 'v':
    valor_ethnicity = 0
elif ethnicity == 'h':
    valor_ethnicity = 1
elif ethnicity == 'bb':
    valor_ethnicity = 2
elif ethnicity == 'j':
    valor_ethnicity = 3
elif ethnicity == 'n':
    valor_ethnicity = 4
elif ethnicity == 'z':
    valor_ethnicity = 5
elif ethnicity == 'dd':
    valor_ethnicity = 6
elif ethnicity == 'ff':
    valor_ethnicity = 7
else:
    valor_ethnicity = 8

years_employed= st.number_input("Years Employed: ",  min_value=0.0)
prior_default = st.radio("Prior Default: ",('t', 'f'))
if prior_default == 't':
    valor_prior_default = 0
else:
    valor_prior_default = 1

employed = st.radio("Employed: ",('t', 'f'))
if employed == 't':
    valor_employed = 0
else:
    valor_employed = 1

credit_score= st.number_input("Credit Score: ",  min_value=0.0)
drivers_license = st.radio("Drivers License: ",('t', 'f'))
if drivers_license == 't':
    valor_drivers_license = 0
else:
    valor_drivers_license = 1

citizen = st.radio("Citizen: ",('g', 'p', 's'))
if citizen == 'g':
    valor_citizen = 0
elif citizen == 'p':
    valor_citizen = 1
else:
    valor_citizen = 3

zip_code= st.number_input("Zip Code: ",  min_value=0.0)
income= st.number_input("Income: ",  min_value=0.0)

# Botón de predicción
if st.button("Prediction"):
    data = pd.DataFrame({
        'A1': [valor_gender],
        'A2': [age],
        'A3': [debt],
        'A4': [valor_married],
        'A5': [valor_bank_coustomer],
        'A6': [valor_education_level],
        'A7': [valor_ethnicity],
        'A8': [years_employed],
        'A9': [valor_prior_default],
        'A10': [valor_employed ],
        'A11': [credit_score],
        'A12': [valor_drivers_license],
        'A13': [valor_citizen],
        'A14': [zip_code],
        'A15': [income],
    })

    # Realiza la predicción y muestra el resultado en la interfaz
    prediction = model.predict(data)
    if prediction[0] == 1:
        st.subheader("Su crédito fue: APROBADO")
    else:
        st.subheader("Su crédito fue: RECHAZADO")

st.write("<p style='text-align: center;'>By Johann Lozano Enriquez  a338834</p>", unsafe_allow_html=True)