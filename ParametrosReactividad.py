import streamlit as st
import pandas as pd

st.title("My primer app")
st.write("Hola mundo")

st.button("Holi")
#st.button(":D")

#dt es data frame
df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

st.write(df)

st.map(df)

#Buscar steamlit API
#st.latex("\r^2 + a r^3\sum_{k=0}^{n-1} ar^\")

st.markdown(" **este es una viñeta** ")
