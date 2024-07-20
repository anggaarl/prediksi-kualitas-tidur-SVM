import pickle
import streamlit as st

# Load the trained model
model = pickle.load(open('sleep_quality_model.sav', 'rb'))

# Title
st.title('Prediksi Gangguan Tidur dengan Algoritma SVM')

# Input data
st.header('Masukkan Data Aktivitas Harian Anda')

gender = st.selectbox('Gender', options=[0, 1], format_func=lambda x: 'Male' if x == 0 else 'Female')

age = st.slider('Age', 27, 59, 31)

occupation = st.selectbox('Occupation', options=[
    'Nurse', 'Doctor', 'Engineer', 'Lawyer', 'Teacher', 'Accountant', 'Salesperson', 
    'Software Engineer', 'Scientist', 'Sales Representative', 'Manager'
])
occupation_mapping = {
    'Nurse': 0, 'Doctor': 1, 'Engineer': 2, 'Lawyer': 3, 'Teacher': 4,
    'Accountant': 5, 'Salesperson': 6, 'Software Engineer': 7, 'Scientist': 8,
    'Sales Representative': 9, 'Manager': 10
}
occupation = occupation_mapping[occupation]

sleep_duration = st.slider('Sleep Duration (hours)', min_value=5.8, max_value=8.5, value=7.0, step=0.1)
quality_of_sleep = st.slider('Quality of Sleep', 4, 9, 6) 
physical_activity_level = st.slider('Physical Activity Level', 30, 90, 50)
stress_level = st.slider('Stress Level', 3, 8, 5)

bmi_category = st.selectbox('BMI Category', options=[
    'Normal', 'Overweight', 'Normal Weight', 'Obese'
])
bmi_category_mapping = {
    'Normal': 0, 'Overweight': 1, 'Normal Weight': 2, 'Obese': 3
}
bmi_category = bmi_category_mapping[bmi_category]

# List of blood pressure values
blood_pressure = st.select_slider('Blood Pressure', options=[
    "115/75", "115/78", "117/76", "118/75", "118/76",
    "119/77", "120/80", "121/79", "122/80", "125/80",
    "125/82", "126/83", "128/84", "128/85", "129/84",
    "130/85", "130/86", "131/86", "132/87", "135/88",
    "135/90", "139/91", "140/90", "140/95", "142/92"
])

blood_pressure_mapping = {
    "115/75": 1, "115/78": 2, "117/76": 3, "118/75": 4, "118/76": 5,
    "119/77": 6, "120/80": 7, "121/79": 8, "122/80": 9, "125/80": 10,
    "125/82": 11, "126/83": 12, "128/84": 13, "128/85": 14, "129/84": 15,
    "130/85": 16, "130/86": 17, "131/86": 18, "132/87": 19, "135/88": 20,
    "135/90": 21, "139/91": 22, "140/90": 23, "140/95": 24, "142/92": 25
}
blood_pressure = blood_pressure_mapping[blood_pressure]

heart_rate = st.slider('Heart Rate', 65, 86, 70)
daily_steps = st.slider('Daily Steps', 3000, 10000, 5000, step=100)

# Make prediction
sleep_diagnose = ''
if st.button('Prediksi Gangguan Tidur'):
    sleep_predict = model.predict([[gender, age, occupation, sleep_duration, quality_of_sleep, physical_activity_level, stress_level, bmi_category, blood_pressure, heart_rate, daily_steps]])
    
    if sleep_predict == 0:
        sleep_diagnose = 'Anda Tidak Mengalami Masalah Tidur'
    elif sleep_predict == 1:
        sleep_diagnose = 'Anda Mengalami SLEEP APNEA'
    else: 
        sleep_diagnose = 'Anda Mengalami INSOMNIA'
        
    st.success(sleep_diagnose)
