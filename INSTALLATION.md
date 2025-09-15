# 🚀 Installation Guide

Welcome to **Serendipity AI** — a solo-built, creator-powered workspace for modular writing, memory-powered chat, and bold branding.

---

## 📋 Prerequisites

Before you begin, make sure you have:

- **Python 3.10+**  
  ```bash
  python --version

Git

git --version

pip (comes with Python)

pip --version

OpenAI API KeyGet yours here

## 🛠️ Installation Steps

•Clone the Repository

git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI

•Create Virtual Environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

•Install Dependencies

pip install --upgrade pip
pip install -r requirements.txt

•Configure Environment

cp .env.example .env

Edit .env with your API key:

OPENAI_API_KEY=sk-your-key-here
APP_VERSION=8.0

## 🚦 Run the App

uvicorn main:app --reload

Visit: http://localhost:8000

## 🧪 Developer Setup (Optional)

pip install -r requirements-dev.txt
pre-commit install

Run with auto-reload:

uvicorn main:app --reload --host 0.0.0.0 --port 8000

## ✅ Health Check

curl http://localhost:8000/health

Expected response:

{
  "status": "healthy",
  "service": "Serendipity AI",
  "version": "8.0.0",
  "api_configured": true
}

## 🐛 Troubleshooting

•Missing Dependencies

source venv/bin/activate
pip install -r requirements.txt

•API Key Not Found

cat .env  # Check for OPENAI_API_KEY

•Port Already in Use

lsof -ti:8000 | xargs kill -9

## 🎯 What’s Next

•Explore the API: http://localhost:8000/docs

•Customize the AI: Edit system prompt in main.py

•Deploy to production: See README.md

•Contribute: Check CONTRIBUTING.md

## 📞 Support & Contact

-**[📧 Email](mailto:hehehola1177@hotmail.com)**

-**[💬 Discord](https://discord.com/users/1191348720227332248)**

-**[🐛 Issues](https://github.com/ESTITO-XP/Serendipity-AI/issues)**

-**[💡 Discussions](https://github.com/ESTITO-XP/Serendipity-AI/discussions)**

<div align="center">

 
Built by **[ESTITO XP](https://github.com/ESTITO-XP/)**
