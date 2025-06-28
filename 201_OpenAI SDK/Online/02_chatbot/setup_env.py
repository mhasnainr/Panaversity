#!/usr/bin/env python3
"""
Setup script to help configure environment variables for the chatbot.
This script will create a .env file from the example if it doesn't exist.
"""

import os
import shutil
from pathlib import Path


def setup_environment():
    """Set up the environment configuration."""
    env_file = Path(".env")
    example_file = Path(".env.example")
    
    print("🤖 Chatbot Environment Setup")
    print("=" * 40)
    
    # Check if .env.example exists
    if not example_file.exists():
        print("❌ Error: .env.example file not found!")
        print("Please ensure .env.example exists in the project root.")
        return False
    
    # Check if .env already exists
    if env_file.exists():
        print("✅ .env file already exists!")
        print("If you need to update your API key, edit the .env file manually.")
        return True
    
    # Copy .env.example to .env
    try:
        shutil.copy2(example_file, env_file)
        print("✅ Created .env file from .env.example")
        print("\n📝 Next steps:")
        print("1. Edit the .env file and replace 'your_google_api_key_here' with your actual API key")
        print("2. Get your Google API key from: https://makersuite.google.com/app/apikey")
        print("3. Save the .env file")
        print("4. Restart your application")
        print("\n⚠️  Important: Never commit your .env file to version control!")
        return True
        
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")
        return False


def check_environment():
    """Check if the environment file exists."""
    print("\n🔍 Checking environment configuration...")
    
    env_file = Path(".env")
    if not env_file.exists():
        print("❌ .env file not found!")
        print("Run this script to create it from .env.example")
        return False
    
    print("✅ .env file exists!")
    print("Make sure to add your actual API key to the .env file.")
    return True


if __name__ == "__main__":
    print("🚀 Welcome to the Chatbot Environment Setup!")
    
    # Setup environment
    if setup_environment():
        # Check configuration
        check_environment()
    
    print("\n✨ Setup complete!") 