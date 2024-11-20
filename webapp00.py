# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Arte & Tinta")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("COLORINDO A SUA OBRA.")

st.write("Batata doce")

import streamlit as st

tamanho = st.slider("Qual a altura da parede?", 0, 130, 25)
st.write("Altura: ", tamanho, "m2")
