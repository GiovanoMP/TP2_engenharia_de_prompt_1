# app/api/services/gpt2_service.py

from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
from typing import Optional

class GPT2Service:
    def __init__(self, model_name: str = "gpt2"):
        """
        Inicializa o serviço GPT-2 carregando o modelo e tokenizer.
        
        Args:
            model_name (str): Nome do modelo GPT-2 a ser usado
        """
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        
        # Verificar se há GPU disponível
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = self.model.to(self.device)
        
    async def generate_text(self, prompt: str, max_length: int = 100) -> str:
        """
        Gera texto a partir de um prompt usando o modelo GPT-2.
        
        Args:
            prompt (str): Texto de entrada para gerar a continuação
            max_length (int): Comprimento máximo do texto gerado
            
        Returns:
            str: Texto gerado
        """
        try:
            # Tokenizar o input
            inputs = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
            
            # Configurar parâmetros de geração
            attention_mask = torch.ones(inputs.shape, dtype=torch.long, device=self.device)
            
            # Gerar texto
            outputs = self.model.generate(
                inputs,
                attention_mask=attention_mask,
                max_length=max_length,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=0.7,
                pad_token_id=self.tokenizer.eos_token_id
            )
            
            # Decodificar o texto gerado
            generated_text = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            return generated_text
            
        except Exception as e:
            raise RuntimeError(f"Erro ao gerar texto: {str(e)}")
    
    @classmethod
    async def create(cls) -> 'GPT2Service':
        """
        Factory method para criar uma instância do serviço.
        Útil para inicialização assíncrona quando necessário.
        """
        return cls()