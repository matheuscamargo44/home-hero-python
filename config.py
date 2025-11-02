from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Database Configuration
    DATABASE_URL: str = "mysql+pymysql://root:@localhost:3306/HomeHero?charset=utf8mb4"
    
    # JPA/Hibernate equivalent settings
    DB_SHOW_SQL: bool = True
    DB_FORMAT_SQL: bool = True
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()

