from flask import Flask, jsonify, request

import psutil
import datetime
import socket
import os
import logging
from dotenv import load_dotenv
from openai import OpenAI


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

# ---------- AI Analysis Endpoint ----------
@app.route("/ai-analysis")
def ai_analysis():
    load_dotenv()
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url="https://generativelanguage.googleapis.com/v1beta/"
    )
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    prompt = f"""
    CPU usage is {cpu}% and memory usage is {memory}%.
    Analyze the system health and suggest improvements. Answer only 2-3 sentences. If the system is healthy, say "System is healthy". If there are issues, provide specific recommendations to optimize performance.
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"system","content":"You are a helpful assistant."},
                  {"role":"user","content":prompt}]
    )

    return response.choices[0].message.content

# ---------- AI Question Endpoint ----------
@app.route("/ask-ai")
def ask_ai():
    load_dotenv()
    client = OpenAI(
        api_key=os.getenv("GEMINI_API_KEY"),
        base_url = "https://generativelanguage.googleapis.com/v1beta"
    )
    question = request.args.get("q", "Why is CPU usage high and how can I optimize it?")
    cpu = psutil.cpu_percent()
    memory = psutil.virtual_memory().percent

    prompt = f"""
    System CPU={cpu}% memory={memory}%.
    Question: {question} 
    answer only 2-3 sentences. use simple language and provide actionable advice. If the question is not related to system performance, politely decline and ask for a relevant question. 
    """

    response = client.chat.completions.create(
        model="gemini-2.5-flash",
        messages=[{"role":"system","content":"You are a helpful assistant."},
                  {"role":"user","content":prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
