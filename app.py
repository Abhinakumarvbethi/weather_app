import streamlit as st
import plotly.express as px
from weather_data import get_weather_data

# 🛠 MUST be first Streamlit command
st.set_page_config(page_title="Weather Explorer", layout="centered")

st.title("📈 Real-time Weather Data Explorer")
st.write("✅ App loaded successfully!")  # Debug line

st.write("Enter a location (latitude & longitude) to see the last 24 hours of temperature data.")

latitude = st.number_input("🌍 Latitude", value=28.61)
longitude = st.number_input("🌐 Longitude", value=77.21)

if st.button("Fetch Weather Data"):
    with st.spinner("Fetching data..."):
        try:
            df = get_weather_data(latitude, longitude)
            st.success("Data fetched successfully!")
            fig = px.line(df, x='Time', y='Temperature (°C)', title='Hourly Temperature')
            st.plotly_chart(fig)
        except Exception as e:
            st.error(f"Error: {e}")
