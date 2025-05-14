import pandas as pd 
import numpy as np
from flask import Flask,request
import pickle

app=Flask(__name__)

pickle_in=open(r"C:\Users\ajcho\OneDrive\Desktop\full stack data science and AI\BY SELF\ML\ML self\Linear_housing_model.pkl","rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=['GET'])
def predict_note_authentication():

    '''
    ['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']
    '''
    input_cols=['MedInc','HouseAge','AveRooms','AveBedrms','Population','AveOccup','Latitude','Longitude']
    list1=[]
    for i in input_cols:
        val=request.args.get(i)
        list1.append(eval(val))

    prediction=classifier.predict([list1])

    print(prediction)
    return 'Hello The Answer is'+str(prediction)

@app.route('/predict_file',methods=['POST'])
def predict_note_file():
    df_test=pd.read_csv(request.files.get('file'))
    prediction=classifier.predict(df_test)
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000) 