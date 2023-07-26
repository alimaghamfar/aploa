import streamlit as st
import cv2
import numpy as np

st.write("Upload the Image of Person to Register them in DataBase")

uploaded_file = st.file_uploader("Upload image", type=['jpeg', 'png', 'jpg', 'webp'])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    st.image(image, channels="BGR")