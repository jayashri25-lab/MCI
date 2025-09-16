from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder="../frontend/build", static_url_path="/")

@app.route("/api/hello")
def hello():
    return jsonify(message="Hello from Flask!")

@app.route("/")
def index():
    return send_from_directory(app.static_folder, "index.html")

if __name__ == "__main__":
    app.run(debug=True)
