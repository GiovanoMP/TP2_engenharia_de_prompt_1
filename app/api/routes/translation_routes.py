# app/api/routes/translation_routes.py

from fastapi import APIRouter, HTTPException, Depends
from ..models.translation_models import TranslationRequest, TranslationResponse
from ..services.translation_service import TranslationService
from typing import Optional

# Criar router
router = APIRouter(
    prefix="/api/v1/translate",
    tags=["translation"],
    responses={404: {"description": "Not found"}}
)

# Dependency para obter o serviço de tradução
async def get_translation_service() -> TranslationService:
    service = await TranslationService.create()
    try:
        yield service
    finally:
        # Cleanup se necessário
        pass

@router.post(
    "/en-to-fr",
    response_model=TranslationResponse,
    summary="Traduz texto do inglês para o francês",
    description="Recebe um texto em inglês e retorna sua tradução em francês"
)
async def translate_text(
    request: TranslationRequest,
    service: TranslationService = Depends(get_translation_service)
):
    """
    Endpoint para tradução de texto.
    
    Args:
        request: TranslationRequest contendo o texto a ser traduzido
        service: Instância do serviço de tradução (injetada automaticamente)
    
    Returns:
        TranslationResponse com o texto original e sua tradução
    
    Raises:
        HTTPException: Se houver erro na tradução
    """
    try:
        translated_text = await service.translate(
            text=request.text,
            max_length=request.max_length
        )
        
        return TranslationResponse(
            source_text=request.text,
            translated_text=translated_text
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro na tradução: {str(e)}"
        )

@router.get("/health")
async def health_check():
    """
    Verifica status do serviço de tradução
    """
    return {
        "status": "healthy",
        "model": "Helsinki-NLP/opus-mt-en-fr",
        "service": "translation"
    }