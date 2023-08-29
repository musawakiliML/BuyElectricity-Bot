import motor.motor_asyncio
import asyncio
from app.server.config.config import Settings

settings = Settings()

# Database Configuration

client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGODB_URL, serverSelectionTimeoutMS=5000)
client.get_io_loop = asyncio.get_event_loop

try:
    db_connection = client.server_info()
    print(f'Connected to MongoDB Server')
except Exception as e:
    print("Unable to connect to the MongoDB server.")
    print(str(e))

database = client.buyelectricity

# Database Collections

user_sessions = database.get_collection("user_session")
user_orders = database.get_collection("orders")