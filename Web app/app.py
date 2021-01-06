from flask import Flask,render_template,jsonify, request

#import utils.PreProcessing
import pandas as pd
import numpy as np
import random
#import sklearn
#import pickle
import logging
#import sqlalchemy

#engine = sqlalchemy.create_engine('mysql+pymysql://root:Kvram97*@localhost:3306/application')

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

def zero_to_Yes(val):
    if val==0:
       return 'Yes'
    else:
       return 'No'


@app.route('/predict',methods=['POST'])
def upload_route_summary():
    if request.method == 'POST':
       result = request.files['file']
       result = pd.read_csv(result)
       #result.to_sql(
       #    name='application_train',
       #    con=engine,
       #    index=False,
       #    if_exists='append'
       #) 
       loan_ids = result['SK_ID_CURR']
       
       #Missing data handling
       missingval=result.columns[result.isnull().any()] 
        
       categorical_vars = [var for var in result.columns if result[var].isnull().mean()>0 and result[var].dtypes=='O']   
       numeric_vars = [e for e in missingval if e not in categorical_vars]

       from sklearn.impute import SimpleImputer 
       imputer = SimpleImputer(missing_values=np.nan, strategy='median')
       result[numeric_vars] = imputer.fit_transform(result[numeric_vars])
       
       result['NAME_TYPE_SUITE'].fillna('Unaccompanied',inplace=True)
       result['OCCUPATION_TYPE'].fillna('Laborers',inplace=True)
       result['FONDKAPREMONT_MODE'].fillna('reg oper account',inplace=True)
       result['HOUSETYPE_MODE'].fillna('block of flats',inplace=True)
       result['WALLSMATERIAL_MODE'].fillna('Panel',inplace=True)
       result['EMERGENCYSTATE_MODE'].fillna('No',inplace=True)
       logging.debug("Missing values are successfully imputed")
          
       #encoding
       from sklearn.preprocessing import LabelEncoder
       le = LabelEncoder()
       for col in result:
            if result[col].dtype == 'object':
                if len(list(result[col].unique())) <= 2:
                    le.fit(result[col])
                    result[col] = le.transform(result[col])
      
       # one-hot encoding of categorical variables
       result = pd.get_dummies(result)
       logging.debug("Values are encoded")

       #Feature engineering
       result['CREDIT_INCOME_PERCENT'] = result['AMT_CREDIT'] / result['AMT_INCOME_TOTAL']
       result['ANNUITY_INCOME_PERCENT'] = result['AMT_ANNUITY'] / result['AMT_INCOME_TOTAL']
       result['CREDIT_TERM'] = result['AMT_ANNUITY'] / result['AMT_CREDIT']
       result['DAYS_EMPLOYED_PERCENT'] = result['DAYS_EMPLOYED'] / result['DAYS_BIRTH'] 
                    
       #Feature selection
       selected_feat=['FLAG_OWN_REALTY', 'CNT_CHILDREN', 'AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY',
        'AMT_GOODS_PRICE', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'OWN_CAR_AGE', 
        'CNT_FAM_MEMBERS', 'REGION_RATING_CLIENT', 'EXT_SOURCE_1', 'EXT_SOURCE_2', 'EXT_SOURCE_3', 'APARTMENTS_AVG',
        'BASEMENTAREA_AVG', 'YEARS_BEGINEXPLUATATION_AVG', 'YEARS_BUILD_AVG', 'COMMONAREA_AVG', 'ENTRANCES_AVG', 
        'FLOORSMAX_AVG', 'FLOORSMIN_AVG', 'LANDAREA_AVG', 'LIVINGAPARTMENTS_AVG', 'LIVINGAREA_AVG', 'NONLIVINGAREA_AVG',
        'TOTALAREA_MODE', 'OBS_30_CNT_SOCIAL_CIRCLE', 'DEF_30_CNT_SOCIAL_CIRCLE', 'OBS_60_CNT_SOCIAL_CIRCLE',
        'DAYS_LAST_PHONE_CHANGE', 'AMT_REQ_CREDIT_BUREAU_MON', 'AMT_REQ_CREDIT_BUREAU_QRT', 'AMT_REQ_CREDIT_BUREAU_YEAR',
        'NAME_FAMILY_STATUS_Married', 'OCCUPATION_TYPE_Laborers', 'CREDIT_INCOME_PERCENT', 'ANNUITY_INCOME_PERCENT',
        'CREDIT_TERM', 'DAYS_EMPLOYED_PERCENT']
        
       result=result[selected_feat]               
    

    clf ="model_xgb_classifier.json"
    import xgboost as xgb

    loaded_model = xgb.XGBClassifier()
    booster = xgb.Booster()
    booster.load_model(clf)
    loaded_model._Booster = booster
    loaded_model._le = LabelEncoder().fit([0,1])

    prediction = loaded_model.predict(result)
    prediction_series = list(pd.Series(prediction))
    logging.debug("The model has been loaded...doing predictions now...")
    final_predictions = pd.DataFrame(list(zip(loan_ids, prediction_series)))
    final_predictions.columns = ['Loan ID', 'Prediction']
    final_predictions['Prediction'] = final_predictions['Prediction'].apply(zero_to_Yes)
    logging.debug("Prediction successful")

    rand_num = random.randint(10000,99999)
    filepath="static/Result/prediction"+str(rand_num)+".csv"
    final_predictions.to_csv(filepath,index=False)
    return jsonify(prediction=filepath)

@app.errorhandler(400)
def bad_request(error=None):
    message = {
            'status': 400,
            'message': 'Bad Request: ' + request.url + '--> Please check your data payload...',
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp

if __name__ == "__main__":
    app.run(debug=True)
