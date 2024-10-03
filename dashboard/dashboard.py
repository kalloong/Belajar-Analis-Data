import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned datasets
shipping_data_cleaned_df = pd.read_csv("shipping_data_cleaned.csv")
product_reviews_cleaned_df = pd.read_csv("product_reviews.csv")
rfm_satisfaction_df = pd.read_csv("rfm_satisfaction.csv")

# Set up Streamlit layout
st.set_page_config(page_title="E-Commerce Customer Satisfaction Dashboard", layout="wide")

# Sidebar for user interaction
st.sidebar.title("Filters")
category_filter = st.sidebar.multiselect(
    'Select Product Categories:',
    product_reviews_cleaned_df['product_category_name_english'].unique(),
    default=product_reviews_cleaned_df['product_category_name_english'].unique()
)

# Main dashboard
st.title("E-Commerce Customer Satisfaction Dashboard")
st.write("This dashboard analyzes customer satisfaction based on shipping times, product categories, and customer RFM segmentation.")

# Section 1: Shipping Time vs Customer Satisfaction
st.header("1. Shipping Time and Customer Satisfaction")

# Filter the dataset if needed
filtered_shipping_data = shipping_data_cleaned_df[shipping_data_cleaned_df['shipping_time'] >= 0]

# Visualization: Shipping Time vs Review Score
fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='shipping_time', y='review_score', data=filtered_shipping_data, ax=ax)
ax.set_title('Shipping Time vs Customer Satisfaction (Review Score)')
ax.set_xlabel('Shipping Time (Days)')
ax.set_ylabel('Review Score')
st.pyplot(fig)

# Conclusion 1
st.markdown("""
**Conclusion 1:**
- Faster Shipping Times Lead to Higher Customer Satisfaction.
- Delayed shipments result in a significant increase in negative reviews.
""")

# Section 2: Product Categories and Positive Reviews
st.header("2. Product Categories and Positive Reviews")

# Filter by selected categories
filtered_reviews = product_reviews_cleaned_df[product_reviews_cleaned_df['product_category_name_english'].isin(category_filter)]

# Visualization: Average Review Score by Category
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='review_score', y='product_category_name_english', data=filtered_reviews, palette='Blues_d', ax=ax)
ax.set_title('Product Categories with Positive Reviews')
ax.set_xlabel('Average Review Score')
ax.set_ylabel('Product Category')
st.pyplot(fig)

# Conclusion 2
st.markdown("""
**Conclusion 2:**
- Product categories with better product descriptions receive higher customer reviews.
""")

# Section 3: RFM Analysis
st.header("3. Customer Satisfaction by RFM Segment")

# Visualization: RFM Segment vs Review Score
fig, ax = plt.subplots(figsize=(12, 6))
sns.barplot(x='RFM_Score', y='review_score', data=rfm_satisfaction_df, palette='coolwarm', ax=ax)
ax.set_title('Customer Satisfaction by RFM Segment')
ax.set_xlabel('RFM Segment')
ax.set_ylabel('Average Review Score')
st.pyplot(fig)

# Conclusion 3
st.markdown("""
**Conclusion 3:**
- Customers with high RFM scores (Recency, Frequency, Monetary) are more likely to give positive reviews.
- At-risk and lost customers tend to leave negative reviews, showing lower satisfaction.
""")