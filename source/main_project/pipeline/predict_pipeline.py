import sys
import pandas as pd
from source.commons import load_object
from source.exception import UserException
from source.logger import logging
from sklearn.preprocessing import LabelEncoder


class PredicPipeline:
    def __init__(self):
        pass
    
    logging.info('Preprocessing user input and making predictions')
    def predict(self,features):
        model_path = 'elements\model.pkl'
        preprocessor_path = 'elements\preprocessor.pkl'
        # loaeding objects
        model = load_object(model_path)
        preprocessor = load_object(preprocessor_path)
        data_scaled = preprocessor.transform(features)
        prediction = model.predict(data_scaled)
        
        return prediction
logging.info('This class is responsible for mapping all the inputs from html to flask')
class UserData:
    def __init__(self,
                 age,workclass,education,
                marital,occupation,relationship,race,
                gender):
        self.age = age
        self.work = workclass
        self.edu = education
        self.marital = marital
        self.occu = occupation
        self.relat = relationship
        self.race = race
        self.gender = gender
        
    # let's write a function that returns the user input as a numpy array
    def get_data_as_df(self):
        try:
            user_data = {
                'age':[self.age],
                "workclass":[self.work],
                "education":[self.edu],
                "marital-status":[self.marital],
                "occupation":[self.occu],
                "relationship":[self.relat],
                "race":[self.race],
                "gender":[self.gender]
            }
            return pd.DataFrame(user_data)
        except Exception as e:
            raise UserException(e,sys)
        