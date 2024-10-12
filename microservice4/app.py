from flask import Flask, jsonify
import random

app = Flask(__name__)

def generate_random(n1, n2, count=1):
    values = [random.randint(n1, n2) for _ in range(count)]
    return jsonify({'values': values})

@app.route('/')
def default():
    return generate_random(1, 100, 1)

@app.route('/generate-random/')
def no_params():
    return generate_random(1, 100, 1)

@app.route('/generate-random/<int:n1>/')
def one_param(n1):
    return generate_random(1, n1, 1)

@app.route('/generate-random/<int:n1>/<int:n2>/')
def two_params(n1, n2):
    return generate_random(n1, n2, 1)

@app.route('/generate-random/<int:n1>/<int:n2>/<int:count>/')
def three_params(n1, n2, count):
    return generate_random(n1, n2, count)

if __name__ == "__main__":
    app.run(debug=True)