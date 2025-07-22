import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="Smart Finance Hub", layout="wide")
st.title("📊 Smart Finance Hub Dashboard")

section = st.sidebar.radio("Choose Section", [
    "📉 Crash Analysis", "💰 Mutual Fund Plan"
])

def load_data():
    stocks = ['TCS.NS', 'INFY.NS', 'RELIANCE.NS', 'HDFCBANK.NS']
    return yf.download(stocks, start='2010-01-01')['Adj Close']

if section == "📉 Crash Analysis":
    st.header("📉 Crash Analysis of NIFTY")
    nifty = yf.download("^NSEI", start="2006-01-01")
    fig, ax = plt.subplots(figsize=(12,5))
    ax.plot(nifty['Close'])
    ax.axvspan(pd.Timestamp("2008-09-01"), pd.Timestamp("2009-06-01"), color='red', alpha=0.3)
    ax.axvspan(pd.Timestamp("2020-03-01"), pd.Timestamp("2020-06-01"), color='orange', alpha=0.3)
    ax.set_title("NIFTY Crashes Highlighted")
    st.pyplot(fig)

elif section == "💰 Mutual Fund Plan":
    st.header("💰 Get Mutual Fund Recommendations")
    risk = st.selectbox("Select Risk Level", ['Low', 'High', 'Very High'])
    funds = pd.DataFrame({
        'Fund': ['HDFC Equity', 'SBI Small Cap', 'ICICI Liquid'],
        'Category': ['Equity', 'Small Cap', 'Liquid'],
        'Risk': ['High', 'Very High', 'Low'],
        '5Y_Return': [0.15, 0.22, 0.06]
    })
    match = funds[funds['Risk'].str.contains(risk, case=False)]
    st.dataframe(match)
