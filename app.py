import streamlit as st
import pandas as pd
import joblib

from data_preprocesssing import data_preprocessing, encoder_daytime, encoder_displaced, encoder_scholarship, encoder_tuition_fee
from data_preprocesssing import scaler_admission_grade, scaler_application_order, scaler_cu_1_approved, scaler_cu_1_enrolled, scaler_cu_1_grade, scaler_cu_2_approved, scaler_cu_2_credited, scaler_cu_2_enrolled, scaler_cu_2_evaluations, scaler_cu_2_grade, scaler_previous_qual

from prediction import prediction

st.set_page_config(
    page_title="Students Performance Prediction", layout="centered")
st.title('Students Performance Prediction at Jaya-Jaya Institute')
st.write("\n\nInput the student data below.")
st.write('\n\n')

data = pd.DataFrame()

col1, col2, col3, col4 = st.columns(4)

with col1:
    Tuition_fees_up_to_date = st.selectbox(
        label='Tuition Fees Update', options=encoder_tuition_fee.classes_, index=1)
    data['Tuition_fees_up_to_date'] = [Tuition_fees_up_to_date]

with col2:
    Scholarship_holder = st.selectbox(
        label='Scholarship Holder', options=encoder_scholarship.classes_, index=1)
    data['Scholarship_holder'] = [Scholarship_holder]

with col3:
    Displaced = st.selectbox(
        label='Displaced', options=encoder_displaced.classes_, index=1)
    data['Displaced'] = [Displaced]

with col4:
    Daytime_evening_attendance = st.selectbox(
        label='Attendance', options=encoder_daytime.classes_, index=1)
    data['Daytime_evening_attendance'] = [Daytime_evening_attendance]


col1, col2, col3 = st.columns(3)

with col1:
    Admission_grade = float(st.number_input(
        label='Admission Grade', min_value=95, max_value=190, value=100))
    data["Admission_grade"] = Admission_grade

with col2:
    Application_order = int(st.number_input(
        label='Application Order', min_value=0, max_value=9, value=1))
    data["Application_order"] = Application_order

with col3:
    Previous_qualification_grade = float(st.number_input(
        label='Previous Qualification Grade', min_value=95, max_value=190, value=100))
    data["Previous_qualification_grade"] = Previous_qualification_grade

st.write('\n')
st.write('## **Cirricular Units of 1nd Semester**')

col1, col2, col3 = st.columns(3)

with col1:
    Curricular_units_1st_sem_approved = int(st.number_input(
        label='Approved', min_value=0, max_value=26, value=10))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col2:
    Curricular_units_1st_sem_grade = float(st.number_input(
        label='Grade', min_value=0, max_value=19, value=10))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade

with col3:
    Curricular_units_1st_sem_enrolled = int(st.number_input(
        label='Enrolled', min_value=0, max_value=26, value=10))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled

st.write('\n')
st.write('## **Cirricular Units of 2nd Semester**')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    Curricular_units_2nd_sem_approved = int(st.number_input(
        label='Approved ', min_value=0, max_value=26, value=10))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col2:
    Curricular_units_2nd_sem_grade = float(st.number_input(
        label='Grade ', min_value=0, max_value=19, value=10))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with col3:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(
        label='Enrolled ', min_value=0, max_value=26, value=10))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled

with col4:
    Curricular_units_2nd_sem_evaluations = int(st.number_input(
        label='Evaluations ', min_value=0, max_value=35, value=10))
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations

with col5:
    Curricular_units_2nd_sem_credited = int(st.number_input(
        label='Credited ', min_value=0, max_value=20, value=10))
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited


with st.expander('View raw data'):
    st.dataframe(data=data, width=800, height=10)


if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander('View the Preprocessed Data'):
        st.dataframe(data=new_data, width=800, height=10)
    st.write(f'The student predicted as **{prediction(new_data)}**')
