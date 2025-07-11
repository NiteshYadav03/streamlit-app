import streamlit as st
import pandas as pd
st.title("Welcome to Chapter 4 of Streamlit!")

st.title("Car Sales Data Analysis")

file = st.file_uploader("Upload a CSV file", type=["csv"])

if file:
    df=pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Data Statistics")
    st.write(df.describe())

if file:
    st.subheader("Data Visualization")
    st.bar_chart(df['Cars_Sold'] )
    st.line_chart(df['Cars_Sold'])
    st.area_chart(df['Cars_Sold'])
     