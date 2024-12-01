# tests/streamlit_test.py

import streamlit as st
import requests
import json

def main():
    st.title("GPT-2 Text Generation Tester")
    
    # Input de texto
    input_text = st.text_area(
        "Digite o texto inicial:",
        value="Once upon a time",
        height=100
    )
    
    # Slider para max_length
    max_length = st.slider(
        "Tamanho máximo do texto gerado:",
        min_value=50,
        max_value=500,
        value=100
    )
    
    # Botão para gerar texto
    if st.button("Gerar Texto"):
        # URL do endpoint
        url = "http://localhost:8000/api/v1/gpt2/generate"
        
        # Dados para a requisição
        data = {
            "text": input_text,
            "max_length": max_length
        }
        
        try:
            with st.spinner("Gerando texto..."):
                # Fazer requisição
                response = requests.post(url, json=data)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    # Mostrar resultados
                    st.success("Texto gerado com sucesso!")
                    
                    st.subheader("Texto Original:")
                    st.write(result["input_text"])
                    
                    st.subheader("Texto Gerado:")
                    st.write(result["generated_text"])
                else:
                    st.error(f"Erro: {response.status_code}")
                    st.write(response.text)
                    
        except Exception as e:
            st.error(f"Erro ao conectar com a API: {str(e)}")
    
    # Adicionar informações sobre a API
    with st.expander("Informações da API"):
        st.write("""
        Esta interface testa a API GPT-2 que está rodando localmente.
        - Endpoint: http://localhost:8000/api/v1/gpt2/generate
        - Método: POST
        - Formato: JSON
        """)

if __name__ == "__main__":
    main()