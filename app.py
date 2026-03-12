from flask import Flask, jsonify
import psutil
import datetime
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return "DevOps Monitoring API Running 🚀"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "service": "devops-cicd-app"
    })

@app.route("/system")
def system():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    return jsonify({
        "cpu_usage": cpu,
        "memory_usage": memory
    })

@app.route("/time")
def time():
    return jsonify({
        "server_time": str(datetime.datetime.now())
    })

@app.route("/info")
def info():
    return jsonify({
        "hostname": socket.gethostname(),
        "platform": "Docker Container"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)