from pydantic import BaseModel, Field

class TextGenerationRequest(BaseModel):
    text: str = Field(
        ...,  # ... significa que é obrigatório
        description="O texto de entrada para gerar a continuação",
        min_length=1,
        max_length=1000
    )
    max_length: int = Field(
        default=100,
        description="Tamanho máximo do texto gerado",
        ge=1,  # maior ou igual a 1
        le=1000  # menor ou igual a 1000
    )

class TextGenerationResponse(BaseModel):
    input_text: str = Field(
        ...,
        description="O texto original fornecido como entrada"
    )
    generated_text: str = Field(
        ...,
        description="O texto gerado pelo modelo GPT-2"
    )