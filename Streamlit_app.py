import streamlit as st
import sklearn 
import pandas as pd 
import numpy as np
import pickle

model = pickle.load(open('model.sav','rb'))


st.title('Credit Card Fraud Detection ')
st.sidebar.header('Please select the information')

#function for input
def user_report():
    V17 = st.sidebar.number_input('V17',min_value=-25.16,max_value=9.25,step=0.005)
    V14 = st.sidebar.number_input('V14',min_value=-19.21,max_value=10.52,step=0.005)
    V12 = st.sidebar.number_input('V12',-18.68,7.84,0.005)
    V10 = st.sidebar.number_input('V10',-24.58,23.74,0.005)
    V16 = st.sidebar.number_input('V16',min_value=-14.12,max_value=17.31,step=0.005) 
    V3 = st.sidebar.number_input('V3',-48.32,9.38,0.005)
    V7 = st.sidebar.number_input('V7',-43.55,120.58,0.005)
    V11 = st.sidebar.number_input('V11',-4.79,12.01,0.005)
    V4 = st.sidebar.number_input('V4',min_value=-5.68,max_value=16.87,step=0.005)
    V18 = st.sidebar.number_input('V18',min_value=-9.49,max_value=5.04,step=0.005) 
 


    user_report_data={
        'V17': V17,
        'V14': V14,
        'V12': V12,
        'V10': V10,
        'V16': V16,
        'V3': V3,
        'V7': V7,
        'V11': V11,
        'V4': V4,
        'V18': V18,

    }
    report_data = pd.DataFrame(user_report_data,index=[0])
    return report_data





user_data = user_report()
st.header('Please check the information provided by you')
st.write(user_data)

## fares Prediction
if (st.button("Click to detect fraud or Not")):
    fraud = model.predict(user_data)

    if(fraud == 0):
        st.success("fraud has not happened")
    elif(fraud == 1):
        st.error("fraud has happened")