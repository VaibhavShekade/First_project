import streamlit as st
from matplotlib import image
import pandas as pd
import plotly.express as px
import os


FILE_DIR = os.path.dirname(os.path.abspath(__file__))

PARENT_DIR = os.path.join(FILE_DIR, os.pardir)

dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Rice.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "rice production across different countries from 1961 to 2021.csv")

st.title("Dashboard - Rice production")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

species = st.selectbox("Select the country:", df['Area'].unique())

col1, col2 = st.columns(2)

fig_1 = px.histogram(df[df['Area'] == species], x="Value")
col1.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Area'] == species], y="Value")
col2.plotly_chart(fig_2, use_container_width=True)