# -*- coding: utf-8 -*-
"""
Created on Thu May 30 10:21:15 2024

@author: user
"""

import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model=pickle.load(open('C:/Users/user/Desktop/Diabetes Prediction Model/trained_model.sav','rb'))#rb=read byte(bit,binary)

#creating a function for pridiction

def diabetes_prediction(input_data):
    
    

    #Changing the input_data to numpy array
    data=np.array(input_data)

    #Reshaping the array as we are predicting for one instance
    input_data_reshaped=data.reshape (1, -1)

    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction==0:
        return'this person is not Diabetic'
    else:
        return'this person is Diabetic'
        
        
        
def main():
    
    # giving a title
    st.title('Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness Level')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI Value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    Age = st.text_input('Age of the Person')
    
    
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,  Glucose,  BloodPressure,SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])
        
        
        
    st.success(diagnosis)
    
    
   
    
   
if __name__ == '__main__':
    main()
    
