import os
from dotenv import load_dotenv

class Config:
    """Centralized configuration that supports multiple environments."""
    
    BASE_URL = None
    BROWSER = None
    IMPLICIT_WAIT = None
    EXPLICIT_WAIT = None
    HEADLESS = None

    @classmethod
    def load(cls, env_name=None):
        if env_name is None:
            # Check environment variable, then default to prod
            env_name = os.getenv("ENV", "prod").lower()
        
        # Determine path (configs is in automation/)
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        env_file = os.path.join(base_dir, f".env.{env_name}")
        
        if not os.path.exists(env_file):
            print(f"Warning: {env_file} not found. Falling back to default .env")
            env_file = os.path.join(base_dir, ".env")
        else:
            print(f"Loading environment settings from: {env_file}")
            
        load_dotenv(env_file, override=True)
        
        cls.BASE_URL = os.getenv("BASE_URL")
        cls.BROWSER = os.getenv("BROWSER", "chrome").lower()
        cls.IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 10))
        cls.EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", 15))
        cls.HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"

# Initial load for default settings
Config.load()
