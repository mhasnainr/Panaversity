# 🤖 Hasnain's Chatbot

A conversational AI chatbot built with Chainlit and Google's Gemini API.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Google API Key (Get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd 02_chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   # or if using uv
   uv sync
   ```

3. **Set up environment variables**
   ```bash
   # Run the setup script
   python setup_env.py
   
   # Or manually copy the example file
   cp .env.example .env
   ```

4. **Add your API key**
   - Edit the `.env` file
   - Replace `your_google_api_key_here` with your actual Google API key

5. **Run the chatbot**
   ```bash
   chainlit run src/02_chatbot/agent.py
   ```

## 🔐 Security

### Environment Variables

This project uses environment variables to keep your API keys secure. Here's what's protected:

- **`.env`** - Contains your actual API keys (NEVER commit this file)
- **`.env.example`** - Template showing required variables (safe to commit)

### Files in `.gitignore`

The following files are automatically excluded from version control:

- `.env` and all environment files
- Python cache files (`__pycache__/`, `*.pyc`)
- Virtual environments (`.venv/`, `venv/`)
- IDE files (`.vscode/`, `.idea/`)
- OS files (`.DS_Store`, `Thumbs.db`)
- Logs and temporary files

## 📁 Project Structure

```
02_chatbot/
├── .env.example          # Environment template (safe to commit)
├── .gitignore           # Git ignore rules
├── setup_env.py         # Setup script
├── README.md            # This file
├── pyproject.toml       # Project configuration
├── src/
│   └── 02_chatbot/
│       ├── __init__.py
│       ├── agent.py     # Main chatbot logic
│       ├── config.py    # Configuration management
│       └── chainlit.md  # Chainlit UI configuration
└── .venv/               # Virtual environment (ignored)
```

## ⚙️ Configuration

### Environment Variables

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `GOOGLE_API_KEY` | ✅ | - | Your Google API key |
| `MODEL_NAME` | ❌ | `gemini-2.5-flash` | Gemini model to use |
| `BASE_URL` | ❌ | Google's API URL | API base URL |
| `DEBUG` | ❌ | `false` | Enable debug mode |

### Example `.env` file

```env
# Google API Configuration
GOOGLE_API_KEY=your_actual_api_key_here

# Optional: Model Configuration
MODEL_NAME=gemini-2.5-flash

# Optional: Base URL
BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai/

# Optional: Debug mode
DEBUG=false
```

## 🛠️ Development

### Running in Development

```bash
# Enable debug mode
echo "DEBUG=true" >> .env

# Run with debug logging
chainlit run src/02_chatbot/agent.py --debug
```

### Testing Configuration

```bash
# Check if your environment is set up correctly
python setup_env.py
```

## 🔧 Troubleshooting

### Common Issues

1. **"GOOGLE_API_KEY not set"**
   - Make sure you have a `.env` file
   - Check that your API key is correctly set in the `.env` file
   - Restart your application after making changes

2. **Import errors**
   - Ensure you're in the correct directory
   - Check that all dependencies are installed
   - Verify your Python environment is activated

3. **API errors**
   - Verify your Google API key is valid
   - Check that you have sufficient API quota
   - Ensure you're using the correct model name

## 📝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License.

## 🤝 Support

If you encounter any issues:

1. Check the troubleshooting section above
2. Review the configuration documentation
3. Open an issue on GitHub

---

**⚠️ Important Security Note**: Never commit your `.env` file or any files containing API keys to version control!
