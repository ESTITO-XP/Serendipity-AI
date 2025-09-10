# 🤖 Serendipity AI

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/1f068665-3422-4899-89fd-fae272b3bf4d" />

<div align="center">

![GitHub Stars](https://img.shields.io/github/stars/ESTITO-XP/Serendipity-AI?style=for-the-badge&logo=github&color=yellow)
![GitHub Forks](https://img.shields.io/github/forks/ESTITO-XP/Serendipity-AI?style=for-the-badge&logo=github&color=blue)
![GitHub Issues](https://img.shields.io/github/issues/ESTITO-XP/Serendipity-AI?style=for-the-badge&logo=github&color=red)
![License](https://img.shields.io/github/license/ESTITO-XP/Serendipity-AI?style=for-the-badge&color=green)

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.110.0-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

</div>

> **Your supportive AI companion for delightful discoveries**

*Discover the unexpected, explore new possibilities, and engage in meaningful conversations with an AI that truly cares about your journey.*

---

## ✨ What is Serendipity AI?

Serendipity AI isn't just another chatbot. It's your **supportive companion** designed to bring joy, inspiration, and serendipitous discoveries to every interaction. Whether you're brainstorming ideas, seeking guidance, or just want to explore fascinating topics, Serendipity is here to make every conversation delightful.

### 🎯 Core Philosophy
- **Supportive** → Always encouraging and understanding
- **Curious** → Genuine interest in your thoughts and ideas  
- **Creative** → Unique perspectives and innovative solutions
- **Empathetic** → Emotional intelligence in every response
- **Inspiring** → Helping you see new possibilities

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+ (3.9+ recommended)
- OpenAI API key ([Get one here](https://platform.openai.com/api-keys))

### 1️⃣ Clone & Setup
```bash
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI
pip install -r requirements.txt
```

### 2️⃣ Configure Environment
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-actual-key-here
```

### 3️⃣ Launch
```bash
python app.py
```

🎉 **Open http://localhost:8000** and start chatting!

---

## 💫 Features

### 🎨 **Beautiful Interface**
- Modern glassmorphism design with smooth animations
- Responsive layout that works on all devices
- Real-time typing indicators and message animations
- Dark/light mode friendly color scheme

### 🧠 **Intelligent Conversations**
- Powered by OpenAI's GPT-3.5-turbo
- Context-aware responses that remember your conversation
- Optimized prompting for supportive, engaging interactions
- Smart session management with conversation history

### ⚡ **Performance & Reliability**
- Fast FastAPI backend with async processing
- Comprehensive error handling and rate limiting
- Health monitoring and session management
- Production-ready architecture

### 🔒 **Security & Privacy**
- Environment-based configuration for API keys
- No data persistence (conversations stay private)
- CORS protection and input validation
- Secure secret management with .env files

---

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Frontend** | HTML5, CSS3, JavaScript | Beautiful, responsive chat interface |
| **Backend** | FastAPI + Python | High-performance async API server |
| **AI Engine** | OpenAI GPT-3.5-turbo | Natural language processing |
| **Configuration** | python-dotenv | Secure environment management |

---

## 📁 Project Structure

```
Serendipity-AI/
├── 📄 README.md              # You are here!
├── ⚖️ LICENSE.txt            # MIT License
├── 🔧 requirements.txt       # Python dependencies
├── 🌍 app.py                 # FastAPI backend server
├── 📁 static/
│   └── 🎨 index.html         # Chat interface
├── 🔐 .env.example           # Environment template
├── 🚫 .gitignore             # Git ignore rules
└── 🔑 .env                   # Your secrets (not in repo)
```

---

## 🎮 Usage Examples

### Start a Creative Session
```
👤 "Help me brainstorm ideas for a creative project"
🤖 "I'd love to help you explore some creative possibilities! What type of project are you thinking about? Are you drawn to..."
```

### Get Guidance
```
👤 "I'm feeling stuck on a problem, can you help?"
🤖 "I'm here to support you through this! Sometimes when we feel stuck, it helps to step back and look at the situation from a fresh angle..."
```

### Explore New Ideas
```
👤 "What's something interesting I should explore today?"
🤖 "What a wonderful question! Here are some serendipitous directions you might find intriguing..."
```

---

## 🚀 Deployment

### Local Development
```bash
python app.py
# Server runs on http://localhost:8000
```

### Production Deployment

#### Heroku
```bash
# Create Procfile
echo "web: uvicorn app:app --host=0.0.0.0 --port=\$PORT" > Procfile

# Deploy
heroku create your-serendipity-app
heroku config:set OPENAI_API_KEY=your-key-here
git push heroku main
```

#### Railway
```bash
# Install Railway CLI
npm install -g @railway/cli

# Deploy
railway login
railway new
railway add
railway up
```

#### Docker
```bash
# Build
docker build -t serendipity-ai .

# Run
docker run -p 8000:8000 -e OPENAI_API_KEY=your-key serendipity-ai
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Required | Description | Example |
|----------|----------|-------------|---------|
| `OPENAI_API_KEY` | ✅ Yes | Your OpenAI API key | `sk-proj-abc123...` |
| `PORT` | ❌ No | Server port (default: 8000) | `8000` |
| `LOG_LEVEL` | ❌ No | Logging level (default: info) | `info` |

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Serve chat interface |
| `/chat` | POST | Send message, get AI response |
| `/health` | GET | Health check |
| `/sessions/{id}/history` | GET | Get chat history |
| `/sessions/{id}` | DELETE | Clear session |

---

## 🎨 Customization

### Modify AI Personality
Edit the system prompt in `app.py`:
```python
system_message = {
    "role": "system", 
    "content": "You are [Your Custom AI Personality]..."
}
```

### Update Visual Design
Customize the interface in `static/index.html`:
- Colors: Modify CSS gradient variables
- Fonts: Update font-family declarations
- Layout: Adjust container dimensions and spacing

### Add Features
- File upload support
- Voice messages
- Custom chat themes
- User authentication
- Conversation export

---

## 🤝 Contributing

We love contributions! Here's how to get involved:

### 🐛 Found a Bug?
1. Check [existing issues](https://github.com/ESTITO-XP/Serendipity-AI/issues)
2. Create a new issue with details
3. Include steps to reproduce

### 💡 Have an Idea?
1. Open a [discussion](https://github.com/ESTITO-XP/Serendipity-AI/discussions)
2. Describe your feature idea
3. Let's collaborate on implementation

### 🔧 Want to Code?
1. Fork the repository
2. Create a feature branch: `git checkout -b amazing-feature`
3. Make your changes
4. Test thoroughly
5. Submit a pull request

---

## 📊 Roadmap

### 🎯 Version 1.1 (Coming Soon)
- [ ] Conversation export/import
- [ ] Custom AI personalities
- [ ] Improved mobile experience
- [ ] Rate limiting for production

### 🌟 Version 2.0 (Future)
- [ ] Voice message support
- [ ] Multi-language support
- [ ] Plugin system
- [ ] Advanced analytics

---

## 🏆 Inspiration

Serendipity AI was inspired by the belief that AI should be more than just a tool—it should be a **companion** that brings joy, support, and unexpected discoveries to our daily lives.

> *"The beautiful thing about serendipity is that it transforms ordinary moments into extraordinary discoveries."*

---

## 📞 Support & Community

### 💬 Get Help
- [📧 Email](mailto:hehehola1177@hotmail.com)
- [💭 Discord
](https://discord.com/users/1191348720227332248)
- [🐛 Issues](https://github.com/ESTITO-XP/Serendipity-AI/issues)
- [💬 Discussions](https://github.com/ESTITO-XP/Serendipity-AI/discussions)

### 🌟 Show Your Support
If Serendipity AI brought some joy to your day:
- **⭐ Star this repository**
- **🍴 Fork and customize for your needs**
- **📢 Share with friends who might enjoy it**
- **🤝 Contribute to make it even better**

---

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE.txt) file for details.

*Built with ❤️ by [ESTITO_XP](https://github.com/ESTITO-XP)*

---

<div align="center">

**[⭐ Star](https://github.com/ESTITO-XP/Serendipity-AI)  [🍴 Fork](https://github.com/ESTITO-XP/Serendipity-AI/fork)  [🐛 Issues](https://github.com/ESTITO-XP/Serendipity-AI/issues)  [💡 Discussions](https://github.com/ESTITO-XP/Serendipity-AI/discussions)**

*Made with serendipity in mind* ✨

</div>
