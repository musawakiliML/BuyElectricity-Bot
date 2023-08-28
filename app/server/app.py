from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# API Routes
from app.server.api.v1.endpoints.whatsapp_hook import router as Webhhook_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Webhhook_router, tags=["WhatsApp Webhooks"], prefix='/buyelectricityhook')
