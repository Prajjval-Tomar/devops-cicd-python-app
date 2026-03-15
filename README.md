# DevOps CI/CD Python Monitoring App 🚀

A containerized DevOps monitoring API built with Python and Flask, automated using a CI/CD pipeline with GitHub Actions, and distributed through Docker Hub.

This project demonstrates real-world DevOps practices including:

CI/CD pipeline automation

Docker containerization

Container registry publishing

Automated testing

Monitoring endpoints

Project Architecture
Developer
   │
   ▼
GitHub Repository
   │
   ▼
GitHub Actions CI/CD Pipeline
   │
   ├── Run Tests
   ├── Build Docker Image
   └── Push Image to Docker Hub
   │
   ▼
Docker Container Deployment
Tech Stack
Technology Purpose
Python Application logic
Flask REST API framework
Docker Containerization
GitHub Actions CI/CD automation
Docker Hub Container registry
PyTest Automated testing
psutil System monitoring metrics
Features

DevOps CI/CD pipeline using GitHub Actions

Docker containerized Python application

Automatic Docker image build and push

Health monitoring API endpoints

System metrics monitoring (CPU & Memory)

Containerized deployment ready

API Endpoints
Service Status
GET /

Response:

DevOps Monitoring API Running 🚀
Health Check
GET /health

Example Response

{
  "status": "healthy",
  "service": "devops-cicd-app"
}
System Metrics
GET /system

Example Response

{
  "cpu_usage": 15.2,
  "memory_usage": 42.5
}
Server Time
GET /time
Container Info
GET /info
Run the Project Locally
Clone the Repository
git clone <https://github.com/Prajjval-Tomar/devops-cicd-python-app.git>
cd devops-cicd-python-app
Run Using Docker

Build Docker Image

docker build -t devops-demo .

Run Container

docker run -p 5000:5000 devops-demo

Open browser:

<http://localhost:5000>
Pull Image from Docker Hub
docker pull prajjvaltomar/devops-demo-app

Run container:

docker run -p 5000:5000 prajjvaltomar/devops-demo-app
CI/CD Pipeline

The project uses GitHub Actions for continuous integration and deployment.

Pipeline Steps:

Code pushed to GitHub

Install dependencies

Run automated tests

Build Docker image

Push image to Docker Hub

Workflow file:

.github/workflows/ci-cd.yml
Project Structure
devops-cicd-python-app
│
├── app.py
├── requirements.txt
├── Dockerfile
├── test_app.py
│
├── .github
│   └── workflows
│       └── ci-cd.yml
│
└── README.md
Future Improvements

Kubernetes deployment

Prometheus monitoring

Grafana dashboards

Load balancing

Production WSGI server (Gunicorn)

Author

Prajjval Tomar

LinkedIn
<https://linkedin.com/in/prajjval-tomar>

GitHub
<https://github.com/Prajjval-Tomar>

License

This project is for educational and DevOps practice purposes.

## All API End Ponts

health
info
metrics
system
time
ask-ai
ai-analysis
