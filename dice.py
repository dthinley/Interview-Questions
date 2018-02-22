from flask import Flask, jsonify
app = Flask(__name__)

import json
import random

@app.route('/dice.json')
def roll_dice():
    """return json result of two dice rolls"""
    dice = [random.choice(range(1, 6)), random.choice(range(1, 6))]
    return jsonify(dice=dice)


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
