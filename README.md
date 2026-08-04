# GitHub Actions Practice

[![Docker Build and Push](https://github.com/AFarinha/github-actions-practice/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/AFarinha/github-actions-practice/actions/workflows/docker-publish.yml)

Small practice repository for GitHub Actions workflows.

The Docker workflow builds and publishes the Flask/Postgres Task API from Day 36.

## Docker Image

```bash
docker pull afarinha/github-actions-practice:latest
cp env.sample .env
APP_IMAGE=afarinha/github-actions-practice:latest docker compose -f docker-compose.hub.yml up -d
curl http://localhost:8081/health
```
