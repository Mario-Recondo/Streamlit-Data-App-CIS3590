import streamlit as st
import pandas as pd
import plotly.express as px
from api import apod_generator
import os

st.title("Water Quality Dashboard")
st.header("Internship Ready Software Development")
st.subheader("Mario Recondo")
st.divider()

df = pd.read_csv("biscayneBay_waterquality.csv")

tab1, tab2, tab3, tab4 = st.tabs(
    ["Descriptive Statistics",
     "2d Plots",
     "3d Plots",
     "Nasa Astronomy APOD"]
)

with tab1:
    st.info("Working on this")
    st.dataframe(df)
    st.caption("Raw Data")
    st.divider()
    st.dataframe(df.describe())
    st.caption("Descriptive Statistics")

with tab2:
    fig1 = px.line(df,
                   x="Time",
                   y="Temperature (c)")
    st.plotly_chart(fig1)

with tab3:
    fig3 = px.scatter_3d(df,
                         x="Longitude",
                         y="Latitude",
                         z="Total Water Column (m)",
                         color="Temperature (c)")
    fig3.update_scenes(zaxis_autorange="reversed")
    st.plotly_chart(fig3)

with tab4:
    st.header("Astronomy Picture of the Day")
    # TODO: Call a function that generates the APOD
    url = "https://api.nasa.gov/planetary/apod?api_key="
    response = apod_generator(url, os.getenv("NASA_API_KEY"))
    st.image(response["hdurl"])
    show_author = st.checkbox("Show Info")

    if show_author:
        st.caption(response["title"])
        st.caption(response["date"])
        st.caption(response["explanation"])

# 'copyright', 'date', 'explanation', 'hdurl', 'media_type', 'service_version', 'title', 'url']
