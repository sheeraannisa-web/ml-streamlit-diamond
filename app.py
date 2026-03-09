import streamlit as st
import pickle
import numpy as np
import pandas as pd


with open("model.pkl", "rb") as file:
    model = pickle.load(file)
st.title("Prediksi Harga Diamond")

carat = st.number_input("Carat")
cut = st.number_input("Cut")
color = st.number_input("Color")
clarity = st.number_input("Clarity")
depth = st.number_input("Depth")
table = st.number_input("Table")
x = st.number_input("X")
y = st.number_input("Y")
z = st.number_input("Z")

if st.button("Prediksi"):

    data = pd.DataFrame([[carat,cut,color,clarity,depth,table,x,y,z]],
    columns=['carat','cut','color','clarity','depth','table','x','y','z'])

    hasil = model.predict(data)

    st.success(f"Prediksi Harga: {hasil[0]}")