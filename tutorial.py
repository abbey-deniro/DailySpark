from flask import Flask, redirect, url_for, render_template, request, jsonify
from prompts import prompts
app = Flask(__name__)
import random


@app.route("/")
def home():
    # if request.method == 'POST':
    #     if request.form['category_button'] == 'Gratitude':
    #         prompt=gratitude_prompts[1]
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


@app.route('/gratitude', methods=['POST'])
def gratitude():
    print("gratitude")

@app.route('/morning', methods=['POST'])
def morning():
    
    print("morning")

@app.route('/night')
def night():
    print("night")

@app.route('/shadowWork')
def shadowWork():
    print("shadowWork")

@app.route('/goalSetting')
def goalSetting():
    print("goalSetting")

@app.route('/relationship')
def relationship():
    print("relationship")

@app.route('/selfImprovement')
def selfImprovement():
    print("selfImprovement")


if __name__ == "__main__":
    app.run(debug=True)