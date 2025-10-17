# 🛠️ Installation Guide — Serendipity AI

<img width="1920" height="1080" alt="Image" src="https://github.com/user-attachments/assets/e09e4981-c20f-4844-8945-1d64ec9d79c9" />

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
