from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench(self, englishText):
    textToTranslate = request.args.get('textToTranslate')
    frenchText = self.translate(text=englishText, model_id='en-fr')
    return frenchText

@app.route("/frenchToEnglish")
def frenchToEnglish(self, frenchText):
    textToTranslate = request.args.get('textToTranslate')
    englishText = self.translate(text=englishText, model_id='en-fr')
    return englishText

@app.route("/")
def renderIndexPage():
    render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
