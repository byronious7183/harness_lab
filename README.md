# Harness Lab App

A small Flask app for the Harness Sales Engineer candidate lab.

## Endpoints

| Path | Description |
|------|-------------|
| `/` | Greeting and app version |
| `/health` | Health check (used by Kubernetes probes) |
| `/version` | Returns `APP_VERSION` (handy for telling canary from stable) |
| `/add?a=2&b=3` | Adds two numbers |

## Run locally

```bash
pip install -r requirements.txt
pytest
python app.py          # http://localhost:5000
```

## Build and run with Docker

```bash
docker build -t harness-lab-app .
docker run -p 5000:5000 harness-lab-app
```

## Kubernetes

Manifests are in `k8s/`. Replace `YOUR_DOCKERHUB_USERNAME` in `k8s/deployment.yaml`
with your DockerHub username before deploying.
