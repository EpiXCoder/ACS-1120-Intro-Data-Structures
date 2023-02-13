from flask import Flask
app = Flask(__name__)
from markov import Markov
import re
import random

@app.route('/')
def tweet_deploy():
    sample = 'yoga.txt'
    markov = Markov(sample)
    sentence = markov.generate_sentence()
    return f"<p>{sentence}</p>"
