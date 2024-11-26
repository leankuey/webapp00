import streamlit as st

# Título e introdução do Web App
st.title("Arte & Tinta")
st.header("Colorindo a sua obra.")
st.caption("Calcule a quantidade de tinta necessária para a sua pintura de forma rápida e prática.")

st.image(
    "https://www.interlarinterlagos.com.br/blog/wp-content/uploads/2023/05/Tipos_de_tintas_-_Home_Blog-1140x760.jpg",  # URL da imagem ou caminho local
    caption="Esta é uma imagem fixa no aplicativo.",
    use_column_width=True
)

# Entradas básicas: altura e comprimento da parede
altura = st.number_input("Digite a altura da parede (em metros):", min_value=0.0, format="%.2f")
comprimento = st.number_input("Digite o comprimento da parede (em metros):", min_value=0.0, format="%.2f")

# Calcular área total da parede (somente se valores válidos forem fornecidos)
if altura > 0 and comprimento > 0:
    area_parede = altura * comprimento
    st.write(f"A área total da parede é **{area_parede:.2f} m²**.")

    # Inicializar áreas de portas e janelas
    area_portas = 0
    area_janelas = 0

    # Verificar se há portas
    if st.radio("A parede possui portas?", ["Não", "Sim"]) == "Sim":
        altura_porta = st.number_input("Digite a altura da porta (em metros):", min_value=0.0, format="%.2f")
        comprimento_porta = st.number_input("Digite o comprimento da porta (em metros):", min_value=0.0, format="%.2f")
        if altura_porta > 0 and comprimento_porta > 0:
            area_portas = altura_porta * comprimento_porta
            st.info(f"A área ocupada pela porta é **{area_portas:.2f} m²**.")

    # Verificar se há janelas
    if st.radio("A parede possui janelas?", ["Não", "Sim"]) == "Sim":
        altura_janela = st.number_input("Digite a altura da janela (em metros):", min_value=0.0, format="%.2f")
        comprimento_janela = st.number_input("Digite o comprimento da janela (em metros):", min_value=0.0, format="%.2f")
        if altura_janela > 0 and comprimento_janela > 0:
            area_janelas = altura_janela * comprimento_janela
            st.info(f"A área ocupada pela janela é **{area_janelas:.2f} m²**.")

    # Somar áreas de portas e janelas e calcular a área útil
    area_total_aberturas = area_portas + area_janelas
    if area_total_aberturas > area_parede:
        st.warning("A área total das aberturas não pode ser maior que a área total da parede!")
        area_util = 0
    else:
        area_util = area_parede - area_total_aberturas
        st.success(f"A área útil da parede (descontando portas e janelas) é **{area_util:.2f} m²**.")

    # Calcular quantidade de tinta necessária
    if area_util > 0:
        rendimento_tinta = st.number_input(
            "Digite o rendimento da tinta (em m² por litro):", min_value=1.0, format="%.2f"
        )
        tamanho_lata = st.number_input(
            "Digite o tamanho da lata de tinta (em litros):", min_value=0.5, format="%.2f"
        )
        if rendimento_tinta > 0 and tamanho_lata > 0:
            tinta_necessaria = (area_util * 2) / rendimento_tinta  # Duas demãos
            latas_necessarias = -(-tinta_necessaria // tamanho_lata)  # Arredondamento para cima
            st.success(
                f"Você precisará de aproximadamente **{latas_necessarias:.0f} lata(s)** de {tamanho_lata:.2f} litros."
            )
else:
    st.info("Por favor, insira valores válidos para altura e comprimento.")
