"""
Configuration module for the chatbot application.
Handles environment variables securely with proper validation.
"""

import os
from typing import Optional
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())


class Config:
    """Configuration class to manage environment variables."""
    
    def __init__(self):
        self._google_api_key: Optional[str] = None
        self._model_name: Optional[str] = None
        self._base_url: Optional[str] = None
        self._debug: bool = False
        
        self._load_config()
    
    def _load_config(self):
        """Load configuration from environment variables."""
        # Required: Google API Key
        self._google_api_key = os.getenv("GOOGLE_API_KEY")
        
        # Optional: Model configuration
        self._model_name = os.getenv("MODEL_NAME", "gemini-2.5-flash")
        
        # Optional: Base URL
        self._base_url = os.getenv(
            "BASE_URL", 
            "https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        
        # Optional: Debug mode
        debug_str = os.getenv("DEBUG", "false").lower()
        self._debug = debug_str in ("true", "1", "yes", "on")
    
    @property
    def google_api_key(self) -> str:
        """Get the Google API key."""
        if not self._google_api_key:
            raise ValueError(
                "GOOGLE_API_KEY environment variable is not set. "
                "Please set it in your .env file or environment variables."
            )
        return self._google_api_key
    
    @property
    def model_name(self) -> str:
        """Get the model name."""
        return self._model_name
    
    @property
    def base_url(self) -> str:
        """Get the base URL for the API."""
        return self._base_url
    
    @property
    def debug(self) -> bool:
        """Get debug mode status."""
        return self._debug
    
    def validate(self) -> bool:
        """Validate that all required configuration is present."""
        try:
            # This will raise an error if the API key is missing
            _ = self.google_api_key
            return True
        except ValueError:
            return False
    
    def get_setup_instructions(self) -> str:
        """Get setup instructions for missing configuration."""
        return """
To set up your environment variables:

1. Copy the example file:
   cp .env.example .env

2. Edit the .env file and add your actual API key:
   GOOGLE_API_KEY=your_actual_api_key_here

3. Get your Google API key from: https://makersuite.google.com/app/apikey

4. Restart your application after making changes.

Note: Never commit your .env file to version control!
        """.strip()


# Global configuration instance
config = Config()


def get_config() -> Config:
    """Get the global configuration instance."""
    return config 