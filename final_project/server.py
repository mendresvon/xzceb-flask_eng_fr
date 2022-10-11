from machinetranslation import translator
from flask import Flask, render_template, request
import json
import machinetranslation

app = Flask("Web Translator", template_folder="templates")


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get("textToTranslate")
    # Write your code here
    french_translation = englishToFrench(textToTranslate)
    return f"Translated text to French SUCCESS\nEnglish: {textToTranslate}\nFrench: {french_translation}"


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get("textToTranslate")
    # Write your code here
    english_translation = frenchToEnglish(textToTranslate)
    return f"Translated text to English SUCCESS\nFrench: {textToTranslate}\nEnglish: {english_translation}"


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
