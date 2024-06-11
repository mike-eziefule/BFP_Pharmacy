"""Default configuration settings."""
from functools import lru_cache

"""Default BaseSettings."""

class Settings():

    env_name: str = "local"
    base_url: str = "http://localhost:8000/"
    db_url: str = "sqlite:///./BFPpharmacy.sqlite"

    # default to SQLite
    app_server: str = "local" #change to 'development' when hosting
    
    #openai tags
    tags = [
        {'name': 'auth',
        'description': 'Routes related to Authentication and Authorization'
        },
        {'name': 'user',
        'description': 'Routes related to User Account creation'
        },
        {'name': 'shop',
        'description': 'Routes related to shopping'
        },
        {'name': 'info',
        'description': 'Routes related to browsing web pages and information'
        }
    ]
    
    SECRET_KEY = "ezzypharmbdbc97f82bfe593d1e45cec19ad2591af315096665512564df9af"
    ALGORITHM = "HS256"
    
    class Config:
        """Load env variables from .env file."""
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    """Return the current settings."""
    settings = Settings()
    if settings.app_server == "development":
        settings.db_url = "postgresql://ofqcobrn:zGAxW-IDKlJg4F2sYwCv-NfYZpYDV3ag@ruby.db.elephantsql.com/ofqcobrn"
        settings.base_url = "https://ez-ly.onrender.com/"
    return settings