import streamlit as st
import pandas as pd
import os

st.title("📰 Multi-Source AI News Sentiment Dashboard")

# Safe path (NO ERROR VERSION)
file_path = os.path.join("data", "processed", "multi_news_sentiment.csv")

# Load data
df = pd.read_csv(file_path)

# Show dataset
st.subheader("📊 News Data")
st.dataframe(df)

# Sentiment chart
st.subheader("📈 Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

# Source filter
st.subheader("🌍 Filter by Source")
source = st.selectbox("Choose source", df["source"].unique())

filtered_df = df[df["source"] == source]
st.dataframe(filtered_df)

# Search feature
st.subheader("🔍 Search News")
keyword = st.text_input("Enter keyword")

if keyword:
    result = df[df["headline"].str.contains(keyword, case=False, na=False)]
    st.write(result)