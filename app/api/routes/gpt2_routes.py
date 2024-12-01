# app/api/routes/gpt2_routes.py

from fastapi import APIRouter, HTTPException, Depends
from ..models.gpt2_models import TextGenerationRequest, TextGenerationResponse
from ..services.gpt2_service import GPT2Service
from typing import Optional

# Criar router
router = APIRouter(
    prefix="/api/v1/gpt2",
    tags=["text-generation"],
    responses={404: {"description": "Not found"}}
)

# Dependency para obter o serviço GPT-2
async def get_gpt2_service() -> GPT2Service:
    service = await GPT2Service.create()
    try:
        yield service
    finally:
        # Cleanup se necessário
        pass

@router.post("/generate", 
    response_model=TextGenerationResponse,
    summary="Gera texto usando GPT-2",
    description="Recebe um texto de entrada e gera uma continuação usando o modelo GPT-2")
async def generate_text(
    request: TextGenerationRequest,
    service: GPT2Service = Depends(get_gpt2_service)
):
    """
    Endpoint para geração de texto.
    
    Args:
        request: TextGenerationRequest contendo o texto de entrada e parâmetros
        service: Instância do serviço GPT-2 (injetada automaticamente)
    
    Returns:
        TextGenerationResponse com o texto original e o texto gerado
    
    Raises:
        HTTPException: Se houver erro na geração do texto
    """
    try:
        generated_text = await service.generate_text(
            prompt=request.text,
            max_length=request.max_length
        )
        
        return TextGenerationResponse(
            input_text=request.text,
            generated_text=generated_text
        )
        
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao gerar texto: {str(e)}"
        )

@router.get("/health", 
    summary="Verifica status do serviço",
    description="Endpoint para verificar se o serviço está funcionando")
async def health_check():
    """
    Endpoint de health check.
    
    Returns:
        dict: Status do serviço
    """
    return {"status": "healthy", "model": "gpt2"}