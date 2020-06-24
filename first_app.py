import streamlit as st
import pandas as pd
import numpy as np

st.title("Our first streamlit app")

st.image("img.jpg", caption="sample image", width=400)

data = pd.read_csv("features.csv")

st.markdown("## This is the text using markdown function.")

"## This is the text I typed in quotation marks."

st.write("Text can also be written using the write function.")

st.sidebar.header("Features")
st.sidebar.markdown("Drag the sliders")

row = st.sidebar.slider("Display Records:",0,100,50)


if st.checkbox("Show original dataset"):
    st.write(data.iloc[0:row])    

