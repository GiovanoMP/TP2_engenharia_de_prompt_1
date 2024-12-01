# tests/streamlit_translation_test.py

import streamlit as st
import requests
import json

def main():
    st.title("English to French Translation Tester")
    
    # Criar duas colunas
    col1, col2 = st.columns(2)
    
    with col1:
        st.header("Input")
        # Input de texto
        input_text = st.text_area(
            "Enter English text:",
            value="Hello, how are you?",
            height=200
        )
        
        # Checkbox para max_length
        use_max_length = st.checkbox("Set maximum length?")
        
        # Slider para max_length se checkbox ativado
        max_length = None
        if use_max_length:
            max_length = st.slider(
                "Maximum translation length:",
                min_value=10,
                max_value=500,
                value=100
            )
    
    # Botão para traduzir
    if st.button("Translate"):
        # URL do endpoint
        url = "http://localhost:8000/api/v1/translate/en-to-fr"
        
        # Dados para a requisição
        data = {
            "text": input_text,
            "max_length": max_length
        }
        
        try:
            with st.spinner("Translating..."):
                # Fazer requisição
                response = requests.post(url, json=data)
                
                if response.status_code == 200:
                    result = response.json()
                    
                    with col2:
                        st.header("Output")
                        st.success("Translation completed!")
                        
                        st.subheader("Original Text:")
                        st.write(result["source_text"])
                        
                        st.subheader("French Translation:")
                        st.write(result["translated_text"])
                        
                        # Adicionar métricas
                        st.metric(
                            label="Original length", 
                            value=len(result["source_text"].split())
                        )
                        st.metric(
                            label="Translation length", 
                            value=len(result["translated_text"].split())
                        )
                else:
                    st.error(f"Error: {response.status_code}")
                    st.write(response.text)
                    
        except Exception as e:
            st.error(f"Error connecting to API: {str(e)}")
    
    # Adicionar informações sobre a API
    with st.expander("API Information"):
        st.write("""
        This interface tests the English to French translation API.
        - Endpoint: http://localhost:8000/api/v1/translate/en-to-fr
        - Method: POST
        - Format: JSON
        """)

if __name__ == "__main__":
    main()