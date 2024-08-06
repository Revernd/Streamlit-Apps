import streamlit as st
import yfinance as y
import pandas as pd
import datetime as datetime

st.title("Welcome to stockviz!")
Ticker_symbol = st.text_input("Enter the Company ticker", value="AAPL")

ticker_data = y.Ticker(Ticker_symbol)

dc1, dc2 = st.columns(2)

with dc1:
    start_date = st.date_input("Start data", datetime.date(2019, 7, 6))

with dc2:
    end_date = st.date_input("End Date", datetime.date(2020, 7, 6))


ticker_df = ticker_data.history(period='1d', start=start_date, end=end_date)

#st.dataframe(ticker_df, use_container_width=True)
col1, col2 = st.columns(2)
with col1:
    st.write('''
Daily Close Price Chart
''')
    st.line_chart(ticker_df, y='Close')
with col2:
    st.write('''
Daily Volume Chart
''')
    st.line_chart(ticker_df, y='Volume')


