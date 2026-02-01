
import streamlit as st
st.set_page_config(page_title="Diabetes Shield")
st.title("Diabetes Shield")
st.write("Simple risk calculator")
age = st.slider("Age", 18, 100, 35)
if st.button("Calculate"):
    risk = age / 100
    st.write(f"Risk: {risk:.1%}")
