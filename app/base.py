import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path

st.set_page_config(layout="wide", page_title="Solar Country Comparison")

# Use the correct relative paths
@st.cache_data
def load_data():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    
    df_benin = pd.read_csv(data_dir / "benin-malanville_clean.csv", parse_dates=["Timestamp"])
    df_sierra = pd.read_csv(data_dir / "sierraleone-bumbuna_clean.csv", parse_dates=["Timestamp"])
    df_togo = pd.read_csv(data_dir / "togo-dapaong_qc_clean.csv", parse_dates=["Timestamp"])
    
    df_benin["Country"] = "Benin"
    df_sierra["Country"] = "Sierra Leone"
    df_togo["Country"] = "Togo"
    
    return pd.concat([df_benin, df_sierra, df_togo])

df = load_data()

countries = st.multiselect("Select Countries", options=df["Country"].unique(), default=df["Country"].unique())
metric = st.selectbox("Select Metric", ["GHI", "DNI", "DHI"])

filtered_df = df[df["Country"].isin(countries)]

st.header(f"{metric} Comparison Across Selected Countries")

fig, ax = plt.subplots()
sns.boxplot(data=filtered_df, x="Country", y=metric, ax=ax, palette="Set3")
st.pyplot(fig)

st.subheader("Average GHI by Country")
avg_ghi = filtered_df.groupby("Country")["GHI"].mean().sort_values()
st.bar_chart(avg_ghi)
