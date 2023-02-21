import pickle
import re

import joblib
import numpy as np
import pandas as pd


model = joblib.load('models/House_GBR_Feb15_2023.pkl')
labelEncoders = pickle.load(open('models/label_encoder_Feb15_2023.pkl', 'rb'))


def predict_input(house_input_val):

    # Send back our output

    numpy_input = np.array([convert_data(process_data(get_data(house_input_val)))])
    return model.predict(numpy_input)[0]


def get_data(house_input_val):
    neigh_info_CSV = pd.read_csv('data/neigh_info.csv')

    house_input_dict = house_input_val.to_dict()
    neigh_info_dict = \
        neigh_info_CSV[neigh_info_CSV['neigh_name'] == house_input_dict['community']].to_dict(orient='records')[0]
    house_input_dict.update(neigh_info_dict)
    return house_input_dict.round(2)


def process_data(house_dict):

    # Use label encoder to convert categorical data to numerical data

    house_dict["Type"] = labelEncoders["Type"].transform([house_dict["Type"]])
    house_dict["Sub-Type"] = labelEncoders["Sub-Type"].transform([house_dict["Sub-Type"]])
    house_dict["Style"] = labelEncoders["Style"].transform([house_dict["Style"]])
    house_dict["Construction"] = labelEncoders["Construction"].transform([house_dict["Construction"]])
    house_dict["Foundation"] = labelEncoders["Foundation"].transform([house_dict["Foundation"]])
    house_dict["male_to_fem"] = labelEncoders["male_to_fem"].transform([house_dict["male_to_fem"]])

    del house_dict['community']
    del house_dict['neigh_name']

    house_dict = {key: 0 if value == "" else value for key, value in
                  {key1: re.sub('[^a-zA-Z0-9.:/+ ]', '', str(value1)) for key1, value1 in house_dict.items()}.items()}

    return house_dict


def convert_data(house_processed_dict):
    # Convert house_processed_data to a list

    house_processed_data = [
        house_processed_dict["Bedrooms"],
        house_processed_dict["Bathrooms"],
        house_processed_dict["Square Footage"],
        house_processed_dict["Acres"],
        house_processed_dict["Year Built"],
        house_processed_dict["Type"],
        house_processed_dict["Sub-Type"],
        house_processed_dict["Style"],
        house_processed_dict["Is Waterfront"],
        house_processed_dict["Has Pool"],
        house_processed_dict["Fireplace"],
        house_processed_dict["# of Stories"],
        house_processed_dict["Has Basement"],
        house_processed_dict["Separate Entrance"],
        house_processed_dict["Construction"],
        house_processed_dict["Foundation"],
        house_processed_dict["RE / Bank Owned"],
        house_processed_dict["# of Garages"],
        house_processed_dict["House Fee"],
        house_processed_dict["Renovated"],
    ]

    house_processed_data.extend([i for i in list(house_processed_dict.values())[20:]])
    house_processed_data = [float(i) if house_processed_data.index(i) in (1, 3, 17, 18, 34) else int(i)
                            for i in house_processed_data]

    return house_processed_data
