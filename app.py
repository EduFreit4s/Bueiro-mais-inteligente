import json

from flask import Flask, render_template, redirect, request, jsonify
from flask_socketio import SocketIO, send, emit
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app)
CORS(app)
dados = ""


@app.route("/")
def rota_inicial():
    return render_template("index.html")

if __name__ == "__main__":
    app.run("0.0.0.0",port=8080)

@app.route("/upload", method = ["POST"])
def rota_upload():
    mensagem = request.get_json()
    return "200"
    