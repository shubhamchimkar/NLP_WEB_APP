# NLP Web App

A Flask-based web application that provides user authentication and integrates with NLP Cloud to offer Named Entity Recognition (NER), Sentiment Analysis, and Text Summarization services.

## Features

- **User Authentication**: Secure login and registration system with session management.
- **Named Entity Recognition (NER)**: Extract entities from text using NLP Cloud.
- **Sentiment Analysis**: Analyze sentiment in text, with optional target specification.
- **Text Summarization**: Summarize text in small, medium, or large sizes.
- **Responsive UI**: Clean, user-friendly interface with CSS styling.
- **Deployment Ready**: Configured for production deployment on platforms like Render.

## Prerequisites

- Python 3.8 or higher
- NLP Cloud API key (sign up at [nlpcloud.com](https://nlpcloud.com))

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd nlp-web-app
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory and set the following environment variables:

```env
NLPCLOUD_API_KEY=your_nlpcloud_api_key_here
SECRET_KEY=your_secret_key_here
```

- `NLPCLOUD_API_KEY`: Your NLP Cloud API key.
- `SECRET_KEY`: A secure random string for Flask session management.

Optional environment variables:
- `NLPCLOUD_MODEL`: Default model (default: finetuned-llama-3-70b)
- `NLPCLOUD_GPU`: Use GPU (default: True)

## Usage

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Access the app**:
   - Open http://127.0.0.1:5000 in your browser
   - Register a new account or login
   - Navigate to NER, Sentiment, or Summarization pages

## Deployment

This app is configured for deployment on Render:

1. Push your code to a Git repository (GitHub/GitLab).
2. Create a new Web Service on Render.
3. Connect your repository.
4. Set build command: `pip install -r requirements.txt`
5. Set start command: `gunicorn app:app`
6. Add environment variables in Render dashboard:
   - `NLPCLOUD_API_KEY`
   - `SECRET_KEY`
   - `PORT` (automatically set by Render)

## Project Structure

```
nlp-web-app/
├── app.py                 # Main Flask application
├── api.py                 # NLP Cloud API integration
├── db.py                  # User database management
├── requirements.txt       # Python dependencies
├── Procfile               # Render deployment configuration
├── .gitignore             # Git ignore rules
├── .env                   # Environment variables (not committed)
├── static/
│   └── style.css          # CSS styles
├── templates/
│   ├── base.html          # Base template
│   ├── login.html         # Login page
│   ├── register.html      # Registration page
│   ├── profile.html       # User profile
│   ├── ner.html           # NER interface
│   ├── sentiment.html     # Sentiment analysis interface
│   └── summarization.html  # Summarization interface
└── users.json             # User data (demo only)
```

## API Endpoints

- `GET /`: Login page
- `POST /perform_login`: User login
- `POST /perform_registeration`: User registration
- `GET /profile`: User profile (authenticated)
- `GET /ner`: NER page (authenticated)
- `POST /perform_ner`: Perform NER
- `GET /sentiment`: Sentiment page (authenticated)
- `POST /perform_sentiment`: Perform sentiment analysis
- `GET /summarization`: Summarization page (authenticated)
- `POST /perform_summarization`: Perform summarization
- `GET /logout`: Logout

## Security Notes

- User passwords are stored in plain text in `users.json` for demo purposes only.
- In production, use proper password hashing (e.g., with bcrypt).
- The `.env` file is ignored by git; never commit sensitive data.
- Rate limiting may apply based on your NLP Cloud plan.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`
3. Commit changes: `git commit -am 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

