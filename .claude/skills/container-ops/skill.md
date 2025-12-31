## Skill: Containerization & Kubernetes Operations
## Description: Packaging applications and deploying to Kubernetes clusters.

docker_standards:
  - "Use Multi-stage builds to keep image size small (especially for Python/Next.js)."
  - "Use `python:3.13-slim` as the base image for backend."
  - "Always include a `.dockerignore` file."

kubernetes_manifests:
  - "Create separate manifests for Deployment, Service, and Ingress."
  - "Use ConfigMaps and Secrets for environment variables."
  - "Define resource limits (CPU/Memory) for all pods."

tools:
  - "Minikube (Local Dev)"
  - "Helm (Package Management)"
  - "kubectl (Cluster Management)"