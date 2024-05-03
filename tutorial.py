from flask import Flask, redirect, url_for, render_template, request, jsonify
from prompts import prompts
app = Flask(__name__)
import random


@app.route("/")
def home():
    return render_template("index.html")

def return_prompt(button_id):
    if button_id in prompts:
        return random.choice(prompts[button_id])
    else:
        return "No prompts found for this button"

@app.route('/render_prompts', methods=['POST'])
def render_prompts():
    button_id = request.form['buttonId']
    prompt = return_prompt(button_id)
    return jsonify({'prompt': prompt})

if __name__ == "__main__":
    app.run(debug=True)