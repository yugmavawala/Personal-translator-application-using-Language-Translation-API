from flask import Flask, request, render_template
import re
import requests

app = Flask(__name__)

def check(language,output):
    url = "https://rapidapi.p.rapidapi.com/translateLanguage/translate"
    payload = "{\"target\": \""+language+"\",\"text\": \""+output+"\",\"type\": \"plain\"\r\n}"
    
    print(payload)
    headers = {
    'content-type': "application/json",
    'x-rapidapi-key': "5d797ab107mshe668f26bd044e64p1ffd34jsnf47bfa9a8ee4",
    'x-rapidapi-host': "language-translation.p.rapidapi.com"

    }
    response = requests.request("POST", url, data=payload, headers=headers)
    print(response.text)
    return response.json()['translatedText']

#home page
@app.route('/')
def home():
    return render_template('home.html')

#home page
@app.route('/translator')
def translator():
    return render_template('translator.html')

#translator page
@app.route('/translate',  methods=['POST'])
def translate():
    language=request.form['type']
    output = request.form['output']
    print(output)
    translated = check(language,output)
    return render_template('translate.html',translated=translated)

    
if __name__ == "__main__":
    app.run(debug=True)
    

