from unicodedata import name
#import folium
import pandas as pd
import numpy as np
import streamlit as st
#import leafmap.foliumap as leafmap
#from streamlit_folium import folium_static
def maps(lat, lon):
    df = pd.DataFrame(
     np.random.randn(1000, 2) / [50, 50] + [lat, lon],
     columns=['lat', 'lon'])

    st.map(df, zoom=7.2)

def maps1(df, lat, lon):
    filepath = df
    m = leafmap.Map(tiles="stamentoner")
    m.add_heatmap(
    filepath,
    latitude=lat,
    longitude=lon,
    value="pop_max",
    name="Heat map",
    radius=20,
    )
    m.to_streamlit(width=700, height=500)