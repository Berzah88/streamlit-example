import streamlit as st
from datetime import date


START = "2017-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title("Stock Prediction App")
stocks = ("AAPL", "GOOG", "MSFT", "GME", "SASA")
selected_stocks = st.selectbox("Select Dataset", stocks)

n_years = st.slider("Years of prediction", 1, 4)
period = n_years * 365



