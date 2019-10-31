nfrom flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "code changed enjoy"

if __name__ == "__main__":
    application.run()
