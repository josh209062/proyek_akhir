import pandas as pd
import numpy as np
import joblib

# Load Encoder
encoder_daytime = joblib.load(
    'model/encoder_Daytime_evening_attendance.joblib')
encoder_displaced = joblib.load('model/encoder_Displaced.joblib')
encoder_scholarship = joblib.load('model/encoder_Scholarship_holder.joblib')
encoder_tuition_fee = joblib.load(
    'model/encoder_Tuition_fees_up_to_date.joblib')

# Load Scaler
scaler_admission_grade = joblib.load('model/scaler_Admission_grade.joblib')
scaler_application_order = joblib.load('model/scaler_Application_order.joblib')
scaler_cu_1_approved = joblib.load(
    'model/scaler_Curricular_units_1st_sem_approved.joblib')
scaler_cu_1_enrolled = joblib.load(
    'model/scaler_Curricular_units_1st_sem_enrolled.joblib')
scaler_cu_1_grade = joblib.load(
    'model/scaler_Curricular_units_1st_sem_grade.joblib')
scaler_cu_2_approved = joblib.load(
    'model/scaler_Curricular_units_2nd_sem_approved.joblib')
scaler_cu_2_credited = joblib.load(
    'model/scaler_Curricular_units_2nd_sem_credited.joblib')
scaler_cu_2_enrolled = joblib.load(
    'model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
scaler_cu_2_evaluations = joblib.load(
    'model/scaler_Curricular_units_2nd_sem_evaluations.joblib')
scaler_cu_2_grade = joblib.load(
    'model/scaler_Curricular_units_2nd_sem_grade.joblib')
scaler_previous_qual = joblib.load(
    'model/scaler_Previous_qualification_grade.joblib')

# Load Model
model = joblib.load('model/rdf_model.joblib')

# variabel untuk fitur numerik dan kategori
numeric_columns = [
    'Curricular_units_2nd_sem_approved',
    'Curricular_units_2nd_sem_grade',
    'Curricular_units_1st_sem_approved',
    'Curricular_units_1st_sem_grade',
    'Curricular_units_2nd_sem_enrolled',
    'Curricular_units_1st_sem_enrolled',
    'Admission_grade',
    'Previous_qualification_grade',
    'Curricular_units_2nd_sem_evaluations',
    'Application_order',
    'Curricular_units_2nd_sem_credited'
]

category_columns = [
    'Tuition_fees_up_to_date',
    'Scholarship_holder',
    'Displaced',
    'Daytime_evening_attendance',
]

# membuat fungsi untuk data preprocessing


def data_preprocessing(data):
    """Preprocessing data

    Args:
        data (Pandas DataFrame): Dataframe that contain all the data to make prediction 

    return:
        Pandas DataFrame: Dataframe that contain all the preprocessed data
    """
    data = data.copy()
    df = pd.DataFrame()

    df['Curricular_units_2nd_sem_approved'] = scaler_cu_2_approved.transform(
        np.asarray(data['Curricular_units_2nd_sem_approved']).reshape(-1, 1))[0]
    df['Curricular_units_2nd_sem_grade'] = scaler_cu_2_grade.transform(
        np.asarray(data['Curricular_units_2nd_sem_grade']).reshape(-1, 1))[0]
    df['Curricular_units_1st_sem_approved'] = scaler_cu_1_approved.transform(
        np.asarray(data['Curricular_units_1st_sem_approved']).reshape(-1, 1))[0]
    df['Curricular_units_1st_sem_grade'] = scaler_cu_1_grade.transform(
        np.asarray(data['Curricular_units_1st_sem_grade']).reshape(-1, 1))[0]
    df['Tuition_fees_up_to_date'] = encoder_tuition_fee.transform(
        data['Tuition_fees_up_to_date'])[0]
    df['Scholarship_holder'] = encoder_scholarship.transform(
        data['Scholarship_holder'])[0]
    df['Curricular_units_2nd_sem_enrolled'] = scaler_cu_2_enrolled.transform(
        np.asarray(data['Curricular_units_2nd_sem_enrolled']).reshape(-1, 1))[0]
    df['Curricular_units_1st_sem_enrolled'] = scaler_cu_1_enrolled.transform(
        np.asarray(data['Curricular_units_1st_sem_enrolled']).reshape(-1, 1))[0]
    df['Admission_grade'] = scaler_admission_grade.transform(
        np.asarray(data['Admission_grade']).reshape(-1, 1))[0]
    df['Displaced'] = encoder_displaced.transform(data['Displaced'])[0]
    df['Previous_qualification_grade'] = scaler_previous_qual.transform(
        np.asarray(data['Previous_qualification_grade']).reshape(-1, 1))[0]
    df['Curricular_units_2nd_sem_evaluations'] = scaler_cu_2_evaluations.transform(
        np.asarray(data['Curricular_units_2nd_sem_evaluations']).reshape(-1, 1))[0]
    df['Application_order'] = scaler_application_order.transform(
        np.asarray(data['Application_order']).reshape(-1, 1))[0]
    df['Daytime_evening_attendance'] = encoder_daytime.transform(
        data['Daytime_evening_attendance'])[0]
    df['Curricular_units_2nd_sem_credited'] = scaler_cu_2_credited.transform(
        np.asarray(data['Curricular_units_2nd_sem_credited']).reshape(-1, 1))[0]

    return df
