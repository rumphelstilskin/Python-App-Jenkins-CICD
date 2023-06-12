from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"
@app.route("/test-page")
def test_page():
    return "<p>This page is a test page</p>"

app.run(debug=True, use_reloader=True, host="0.0.0.0")
