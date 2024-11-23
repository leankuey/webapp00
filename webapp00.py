# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Arte & Tinta")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("COLORINDO A SUA OBRA.")

import streamlit as st

# Entrada do usuário
altura = st.number_input("Digite a altura da parede (em metros):", min_value=0.0, format="%.2f")
comprimento = st.number_input("Digite o comprimento da parede (em metros):", min_value=0.0, format="%.2f")

# Calcular área
if altura > 0 and comprimento > 0:
    area = altura * comprimento
    st.success(f"A área da parede é {area:.2f} metros quadrados.")
else:
    st.info("Por favor, insira valores válidos para altura e comprimento.")

# Nota opcional
st.caption("Este aplicativo foi criado para ajudar você a calcular a área de paredes de forma rápida e prática.")

