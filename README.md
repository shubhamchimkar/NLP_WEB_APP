# NLP_WEB_APP

A small Flask app demonstrating simple user registration/login and NLP features using NLP Cloud.

Features
- User registration/login backed by a JSON file (for demo only).
- NER (Named Entity Recognition) endpoint using NLP Cloud.
- Sentiment analysis endpoint using NLP Cloud (supports optional `target`).
- Summarization endpoint using NLP Cloud (size options).
- Simple CSS for improved layout.

Quick start
1. Create a virtualenv and install dependencies (the project uses Python 3.13+):

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # or `pip install nlpcloud flask`
```

2. Set your NLP Cloud API key and optional config in environment variables (recommended):

```bash
export NLPCLOUD_API_KEY="your_api_key_here"
export NLPCLOUD_MODEL="finetuned-llama-3-70b"
export NLPCLOUD_GPU="True"
```

3. Run the app:

```bash
python app.py
```

4. Open the app in your browser:
- http://127.0.0.1:5000/ — Login/Register
- http://127.0.0.1:5000/ner — NER form
- http://127.0.0.1:5000/sentiment — Sentiment form
- http://127.0.0.1:5000/summarization — Summarization form

Notes
- The app stores users in `users.json` for demo purposes. Do not use this in production.
- Keep your `NLPCLOUD_API_KEY` secret. Do not check it into git; .env is ignored by `.gitignore`.
- If the NLP Cloud service returns 429 Too Many Requests, you may be rate-limited. Upgrade your plan or use a mock mode (not included).

Next steps
- Improve security: password hashing, input validation, and session management.
- Replace JSON file with a proper DB (SQLite/Postgres).
- Add mock/offline mode for NLP testing.

