from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

# API Routes
from app.server.api.v1.endpoints.whatsapp_hook import router as Webhhook_router
from app.server.api.v1.endpoints.monnify_hook import router as Monnify_Router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(Webhhook_router, tags=["WhatsApp Webhooks"], prefix='/api/buyelectricityhook')
app.include_router(Monnify_Router, tags=["Monnify Webhook"], prefix='/api/monnifywebhook')


@app.get("/api")
async def start_bot():
    return {"message":"Welcome to EnergiEase: Your Journey to Smarter Energy Choices"}