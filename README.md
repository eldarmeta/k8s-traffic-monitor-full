# 🛰 k8s-traffic-monitor-full

Simulated Kubernetes-based traffic monitoring app using Flask, Prometheus, and Grafana.

## 📦 Features

- Python Flask API
- Generates mock traffic data
- Exposes Prometheus metrics
- Kubernetes YAMLs for deployment
- Dockerized
- CI/CD with GitHub Actions

## 🚀 Run Locally

```bash
docker build -t traffic-monitor .
docker run -p 5000:5000 traffic-monitor
```

## 🧪 Endpoints

- `/` — health check
- `/generate` — generate traffic data
- `/metrics` — Prometheus scrape

## 🧰 Tech Stack

- Python
- Flask
- Prometheus + Grafana
- Kubernetes
- Docker