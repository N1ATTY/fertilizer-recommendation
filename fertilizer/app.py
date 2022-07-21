#from sklearn.ensemble import RandomForestClassifier
from urllib import response
from requests import options
import streamlit as st
import pickle
import numpy as np
import pandas as pd
from weather import  weather_fetch
from fertilizer import Nlow, KHigh, PHigh,NHigh, Klow,Plow
def fert_recommend():
    df = pd.read_csv('fertilizer.csv')
    st.title("Fertelizer Suggestion")
    st.subheader("here you can get Fertelizer Suggestion based on the soil content")
    col1,col2,col3=st.columns(3)
    with col1:
        N = st.number_input("Enter the Nitrogen level", min_value=0, max_value=110, value=25, step=1, help="Nitrogen Level should be in the given range")
    with col2:
        P = st.number_input("Enter the Phosphoures Level", min_value=0, max_value=110, value=90, step=1, help="Pospherus Level should be in the given range")
    with col3:
        K = st.number_input("Enter Potassium Level", min_value=0, max_value=110, value=25, step=1, help="potassium Level should be within the given range")
    df1 = pd.read_csv("distnict-data.csv")
    city = df1['City'].unique().tolist()
    city_name = st.selectbox(label = "Select city", options=city)
    crop_op = df['Crop'].unique().tolist()
    crop_name = st.selectbox(label = "What crop do you want to grow", options=crop_op)
    suggest = st.button('Suggest')
    if suggest:
        nf = df[df['Crop'] == crop_name]['N'].iloc[0]
        pf = df[df['Crop'] == crop_name]['P'].iloc[0]
        kf = df[df['Crop'] == crop_name]['K'].iloc[0]
        n = nf - N
        p = pf - P
        k = kf - K
        temp = {n,p,k}
        max_value= max(temp)
      
        if max_value==n:
            if n < 0:
                key = NHigh
            else:
                key = Nlow
        elif max_value==p:
            if p < 0:
                key = PHigh
            else:
                key = Plow
        else:
            if k < 0:
                key = KHigh
            else:
                key = Klow

        response =key
        
        return st.markdown(f'''{response}'''), weather_fetch(city_name)

fert_recommend()