# app/api/services/translation_service.py

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from typing import Optional

class TranslationService:
    def __init__(self, model_name: str = "Helsinki-NLP/opus-mt-en-fr"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)
        
    async def translate(self, text: str, max_length: Optional[int] = None) -> str:
        try:
            # Tokenizar o input
            inputs = self.tokenizer(text, return_tensors="pt", padding=True).to(self.device)
            
            # Calcular max_length apropriado
            input_length = len(self.tokenizer.encode(text))
            if max_length is None or max_length <= input_length:
                max_length = input_length * 2  # Uma estimativa segura
            
            # Gerar tradução
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_length,  # Usando max_new_tokens em vez de max_length
                num_beams=4,
                length_penalty=0.6,
                early_stopping=True
            )
            
            # Decodificar a tradução
            translated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            return translated_text
            
        except Exception as e:
            raise RuntimeError(f"Erro na tradução: {str(e)}")

    @classmethod
    async def create(cls) -> 'TranslationService':
        return cls()