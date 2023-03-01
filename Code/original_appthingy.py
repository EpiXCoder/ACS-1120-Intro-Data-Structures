"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, render_template
import re
import random


from sample import *

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    num_of_words = int(request.args.get("num"))
    sentence = sentence_gen(num_of_words)
    return f"<p>{sentence}</p>"
  



if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
