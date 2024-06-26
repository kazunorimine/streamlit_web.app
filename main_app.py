import streamlit as st
from PIL import Image

st.title('sapu-apuri')
st.caption('this is a movie for testst')

image = Image.open('./data/cooltext427033607653058.png')
st.image(image,width=200)