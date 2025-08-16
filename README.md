# 🤖 Serendipity AI
![Image](https://github.com/user-attachments/assets/5ae49c13-d0e4-4ae6-9854-16d469863a0b)

<div align="center">
  <img src="https://img.shields.io/badge/AI-Powered-blue?style=for-the-badge&logo=openai" alt="AI Powered">
  <img src="https://img.shields.io/badge/FastAPI-Framework-green?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Python-3.8+-yellow?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge" alt="License">
</div>

<div align="center">
  <h3>🌟 Your intelligent, supportive companion designed to spark delightful discoveries 🌟</h3>
  <p>Built with FastAPI, powered by OpenAI, enhanced with Claude AI automation</p>
</div>

---

## 📖 Table of Contents

- [✨ Features](#-features)
- [🚀 Quick Start](#-quick-start)
- [📦 Installation](#-installation)
- [🔧 Configuration](#-configuration)
- [🎯 Usage](#-usage)
- [🤖 AI Automation](#-ai-automation)
- [🏗️ Architecture](#️-architecture)
- [🛠️ API Documentation](#️-api-documentation)
- [🧪 Development](#-development)
- [🚢 Deployment](#-deployment)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [🆘 Support](#-support)

---

## ✨ Features

### 🎭 **AI Personality**
- **Warm & Supportive**: Genuinely encouraging and curious about your thoughts
- **Insightful**: Helps explore new ideas and perspectives
- **Creative**: Suggests interesting connections and possibilities
- **Respectful**: Always maintains boundaries and user autonomy

### 🛠️ **Technical Features**
- 🚀 **FastAPI Backend** - High-performance, modern Python web framework
- 🤖 **OpenAI Integration** - Powered by GPT models for intelligent conversations
- 💬 **Session Management** - Maintains conversation context across interactions
- 🎨 **Modern UI** - Responsive, mobile-friendly chat interface
- 📊 **Health Monitoring** - Built-in health checks and status endpoints
- 🔒 **Security** - Input validation, error handling, and secure API practices
- 🤖 **Claude Automation** - AI-powered GitHub automation for continuous improvement

### 🌐 **Deployment Ready**
- 📦 **Containerized** - Docker support for easy deployment
- ☁️ **Cloud Native** - Ready for Replit, Heroku, AWS, GCP, Azure
- ⚡ **Production Grade** - Gunicorn, logging, monitoring included
- 🔧 **CI/CD** - GitHub Actions with automated AI enhancements

---

## 🚀 Quick Start

Get Serendipity AI running in under 5 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up environment
cp .env.example .env
# Edit .env with your OpenAI API key

# 4. Run the application
python main.py
```

🎉 **That's it!** Visit `http://localhost:8000` to start chatting with Serendipity AI.

---

## 📦 Installation

### Prerequisites
- **Python 3.8+** (Python 3.9+ recommended)
- **Git**
- **OpenAI API Key** ([Get one here](https://platform.openai.com/api-keys))

### Option 1: Standard Installation
```bash
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Option 2: Development Installation
```bash
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI

# Install with development dependencies
pip install -r requirements.txt
pip install pytest black flake8  # Additional dev tools

# Install pre-commit hooks (optional)
pre-commit install
```

### Option 3: Docker Installation
```bash
# Clone repository
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI

# Build and run with Docker
docker build -t serendipity-ai .
docker run -p 8000:8000 --env-file .env serendipity-ai
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```bash
# Required
OPENAI_API_KEY=your_openai_api_key_here

# Optional
PORT=8000
LOG_LEVEL=INFO
MAX_CONVERSATION_HISTORY=20
```

### Configuration Options

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `OPENAI_API_KEY` | OpenAI API key for AI functionality | - | ✅ |
| `PORT` | Port number for the web server | `8000` | ❌ |
| `LOG_LEVEL` | Logging level (DEBUG, INFO, WARNING, ERROR) | `INFO` | ❌ |
| `MAX_CONVERSATION_HISTORY` | Max messages to keep in conversation | `20` | ❌ |

---

## 🎯 Usage

### Web Interface
1. Start the application: `python main.py`
2. Open your browser to `http://localhost:8000`
3. Start chatting with Serendipity AI!

### API Usage

#### Send a Chat Message
```bash
curl -X POST "http://localhost:8000/chat" \
     -H "Content-Type: application/json" \
     -d '{
       "message": "Hello, how are you today?",
       "session_id": "my-session"
     }'
```

#### Get Conversation History
```bash
curl "http://localhost:8000/history/my-session"
```

#### Health Check
```bash
curl "http://localhost:8000/health"
```

---

## 🤖 AI Automation

Serendipity AI features **Claude-powered automation** that continuously improves the codebase:

### How It Works
1. **Issue Creation**: Create an issue mentioning "claude" 
2. **Automatic Analysis**: Claude analyzes the request and current code
3. **Enhancement Generation**: AI generates improvements and fixes
4. **Pull Request**: Automatically creates a PR with the changes
5. **Review & Merge**: Human review before integration

### Triggering Automation
```bash
# Method 1: Create an issue with "claude" in the body
# Method 2: Manual workflow dispatch
gh workflow run claude-automation.yml -f task="Enhance the UI design"

# Method 3: Use labels
# Add "claude-automation" label to any issue
```

### Automation Features
- 🔍 **Code Analysis** - Reviews current implementation
- 🛠️ **Bug Fixes** - Automatically identifies and fixes issues  
- 🎨 **UI/UX Improvements** - Enhances user interface
- 📚 **Documentation Updates** - Keeps docs current
- 🔒 **Security Enhancements** - Improves security practices
- ⚡ **Performance Optimization** - Optimizes code performance

---

## 🏗️ Architecture

```
🏠 Serendipity AI Architecture
┌─────────────────────────────────────────────┐
│                Frontend                     │
│  ┌─────────────────────────────────────┐   │
│  │     HTML/CSS/JavaScript             │   │
│  │   - Modern chat interface           │   │
│  │   - Responsive design               │   │
│  │   - Real-time messaging             │   │
│  └─────────────────────────────────────┘   │
└─────────────────┬───────────────────────────┘
                  │ HTTP/WebSocket
┌─────────────────▼───────────────────────────┐
│                Backend                      │
│  ┌─────────────────────────────────────┐   │
│  │         FastAPI Server              │   │
│  │   - REST API endpoints              │   │
│  │   - Session management              │   │
│  │   - Input validation                │   │
│  │   - Error handling                  │   │
│  └─────────────────────────────────────┘   │
└─────────────────┬───────────────────────────┘
                  │ API Calls
┌─────────────────▼───────────────────────────┐
│              AI Services                    │
│  ┌─────────────────┐ ┌─────────────────┐   │
│  │   OpenAI API    │ │   Claude API    │   │
│  │ - Chat responses│ │ - Code automation│   │
│  │ - GPT models    │ │ - Enhancement   │   │
│  └─────────────────┘ └─────────────────┘   │
└─────────────────────────────────────────────┘
```

### Key Components

- **FastAPI Server**: High-performance ASGI web framework
- **Conversation Store**: In-memory session management (Redis in production)
- **OpenAI Integration**: GPT-powered conversational AI
- **Claude Automation**: AI-driven code enhancement
- **Static Files**: Modern, responsive web interface

---

## 🛠️ API Documentation

Once running, visit these URLs for complete API documentation:

- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Main Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Main chat interface |
| `GET` | `/health` | Health check |
| `GET` | `/about` | Project information |
| `POST` | `/chat` | Send chat message |
| `GET` | `/history/{session_id}` | Get conversation history |
| `POST` | `/clear-chat` | Clear conversation |
| `GET` | `/sessions` | List active sessions |

---

## 🧪 Development

### Setting Up Development Environment

```bash
# Clone and setup
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI
python -m venv venv
source venv/bin/activate

# Install with dev dependencies  
pip install -r requirements.txt
pip install pytest black flake8 mypy

# Run in development mode
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Code Quality Tools

```bash
# Format code
black main.py

# Lint code  
flake8 main.py

# Type checking
mypy main.py

# Run tests
pytest
```

### Project Structure

```
Serendipity-AI/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── .env.example           # Environment template
├── static/
│   └── index.html         # Frontend interface
├── .github/
│   └── workflows/         # GitHub Actions
│       └── claude-automation.yml
├── tests/                 # Test files
├── docs/                  # Documentation
└── README.md             # This file
```

---

## 🚢 Deployment

### Option 1: Replit (Easiest)
1. Fork this repository
2. Import to Replit
3. Add `OPENAI_API_KEY` to Secrets
4. Run the project

### Option 2: Heroku
```bash
# Install Heroku CLI, then:
heroku create your-serendipity-ai
heroku config:set OPENAI_API_KEY=your_key_here
git push heroku main
```

### Option 3: Docker
```bash
docker build -t serendipity-ai .
docker run -p 8000:8000 --env-file .env serendipity-ai
```

### Option 4: Cloud Platforms
- **AWS**: Use Elastic Beanstalk or ECS
- **Google Cloud**: Use App Engine or Cloud Run  
- **Azure**: Use App Service or Container Instances

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

### Quick Contribution Guide

```bash
# 1. Fork the repository on GitHub
# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/Serendipity-AI.git

# 3. Create a feature branch
git checkout -b feature/amazing-enhancement

# 4. Make your changes and test
python -m pytest
python main.py  # Test locally

# 5. Commit and push
git add .
git commit -m "Add amazing enhancement"
git push origin feature/amazing-enhancement

# 6. Create a Pull Request on GitHub
```

### Ways to Contribute

- 🐛 **Bug Reports**: Found a bug? Open an issue!
- 💡 **Feature Requests**: Have an idea? We'd love to hear it!
- 📝 **Documentation**: Help improve our docs
- 🎨 **UI/UX**: Make the interface more beautiful
- 🔧 **Code**: Fix bugs, add features, optimize performance
- 🤖 **AI Training**: Help improve AI responses and personality

### AI-Powered Contributions
Use our Claude automation! Just create an issue with your idea and mention "claude" - our AI will help implement it automatically.

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📊 Project Stats

<div align="center">
  <img src="https://img.shields.io/github/stars/ESTITO-XP/Serendipity-AI?style=social" alt="Stars">
  <img src="https://img.shields.io/github/forks/ESTITO-XP/Serendipity-AI?style=social" alt="Forks">
  <img src="https://img.shields.io/github/watchers/ESTITO-XP/Serendipity-AI?style=social" alt="Watchers">
</div>

<div align="center">
  <img src="https://img.shields.io/github/issues/ESTITO-XP/Serendipity-AI" alt="Issues">
  <img src="https://img.shields.io/github/issues-pr/ESTITO-XP/Serendipity-AI" alt="Pull Requests">
  <img src="https://img.shields.io/github/last-commit/ESTITO-XP/Serendipity-AI" alt="Last Commit">
</div>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - Feel free to use, modify, and distribute!
```

---

## 🆘 Support

### Need Help?

- 📚 **Documentation**: Check our [docs](docs/) folder
- 💬 **Discussions**: Use GitHub Discussions for questions
- 🐛 **Bug Reports**: Open an issue with detailed information  
- 📧 **Email**: Contact the maintainers
- 🤖 **AI Help**: Create an issue mentioning "claude" for automated assistance!

### Community

- 🌟 **Star the repo** if you find it useful!
- 🍴 **Fork it** to customize for your needs
- 📢 **Share it** with others who might benefit
- 🤝 **Contribute** to make it even better

---

## 🙏 Acknowledgments

- 🤖 **OpenAI** for providing the GPT models
- 🤖 **Anthropic** for Claude AI automation capabilities  
- ⚡ **FastAPI** team for the excellent web framework
- 🐍 **Python** community for amazing ecosystem
- 🚀 **GitHub** for hosting and Actions platform
- ❤️ **Contributors** who make this project better

---

<div align="center">
  <h3>🌟 Made with ❤️ for AI enthusiasts everywhere 🌟</h3>
  <p><em>Spark delightful discoveries with Serendipity AI</em></p>
  
  **[⭐ Star this repository](https://github.com/ESTITO-XP/Serendipity-AI)** | **[🍴 Fork it](https://github.com/ESTITO-XP/Serendipity-AI/fork)** | **[📖 Documentation](docs/)**
</div>

---

<div align="center">
  <sub>Built with FastAPI • Powered by OpenAI • Enhanced by Claude • Deployed Everywhere</sub>
</div>
