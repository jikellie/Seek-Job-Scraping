import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title= 'Survey Results')
st.header('Survey Results 2021')
st.subheader('Was the tutorial helpful')

### load the dataframe
df1 = pd.read_csv('IT-stream.csv')

st.dataframe(df1)

