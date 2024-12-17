import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk


df = pd.read_csv('/usercode/dataset.csv')

st.header("My First Streamlit Application")

#Set page configuration
st.set_page_config(layout = "wide", page_title = "Streamlit Data-centric App", page_icon = ":taxi:")


#Provide a list of functionalities to select from
message = """
        __Select a functionality from the list below__
        """
with st.sidebar:
    st.markdown(message)
    page = st.selectbox('Select:',
        ['View Data Using Dropdowns',
        'Visualize Data on a Map',
        '2D Charts and Histograms', 
        '3D Charts and Histograms']) 