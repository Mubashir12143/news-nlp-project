import streamlit as st
import pandas as pd

# Load dataset
df = pd.read_csv("data/processed/multi_news_sentiment.csv")

st.title("📰 Multi-Source News Sentiment AI System")

# Dataset preview
st.subheader("📊 News Dataset")
st.dataframe(df)

# Sentiment distribution
st.subheader("📈 Sentiment Distribution")
st.bar_chart(df["sentiment"].value_counts())

# Source filter
st.subheader("🌍 Filter by Source")
source = st.selectbox("Select News Source", df["source"].unique())

filtered_df = df[df["source"] == source]
st.dataframe(filtered_df)

# Search feature
st.subheader("🔍 Search News")
keyword = st.text_input("Enter keyword")

if keyword:
    result = df[df["headline"].str.contains(keyword, case=False)]
    st.write(result)