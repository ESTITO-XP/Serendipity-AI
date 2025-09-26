# 🛠️ Installation — Serendipity AI

A creator-first workspace built for memory, modularity, and momentum.  
Designed by a solo founder for solo founders.

---

## 🔧 Requirements

- Python 3.10+
- Git
- pip or poetry
- Recommended: virtualenv
- Optional: FFmpeg (for voice/video features)

---

## 📦 Setup

```bash
git clone https://github.com/ESTITO-XP/Serendipity-AI.git
cd Serendipity-AI
pip install -r requirements.txt

🚀 Run Locally

uvicorn main:app --reload

Access at: http://localhost:8000

🧪 Dev Notes

app.py for modular ASGI entry

routes/ for chat, voice, image, video

utils/ for memory, layout, export logic

requirements.txt includes voice, image, and video support

Verified social links wired into layout logic

AI voiceover and video modules are experimental but  in full artifact form—I’ll match this clarity line for line.
