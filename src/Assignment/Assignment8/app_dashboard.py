import streamlit as st

st.title("Simple Sales Dashboad")
months = st.selectbox("Select Month", ["January", "February", "March", "April"])
sales = {"January": 1200, "February": 1500, "March": 900, "April": 2000}

st.write(f" sales for month {months} is {sales[months]}")

st.bar_chart(list(sales.values()))
