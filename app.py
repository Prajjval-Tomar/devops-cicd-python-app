from flask import Flask, jsonify
import psutil
import datetime
import socket
import os
import logging
from pythonjsonlogger import jsonlogger
from prometheus_client import Counter, generate_latest
app = Flask(__name__)


# ---------- Logging Setup ----------
logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()

logHandler.setFormatter(formatter)
logger.addHandler(logHandler)
logger.setLevel(logging.INFO)

# ---------- Metrics ----------
REQUEST_COUNT = Counter("app_requests_total", "Total API Requests")

# ---------- Environment ----------
APP_VERSION = os.getenv("APP_VERSION", "1.0")

# ---------- Middleware ----------
@app.before_request
def log_request():
    logger.info("API request received")
    
# ---------- Routes ----------
# ---------- API Endpoints ----------
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
