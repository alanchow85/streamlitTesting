"""app.py"""

from flask import Flask

app = Flask(__name__)

@app.rout("/")
def index():
    return "Congrats, it is a web app!"

if __name__ == "__main__":
    app.run()
