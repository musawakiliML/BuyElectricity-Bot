from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   MONGODB_URL: str
   WHATSAPP_URL: str
   WHATSAPP_TOKEN: str
   MONNIFY_API_KEY: str
   MONNIFY_SECRET_KEY: str
   MONNIFY_CONTRACT_CODE: str
   MONNIFY_WALLET_ACCOUNT_NO: str
   NGROK_URL: str
   
   class Config:
      env_file = '.env'