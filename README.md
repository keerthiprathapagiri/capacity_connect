# Capacity Connect
A polished Flask prototype that measures understanding, not just completion.

## Run locally
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python scripts/seed.py
flask --app app run --debug
```
Open http://127.0.0.1:5000. Demo accounts: `admin@capacity.local`, `trainer@capacity.local`, `learner@capacity.local` (password `demo123`). SQLite is created automatically. Video uploads are stored under `static/uploads/videos`; transcripts can be entered manually without external API keys.

Features include role-aware auth and trainer approval, course/lecture/video workflow, event tracking and heatmap API, anonymous doubts, Socket.IO chat, competency/readiness services, notifications, matching, and seed data.
