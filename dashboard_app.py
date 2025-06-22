import streamlit as st
import pandas as pd

# Load dataset
data = pd.read_csv("data/cleaned_customer_data.csv")

st.set_page_config(
    page_title="Customer Insights App",  # 🧠 Browser tab title
    page_icon="🛍️",                      # 🧿 Emoji or image as favicon
    layout="centered"                    # Can also be "wide"
)

# Title
st.title("Customer Insights & Future Purchase Prediction🛍️")

# Input for customer name only
customer_name = st.text_input("Enter Customer Name")

# Filter data
if customer_name:
    matched = data[data['Customer Name'].str.lower() == customer_name.strip().lower()]

    if not matched.empty:
        st.subheader("Customer Information")
        st.write(matched.T)  # Transpose for readability

        # Extract customer product categories from "Product Category"
        if 'Product Category' in matched.columns:
            customer_interests = matched['Product Category'].tolist()  # List of all product categories for the customer
            st.subheader("Predicted Future Interests")
            
            # Find the most frequent product category (for prediction)
            most_common_category = max(set(customer_interests), key=customer_interests.count)

            # Display prediction
            st.success(f"This customer might be interested in future products from: **{most_common_category}**")
        else:
            st.warning("No product category data available for this customer.")
    else:
        st.warning("No customer found with that name.")
