from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! Version 3 code changed"

if __name__ == "__main__":
    application.run()
