# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Arte & Tinta")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("COLORINDO A SUA OBRA.")

st.caption("Este aplicativo foi criado para ajudar você a calcular a quantidade de tinta necessaria para a sua pintura de forma rápida e prática.")

# Entrada do usuário para altura e comprimento da parede
altura = st.number_input("Digite a altura da parede (em metros):", min_value=0.0, format="%.2f")
comprimento = st.number_input("Digite o comprimento da parede (em metros):", min_value=0.0, format="%.2f")

# Calcular a área inicial da parede
if altura > 0 and comprimento > 0:
    area_parede = altura * comprimento
    st.write(f"A área total da parede é **{area_parede:.2f} metros quadrados**.")

    # Perguntar ao usuário se há portas ou janelas
    ha_aberturas = st.radio("A parede possui portas ou janelas?", ("Não", "Sim"))

    if ha_aberturas == "Sim":
        area_aberturas = st.number_input(
            "Digite a área total ocupada pelas portas e janelas (em metros quadrados):",
            min_value=0.0,
            max_value=area_parede,
            format="%.2f",
        )

        # Calcular a área útil
        if area_aberturas > area_parede:
            st.warning("A área das aberturas não pode ser maior que a área total da parede!")
        else:
            area_util = area_parede - area_aberturas
            st.success(f"A área útil da parede (descontando portas e janelas) é **{area_util:.2f} metros quadrados**.")
    else:
        area_util = area_parede
        st.info("Não há portas ou janelas na parede, a área útil é igual à área total.")

    # Perguntar sobre o rendimento da tinta
    rendimento_tinta = st.number_input(
        "Digite o rendimento da tinta (em metros quadrados por litro):",
        min_value=1.0,
        format="%.2f",
    )

    if rendimento_tinta > 0:
        # Calcular a quantidade de tinta necessária para duas demãos
        tinta_necessaria = (area_util * 2) / rendimento_tinta

        # Calcular o número de latas de tinta (arredondando para cima)
        tamanho_lata = st.number_input(
            "Digite o tamanho da lata de tinta (em litros):", min_value=0.5, format="%.2f"
        )
        if tamanho_lata > 0:
            latas_necessarias = -(-tinta_necessaria // tamanho_lata)  # Arredonda para cima
            st.success(
                f"Para pintar a parede com pelo menos **duas demãos**, você precisará de aproximadamente **{latas_necessarias:.0f} lata(s)** de tinta de {tamanho_lata:.2f} litros."
            )
        else:
            st.warning("Insira um tamanho válido para a lata de tinta!")
else:
    st.info("Por favor, insira valores válidos.")
