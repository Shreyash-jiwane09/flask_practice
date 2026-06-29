from flask import Flask
"""
It creates an instance of the Flask class,
which will be your WSGI(Web Server Gateway Interface) application.
"""

#WSGI application 
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/index")
def home():
    return "<html><H1>This is the Welcome page! Simple Web page</H1></html> "


if __name__ == "__main__":
    app.run(debug=True)