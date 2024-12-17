import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pydeck as pdk


df = pd.read_csv('/usercode/dataset.csv')

st.header("My First Streamlit Application")