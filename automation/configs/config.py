import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class Config:
    """Centralized configuration for the test framework."""
    
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")
    BROWSER = os.getenv("BROWSER", "chrome").lower()
    IMPLICIT_WAIT = int(os.getenv("IMPLICIT_WAIT", 10))
    EXPLICIT_WAIT = int(os.getenv("EXPLICIT_WAIT", 15))
    HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"
