import streamlit as st

st.title("Streamlit App")
st.write("Hello, Streamlit!")
st.title("My First Streamlit App")
st.header("Welcome to Streamlit")
st.subheader("This is a subheader")
st.text("This is some text in Streamlit.")
st.markdown("This is **Markdown** text in Streamlit.")
slider=st.slider("Select a number", 0, 100, 50)
st.write(f"You selected: {slider}")

agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("Thank you for agreeing!")

options = st.multiselect("Select your favorite fruits", ["Apple", "Banana", "Cherry", "Date"])
st.write(f"You selected: {options}")


filess=st.file_uploader("Upload a file", type=["csv", "txt"])

if filess is not None:
   filess.getvalue()
   st.write("File "+filess.name+" uploaded successfully!")
   st.write(filess.getvalue())