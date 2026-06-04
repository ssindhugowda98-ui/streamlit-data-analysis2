import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms(df):
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in num_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[col].dropna(), kde=True, ax=ax)
        ax.set_title(f"Distribution of {col}")
        st.pyplot(fig)


def plot_correlation_heatmap(df):
    num_df = df.select_dtypes(include=["int64", "float64"])

    if num_df.shape[1] > 1:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(num_df.corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)
    else:
        st.warning("Not enough numeric columns for correlation.")


def plot_boxplots(df):
    num_cols = df.select_dtypes(include=["int64", "float64"]).columns

    for col in num_cols:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[col], ax=ax)
        ax.set_title(f"Boxplot of {col}")
        st.pyplot(fig)
