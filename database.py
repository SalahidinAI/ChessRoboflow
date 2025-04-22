from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config import config
from models import PredictionModel

client = AsyncIOMotorClient(
    config.MONGODB_URL
)

database = client[config.DB_NAME]

async def init_db():
    await init_beanie(database=database, document_models=[PredictionModel])

try:
    client.server_info()
    print('Connected to data base')
except Exception as e:
    print(f'Data base connection ERROR: {e}')