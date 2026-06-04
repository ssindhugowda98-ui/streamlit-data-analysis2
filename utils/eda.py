import streamlit as st

def show_basic_eda(df):
    col1, col2, col3 = st.columns(3)

    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    st.write("### Data Types")
    st.write(df.dtypes)

    st.write("### Summary Statistics")
    st.write(df.describe())
