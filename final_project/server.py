from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french():
    text_to_translate_f = request.args.get('Hello')
    french_translation= language_translator.translate(text= text_to_translate_f, model_id="en-fr").get_result()
    return french_translation.get['translations'][0].get['translation']

@app.route("/french_to_english")
def french_to_english():
    text_to_translate_e = request.args.get('Bonjour')
    english_translation= language_translator.translate(text= text_to_translate_e, model_id="fr-en").get_result()
    return english_translation.get['translations'][0].get['translation']

@app.route("/index.html")
def renderIndexPage():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
