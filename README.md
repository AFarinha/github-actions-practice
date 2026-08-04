# GitHub Actions Practice

[![Docker Build and Push](https://github.com/AFarinha/github-actions-practice/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/AFarinha/github-actions-practice/actions/workflows/docker-publish.yml)
[![PR Pipeline](https://github.com/AFarinha/github-actions-practice/actions/workflows/pr-pipeline.yml/badge.svg)](https://github.com/AFarinha/github-actions-practice/actions/workflows/pr-pipeline.yml)
[![Main Pipeline](https://github.com/AFarinha/github-actions-practice/actions/workflows/main-pipeline.yml/badge.svg)](https://github.com/AFarinha/github-actions-practice/actions/workflows/main-pipeline.yml)
[![Scheduled Health Check](https://github.com/AFarinha/github-actions-practice/actions/workflows/health-check.yml/badge.svg)](https://github.com/AFarinha/github-actions-practice/actions/workflows/health-check.yml)

Practice repository for a complete GitHub Actions CI/CD pipeline.

The pipeline tests the Flask/Postgres Task API from Day 36 on pull requests, publishes `latest` and commit-specific Docker tags after changes reach `main`, reports the production deployment target, and checks the published application every 12 hours.

## Pipeline

```text
Pull request -> build and test -> PR checks pass
Merge to main -> build and test -> Docker build and push -> production deployment
Every 12 hours -> start Postgres and application containers -> health check
```

## Docker Image

```bash
docker pull afarinha/github-actions-practice:latest
cp env.sample .env
APP_IMAGE=afarinha/github-actions-practice:latest docker compose -f docker-compose.hub.yml up -d
curl http://localhost:8081/health
```
