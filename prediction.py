import joblib

# Load Model
model = joblib.load('model/rdf_model.joblib')

# Load Encoder Fitur Target
target = joblib.load('model/encoder_Status.joblib')


def prediction(data):
    """Making prediction

    Args:
        data (Pandas DataFrame): Dataframe that contain all the preprocessed data

    Returns:
        str: Prediction result (Dropout, Enrolled, or Graduate)
    """
    result = model.predict(data)
    final_result = target.inverse_transform(result)[0]
    return final_result
