import streamlit as st
from PIL import Image

st.header("Image Gallery")

st.info("butterfly")
img=Image.open("butterfly.png")
st.image(img,width=300)

st.info("bike")
img2=Image.open("bike.png")
st.image(img2,width=400)