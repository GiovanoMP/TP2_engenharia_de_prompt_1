from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importações explícitas
from app.api.routes.gpt2_routes import router as gpt2_router
from app.api.routes.translation_routes import router as translation_router

app = FastAPI(
    title="LLM Services API",
    description="API para serviços de geração de texto e tradução",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir rotas com nomes mais explícitos
app.include_router(gpt2_router)
app.include_router(translation_router)

@app.get("/")
async def root():
    return {
        "message": "LLM Services API",
        "services": ["text-generation", "translation"],
        "docs": "/docs",
        "openapi": "/openapi.json"
    }