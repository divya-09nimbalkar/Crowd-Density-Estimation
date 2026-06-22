import streamlit as st
from estimator import estimate_density

st.title("👥 Crowd Density Estimation")

uploaded_file = st.file_uploader("Upload a crowd image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    with open("temp.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())
    result = estimate_density("temp.jpg")
    st.success(result)
