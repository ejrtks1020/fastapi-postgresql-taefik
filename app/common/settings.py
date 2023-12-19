import os
from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    '''
    automatically loaded from the environment variable
    We could have used os.getenv(), but as the number of environment variables increases, this becomes very repetitive. 
    By using BaseSettings, you can specify the environment variable name and it will automatically be loaded.    
    '''
    db_url: str = Field(os.getenv("DATABASE_URL", "postgresql://knh:knh1!@localhost:5432/knh")) # Field(..., env="DATABASE_URL")

settings = Settings()