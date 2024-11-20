# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Arte & Tinta")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("COLORINDO A SUA OBRA.")

st.write("Como já deve ter percebido, o método st.write() é usado para escrita de texto e informações gerais!")

prompt = st.chat_input("Say something")
if prompt:
    st.write(f"User has sent the following prompt: {prompt}")
