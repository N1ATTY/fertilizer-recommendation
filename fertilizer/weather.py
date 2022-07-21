import streamlit as st
from config import weather_api_key
import json
import requests
import numpy as np
import pandas as pd
import datetime
from map import maps
#import leafmap.foliumap as leafmap
import plotly.express as px
from matplotlib.pyplot import axis
def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = weather_api_key
    base_url = "https://api.weatherapi.com/v1/current.json?"

    complete_url = base_url + "key=" + api_key + "&q=" + city_name + "&aqi=no"
    response = requests.get(complete_url)
    x = response.json()

    y = x["location"]
    city = y["name"]
    country = y["country"]
    time = y["localtime"]
    lat = y["lat"]
    lon = y["lon"]
        
    v = x["current"]
    condition = v["condition"]
    co = condition["text"]
    temperature = v["temp_c"]
    humidity = v["humidity"]
    cloud = v["cloud"]
    rainfall = v["precip_mm"]
    
    st.subheader(f"Country: {country}, ETH")
    st.subheader(f"City: {city}")
    st.subheader(f"Time: {time}")
    st.subheader(f"Condition: {co}")
    st.subheader(f"Rainfall: {rainfall} mm")
    col1, col2, col3 = st.columns(3)
    col1.metric(label="Temperature",value=temperature, delta="1.2 °C")
    col2.metric(label="Cloud Amount", value=cloud, delta="-8%")
    col3.metric("Humidity", value=humidity, delta="2%")
    maps(lat,lon)


def weather_fetch_10(city_name, d):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = weather_api_key
    base_url = "https://api.weatherapi.com/v1/current.json?"

    complete_url = base_url + "key=" + api_key + "&q=" + city_name + "&aqi=no"
    response = requests.get(complete_url)
    x = response.json()

    y = x["location"]
    city = y["name"]
    country = y["country"]
    time = y["localtime"]
    lat = y["lat"]
    lon = y["lon"]
    st.subheader(f"Country: {country}, ETH")
    st.subheader(f"City: {city}")
    
    d = str(d)
    st.write('The chosen Date is:', d)
    base_url = "https://api.open-meteo.com/v1/forecast?"
    lat = f"latitude={lat}"
    long = f"longitude={lon}"
    complete_url = base_url + lat + "&" + long + "&" + "hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,soil_temperature_54cm,soil_moisture_9_27cm"
    response = requests.get(complete_url)
    x = response.json()
    elevation = x["elevation"]
    hour = x["hourly"]
    tm = hour["time"]
    temp = hour["temperature_2m"]
    humidity = hour["relativehumidity_2m"]
    rainfall = hour["precipitation"]
    cover = hour["cloudcover"]
    est = hour["soil_temperature_54cm"]
    soilwetness = hour["soil_moisture_9_27cm"]
    filepath = complete_url
    #m = leafmap.Map(tiles="stamentoner")
    #m.add_heatmap(
    #filepath,
    #latitude= lat,
    #longitude= lon,
    #name="Heat map",
    #radius=20,)
    #m.to_streamlit(width=700, height=500)
   
    df = pd.DataFrame(list(zip(tm,temp,humidity,rainfall,cover,est,soilwetness)),
    columns =['Time', 'Temperature in C', 'Humidity','Rainfall','Cloud Amount','Earth Skin Temperature','Soil Moisture'])
    now1 = datetime.datetime.today()
    now = datetime.datetime.today().strftime("%Y-%m-%d")
    tom1= now1 + datetime.timedelta(days=1)
    tom1 = tom1.strftime("%Y-%m-%d")
    tom2= now1 + datetime.timedelta(days=2)
    tom2 = tom2.strftime("%Y-%m-%d")
    tom3= now1 + datetime.timedelta(days=3)
    tom3 = tom3.strftime("%Y-%m-%d")
    tom4= now1 + datetime.timedelta(days=4)
    tom4 = tom4.strftime("%Y-%m-%d")
    tom5= now1 + datetime.timedelta(days=5)
    tom5 = tom5.strftime("%Y-%m-%d")
    tom6= now1 + datetime.timedelta(days=1)
    tom6 = tom6.strftime("%Y-%m-%d")
    if d==now:
        df=df.iloc[0:24]
        st.table(df)
        #t= df.iloc[5,0]
        g = df.iloc[:,1::]
        st.line_chart(data=g, width=0, height=0, use_container_width=True)
    elif d==tom1:
        df=df.iloc[24:48]
        st.table(df)
        g = df.iloc[:,1::]
        st.line_chart(data=g, width=0, height=0, use_container_width=True)
    elif d==tom2:
        df=df.iloc[48:72]
        st.table(df)
        g = df.iloc[:,1::]
        st.line_chart(data=g, width=0, height=0, use_container_width=True)
    elif d==tom3:
        df=df.iloc[72:96]
        st.table(df)       
        g = df.iloc[:,1::]
        st.line_chart(data=g, width=0, height=0, use_container_width=True)
    elif d== tom4:
        df=df.iloc[96:120]
        st.table(df)
        g = df.iloc[:,1::]
        st.line_chart(data=g, width=0, height=0, use_container_width=True)
    elif d== tom5:
        df=df.iloc[120:144]
        st.table(df)
        g = df.iloc[:,1::]
        st.line_chart(data=g, width=0, height=0, use_container_width=True)
    elif d== tom6:
        df=df.iloc[144:168]
        st.table(df)
        g = df.iloc[:,1::]
        st.line_chart(data=g, width=0, height=0, use_container_width=True)
    
