# MEU PRIMEIRO WEB APP
import streamlit as st
  
# Use st.title("") para adicionar um TÍTULO ao seu Web app
st.title("Arte & Tinta")

# Use st.header("") para adicionar um CABEÇALHO ao seu Web app
st.header("COLORINDO A SUA OBRA.")

st.whrite("Digite o tamanho da parede")

def calcular_tinta(altura, largura, rendimento_tinta):
    # Calcula a área da parede
    area_parede = altura * largura
    # Calcula a quantidade de tinta necessária, considerando o rendimento
    quantidade_tinta = area_parede / rendimento_tinta
    return quantidade_tinta

# Função principal
def main():
    print("Calculadora de Tinta para Pintura de Parede")
    
    # Entrada do usuário
    altura = float(input("Digite a altura da parede (em metros): "))
    largura = float(input("Digite a largura da parede (em metros): "))
    
    # Rendimento padrão de tinta (em m² por litro)
    rendimento_tinta = 12  # Rendimento médio de tinta (m²/litro), pode variar dependendo da tinta

    # Calcular a quantidade de tinta necessária
    tinta_necessaria = calcular_tinta(altura, largura, rendimento_tinta)
    
    # Exibir o resultado
    print(f"\nVocê precisará de {tinta_necessaria:.2f} litros de tinta para pintar a parede.")

if __name__ == "__main__":
    main()
