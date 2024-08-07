import numpy as np
import pickle
import streamlit as st


#loading the saved model
loaded_model=pickle.load(open('trained_model.sav','rb'))#rb=read byte(bit,binary)

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
    st.title('Mercy Olokpo Diabetes Prediction Web App')
    
    
    # getting the input data from the user
    

    Pregnancies, Glucose, BloodPressure = st.columns(3)
    Pregnancies.text_input('Number of Pregnancies')
    Glucose.text_input('Glucose Level')
    BloodPressure.text_input('Blood Pressure Value')
    SkinThickness, Insulin, BMI = st.columns(3)
    SkinThickness.text_input('Skin Thickness Level')
    Insulin.text_input('Insulin Level')
    BMI.text_input('BMI Value')
    DiabetesPedigreeFunction, Age = st.columns(2)
    DiabetesPedigreeFunction.text_input('Diabetes Pedigree Function Value')
    Age.text_input('Age of the Person')
    
    
    
    # code for prediction
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies,  Glucose,  BloodPressure,SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age ])
        
        
        
    st.success(diagnosis)
    
    
   
    
   
if __name__ == '__main__':
    main()
    
