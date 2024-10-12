from flask import Flask, jsonify

import random

app = Flask(__name__)


@app.route('/generate-random/')
def no_params():
  return generate_random(1, 100)


@app.route('/')
def default():
  return generate_random(1, 100)


@app.route('/generate-random/<int:n1>/')
def one_param(n1):
  return generate_random(1, n1)


@app.route('/generate-random/<int:n1>/<int:n2>/')
def generate_random(n1, n2):
  return jsonify({'value': str(random.randint(n1, n2))})


if __name__ == "__main__":
  app.run(debug=True)
