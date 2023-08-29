from pydantic_settings import BaseSettings

class Settings(BaseSettings):
   MONGODB_URL: str
   WHATSAPP_URL: str
   WHATSAPP_TOKEN: str

   class Config:
      env_file = '.env'