from flask import Flask
import random

app = Flask(__name__)

@app.route('/generate_random/<int:n1>/<int:n2>/')
def generate_random(n1, n2):
  return str(random.randint(n1, n2))
