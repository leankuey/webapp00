# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Arte & Tinta")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("COLORINDO A SUA OBRA.")

st.write("Batata doce")

import streamlit as st

tamanho = st.slider("Qual o tamanho da parede?", 0, 20, 25)
st.write("Tamanho: ", tamanho, "m2")
