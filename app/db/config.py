import os
from dotenv import load_dotenv  
from pathlib import Path

#Para simplificar
POSTGRES_USER = os.getenv('POSTGRES_USER')
print(POSTGRES_USER)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
#POSTGRES_MY_DB = os.getenv("POSTGRES_DB")
#print(POSTGRES_USER)

class Settings:
    PROJECT_NAME:str = "Luiza Board"
    PROJECT_VERSION: str = "1.0.0"
    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT") # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
settings = Settings()

#2