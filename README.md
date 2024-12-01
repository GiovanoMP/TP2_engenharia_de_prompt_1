# LLM FastAPI Project

Este projeto implementa uma API RESTful usando FastAPI que integra diferentes modelos de linguagem para processamento de texto. Atualmente, suporta dois serviços principais:

1. Geração de texto usando GPT-2
2. Tradução de inglês para francês usando Helsinki-NLP/opus-mt-en-fr

## 🚀 Funcionalidades

### Geração de Texto (GPT-2)
- **Endpoint**: `/api/v1/gpt2/generate`
- Gera continuações de texto a partir de um prompt inicial
- Suporte a controle de comprimento do texto gerado

### Tradução (EN-FR)
- **Endpoint**: `/api/v1/translate/en-to-fr`
- Traduz texto do inglês para o francês
- Otimizado para diferentes tamanhos de texto

## 🛠️ Tecnologias Utilizadas

- FastAPI
- Transformers (Hugging Face)
- PyTorch
- Streamlit (para interface de teste)
- Pydantic
- Uvicorn

## 📋 Pré-requisitos

```bash
python 3.8+
pip
git
