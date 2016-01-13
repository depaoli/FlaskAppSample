#
# Just a demo app, mostly used by https://github.com/depaoli/FlaskAppServer
#
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
