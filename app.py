from flask import Flask,render_template,request,redirect

from db import Database
from api import ner as perform_ner_api, sentiment as perform_sentiment_api, summarization as perform_summarization_api

app = Flask(__name__)

dbo = Database()


@app.route('/')
def index():
    return render_template('login.html', show_nav=False)

@app.route('/register')
def register():
    return render_template('register.html', show_nav=False)

@app.route('/perform_registeration', methods=['POST'])
def perform_registeration():
    name = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')

    response = dbo.insert(name, email, password)
    if response:
        return render_template('login.html', message="User registered successfully, Please login", show_nav=False) 
    else:   
        return render_template('register.html', message="User already exists, Please try with different email", show_nav=False)
    
@app.route('/perform_login', methods=['POST'])
def perform_login():
    email = request.form.get('email')
    password = request.form.get('password')

    response = dbo.search(email, password)

    if response:
        return redirect('/profile')
    else:
        return render_template('login.html', message="Invalid Credentials, Please try again", show_nav=False)

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/ner')
def ner():
    return render_template('ner.html')

@app.route('/perform_ner', methods=['POST'])
def perform_ner():
    text = request.form.get('ner_text')
    # call the nlpcloud NER helper; optionally pass searched_entity
    searched_entity = request.form.get('searched_entity')
    try:
        entities = perform_ner_api(text, searched_entity=searched_entity if searched_entity else None)
    except Exception as e:
        # map specific errors to concise user-friendly messages
        msg = "An error occurred while performing NER."
        # rate-limit / quota exceeded -> concise message
        if hasattr(e, 'response') and getattr(e.response, 'status_code', None) == 429:
            msg = "Instance quota exceeded; please try again later."
        else:
            # generic fallback message
            msg = "NER failed; please try again later."
        # log full error server-side for debugging
        print('NER error:', repr(e))
        return render_template('ner.html', message=msg)

    return render_template('ner.html', message="NER performed successfully on the given text", entities=entities)

@app.route('/sentiment')
def sentiment():
    return render_template('sentiment.html')
@app.route('/perform_sentiment', methods=['POST'])
def perform_sentiment():
    text = request.form.get('sentiment_text')
    target = request.form.get('sentiment_target')
    try:
        result = perform_sentiment_api(text, target=target if target else None)
    except Exception as e:
        msg = "Sentiment analysis failed; please try again later."
        if hasattr(e, 'response') and getattr(e.response, 'status_code', None) == 429:
            msg = "Instance quota exceeded; please try again later."
        print('Sentiment error:', repr(e))
        return render_template('sentiment.html', message=msg)
    return render_template('sentiment.html', message="Sentiment performed", result=result)


@app.route('/summarization')
def summarization():
    return render_template('summarization.html')


@app.route('/perform_summarization', methods=['POST'])
def perform_summarization():
    text = request.form.get('summ_text')
    size = request.form.get('size') or 'small'
    try:
        result = perform_summarization_api(text, size=size)
    except Exception as e:
        msg = "Summarization failed; please try again later."
        if hasattr(e, 'response') and getattr(e.response, 'status_code', None) == 429:
            msg = "Instance quota exceeded; please try again later."
        print('Summarization error:', repr(e))
        return render_template('summarization.html', message=msg)
    return render_template('summarization.html', message="Summarization complete", result=result)
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
