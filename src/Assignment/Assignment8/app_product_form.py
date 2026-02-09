import streamlit as st


product_name = st.sidebar.text_input("Enter Product Name")
category =st.sidebar.selectbox("Select Category", ["Electronics", "Clothing", "Food"])
price= st.sidebar.number_input("Enter Price", min_value=0.0, step=0.01)
if st.sidebar.button("Add Product"):
    st.success("Product addedd successfully!")
    st.write(f"Product Name: {product_name}")
    st.write(f"Category: {category}")
    st.write(f"Price: {price}")