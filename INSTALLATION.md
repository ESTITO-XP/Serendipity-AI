# 🚀 Installation Guide

Get **Serendipity AI** up and running on your system in just a few minutes!

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (Python 3.9+ recommended)
  ```bash
  python --version  # Should show 3.8 or higher
  ```
- **Git** - For cloning the repository
  ```bash
  git --version
  ```
- **pip** - Python package manager (usually comes with Python)
  ```bash
  pip --version
  ```
- **OpenAI API Key** - Get yours at [OpenAI Platform](https://platform.openai.com/api-keys)

---

## 🛠️ Installation Methods

### Method 1: Standard Installation (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI

# 2. Create and activate virtual environment (highly recommended)
python -m venv venv

# Activate virtual environment:
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate

# 3. Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# 4. Setup environment variables
cp .env.example .env
# Edit .env file with your OpenAI API key (see Configuration section below)

# 5. Run the application
python main.py
```

**🎉 That's it!** Visit `http://localhost:8000` to start using Serendipity AI.

---

### Method 2: Quick Start (One-liner)

For experienced developers who want to get started quickly:

```bash
git clone https://github.com/ESTITO-XP/Serendipity-AI.git && cd Serendipity-AI && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt && echo "OPENAI_API_KEY=your_key_here" > .env && echo "✅ Setup complete! Edit .env with your API key, then run: python main.py"
```

---

### Method 3: Development Installation

For contributors and developers who want the full development environment:

```bash
# 1. Fork the repository on GitHub first, then clone your fork
git clone https://github.com/YOUR_USERNAME/Serendipity-AI.git
cd Serendipity-AI

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install with development dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Install additional development tools
pip install pytest black flake8 mypy pre-commit

# 4. Setup environment
cp .env.example .env
# Edit .env with your configuration

# 5. Install pre-commit hooks (optional but recommended)
pre-commit install

# 6. Run in development mode with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## ⚙️ Configuration

### Environment Variables Setup

1. **Copy the example file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit the `.env` file** with your configuration:
   ```bash
   # Required - Get from https://platform.openai.com/api-keys
   OPENAI_API_KEY=sk-your-actual-api-key-here
   
   # Optional configurations
   PORT=8000
   LOG_LEVEL=INFO
   MAX_CONVERSATION_HISTORY=20
   ```

### Getting Your OpenAI API Key

1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign in or create an account
3. Navigate to "API Keys" section
4. Click "Create new secret key"
5. Copy the key and paste it in your `.env` file

**⚠️ Important:** Keep your API key secure and never commit it to version control!

---

## ✅ Verification

After installation, verify everything is working:

### 1. Check Health Endpoint
```bash
curl http://localhost:8000/health
```
Expected response:
```json
{
  "status": "healthy",
  "service": "Serendipity AI",
  "version": "1.0.0",
  "api_configured": true,
  "timestamp": 1692364800.0
}
```

### 2. Test Chat Functionality
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Hello! Can you introduce yourself?",
       "session_id": "test-session"
     }'
```

### 3. Access Web Interface
Open your browser and visit: `http://localhost:8000`

---

## 🐛 Troubleshooting

### Common Issues and Solutions

#### **"ModuleNotFoundError: No module named 'openai'"**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### **"OpenAI API key not configured"**
```bash
# Check your .env file exists and has the correct key
cat .env
# Make sure the key starts with 'sk-'
```

#### **"Permission denied" errors**
```bash
# On macOS/Linux, you might need:
chmod +x main.py
# Or run with python explicitly:
python main.py
```

#### **Port already in use**
```bash
# Use a different port
PORT=8001 python main.py
# Or kill the process using port 8000:
lsof -ti:8000 | xargs kill -9
```

#### **ImportError or dependency conflicts**
```bash
# Create a fresh virtual environment
deactivate  # if currently in venv
rm -rf venv
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 🚀 Next Steps

Once installation is complete:

1. **Explore the API** - Visit `http://localhost:8000/docs` for interactive documentation
2. **Customize the AI** - Modify the system prompt in `main.py` to change personality
3. **Deploy to production** - Check the README for deployment options
4. **Contribute** - See `CONTRIBUTING.md` for ways to improve the project

---

## 💡 Pro Tips

- **Always use virtual environments** - Keeps dependencies isolated
- **Keep your API key secure** - Never share or commit it
- **Monitor your OpenAI usage** - Check your API usage on OpenAI dashboard
- **Use development mode** - Run with `uvicorn main:app --reload` for auto-reload during development
- **Check logs** - Use `LOG_LEVEL=DEBUG` in `.env` for detailed logging

---

## 📞 Need Help?

- 📚 **Documentation**: Check the main [README.md](README.md)
- 🐛 **Issues**: Report bugs on [GitHub Issues](https://github.com/ESTITO-XP/Serendipity-AI/issues)
- 💬 **Discussions**: Ask questions in [GitHub Discussions](https://github.com/ESTITO-XP/Serendipity-AI/discussions)
- 📧 **Email**: Chat with me at [hehehola1177@hotmail.com](mailto:hehehola1177@hotmail.com)
- 🎮 **Discord**: Message me on [Discord](https://discord.com/users/1191348720227332248)

---

*Happy coding! 🎉 Enjoy building with Serendipity AI!*
