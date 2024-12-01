# app/api/models/translation_models.py

from pydantic import BaseModel, Field
from typing import Optional

class TranslationRequest(BaseModel):
    text: str = Field(
        ...,
        description="Texto em inglês para ser traduzido",
        min_length=1,
        max_length=5000
    )
    max_length: Optional[int] = Field(
        default=None,
        description="Tamanho máximo da tradução (opcional)",
        ge=1,
        le=5000
    )

class TranslationResponse(BaseModel):
    source_text: str = Field(
        ...,
        description="Texto original em inglês"
    )
    translated_text: str = Field(
        ...,
        description="Texto traduzido em francês"
    )