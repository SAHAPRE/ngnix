from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There, how are you ? i am good, tell me about you..hello dear </h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
