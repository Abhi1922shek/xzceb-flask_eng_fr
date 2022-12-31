from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('Insert english text')
    # Write your code here
    translated_E2F = translator.english_to_french(textToTranslate)
    return translated_E2F

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('Insert french text')
    # Write your code here
    translated_F2E = translator.french_to_english(textToTranslate)
    return translated_F2E

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
