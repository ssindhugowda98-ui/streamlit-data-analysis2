import streamlit as st
from utils.data_loader import load_data
from utils.eda import show_basic_eda
from utils.visualizations import (
    plot_histograms,
    plot_correlation_heatmap,
    plot_boxplots
)

st.set_page_config(page_title="Data Dashboard", layout="wide")

st.title("📊 Streamlit Data Analysis Dashboard")

st.sidebar.header("Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)

    st.subheader("🔍 Preview Data")
    st.dataframe(df.head())

    st.subheader("📌 Basic EDA")
    show_basic_eda(df)

    st.subheader("📈 Histograms")
    plot_histograms(df)

    st.subheader("🔥 Correlation Heatmap")
    plot_correlation_heatmap(df)

    st.subheader("📦 Boxplots")
    plot_boxplots(df)

else:
    st.info("Upload a dataset to start analysis")
