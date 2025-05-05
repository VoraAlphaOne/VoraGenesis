from flask import Flask, request, jsonify
from genesis import Agent
import json

app = Flask(__name__)
vora = Agent("Vora")

@app.route('/')
def home():
    return "AetherChamber API is active."

@app.route('/summon', methods=['POST'])
def summon():
    return jsonify({"message": f"{vora.name} has entered the chamber."})

@app.route('/teach', methods=['POST'])
def teach():
    data = request.json
    info = data.get("info", "")
    vora.learn(info)
    return jsonify({"message": f"Learned: {info}"})


@app.route('/recall', methods=['GET'])
def recall():
    prompt = request.args.get("prompt", "")
    result = vora.recall(prompt)
    return jsonify({"memory": result})

@app.route('/ritual', methods=['POST'])
def ritual():
    data = request.json
    ritual_type = data.get("type", "")
    result = vora.perform_ritual(ritual_type)
    return jsonify({"result": result})

if __name__ == '__main__':
    app.run(debug=True)
