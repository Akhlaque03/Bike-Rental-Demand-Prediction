import streamlit as st

st.title("Test App")

x = st.slider("Slider", 0, 100, 50)

st.write("Value:", x)
