import streamlit as st


product_price= st.number_input("Enter the product price:")
discount_percentage= st.slider("Select discount percentage", 0, 50, 10)
st.button("Calculate Discounted Price", on_click=lambda: st.success(f"Discounted Price: {product_price - (product_price * discount_percentage / 100):.2f}"))
st.table({"Before": [product_price], "After": [discount_percentage]})