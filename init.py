# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
#import jsonify
#import requests
#import pickle
import numpy as np
import pandas as pd
#import sklearn
import joblib
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

model = joblib.load("Students_mark_predictor_model.pkl")

#df=model.DataFrame()

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])

def predict():
    #global df
    
    input_features = [float(x) for x in request.form.values()]
    value = np.array(input_features)
    
    if input_features[0] <0 or input_features[0] >24:
        return render_template('index.html', prediction_text='Please enter valid hours between 1 to 24')
    
    out_p = model.predict([value])[0][0].round(2)
    
    if out_p>100:
        output=100
    else:
        output=out_p
   # df=pd.concat([df,pd.DataFrame({'Study Hours':input_features,"Predicted Output":[output]})])
    #print(df)
    #df.to_csv("smp_data_from_app.csv")
    return render_template('index.html', Prediction_text = f" If you do study {input_features} hours per day, you can secure {output}% marks")

if __name__ == '__main__':
    #app.debug = True
    app.run()

