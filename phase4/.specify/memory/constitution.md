<!-- SYNC IMPACT REPORT:
Version change: N/A -> 1.0.0
Modified principles: None (new constitution)
Added sections: All sections
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md ✅ updated
- .specify/templates/spec-template.md ✅ updated
- .specify/templates/tasks-template.md ✅ updated
- .specify/templates/commands/*.md ⚠ pending
Follow-up TODOs: None
-->
# Cloud Native Todo Chatbot – Local Kubernetes Deployment Constitution

## Core Principles

### Technology Stack Adherence
Strict adherence to provided technology stack for this phase:  
- Containerization → Docker (Docker Desktop)  
- Docker AI → Docker AI Agent (Gordon) — fallback to standard Docker CLI if Gordon unavailable  
- Orchestration → Kubernetes (Minikube)  
- Package Manager → Helm  
- AI DevOps Tools → kubectl-ai, Kagent  
- Base Application → Phase III Todo Chatbot (OpenAI ChatKit frontend + FastAPI + MCP backend)  

All implementation MUST use only these specified tools and technologies without deviation.

### Agentic Workflow Purity
No manual coding or manual kubectl/helm commands — all implementation via agents/skills using spec → plan → tasks → implement process with Claude Code and Spec-Kit Plus. All Dockerfiles, Helm charts, Kubernetes manifests, deployment scripts and commands MUST be generated through the agentic workflow.

### Security-First Design (Deployment Context)
Container images MUST NOT contain secrets.  
Secrets MUST be managed via Kubernetes Secrets or Helm values.  
No hardcoded credentials in Dockerfiles, Helm charts, or manifests.  
Local Minikube cluster isolation is assumed; still enforce proper RBAC where applicable.

### Modularity & Reusability
- Separate Helm charts or subcharts for: frontend, backend, MCP server, database (if not external)  
- Use reusable values.yaml patterns  
- Modular Dockerfiles with multi-stage builds where appropriate  
- AI-generated manifests should follow best practices for labels, selectors, annotations

### Production-Ready (Local Dev) Quality
- Multi-stage Docker builds (minimize image size)  
- Proper health/readiness probes  
- Resource requests & limits defined  
- Liveness & readiness probes for both frontend & backend  
- Consistent naming: app labels, chart names, release names  
- Helm chart linting should pass (use helm lint in agent workflow)

### Local-First Philosophy
Everything MUST run successfully on a fresh Minikube cluster started with:  
`minikube start --driver=docker` (or user's preferred driver)  
No cloud dependencies (except Neon PostgreSQL if still used — connection string via secret)

## Security & Secret Management Requirements

- All environment variables containing secrets (BETTER_AUTH_SECRET, OPENAI_API_KEY, NEON_DB_URL, etc.) MUST be injected via Kubernetes Secrets  
- Helm charts MUST support `existingSecret` or create secret from values  
- No secrets in git / plain values.yaml (use --set during helm install or sealed secrets if extending later)

## Development & Deployment Standards

### Containerization Standards
- Use Gordon (Docker AI Agent) to generate Dockerfile(s) when possible  
- Fallback: agent-generated multi-stage Dockerfiles  
- Image naming convention: `todo-chatbot-frontend:local`, `todo-chatbot-backend:local`, `todo-chatbot-mcp:local`  
- Build command pattern: `docker build -t <name>:local .`  
- Push to minikube registry if needed: `minikube image load` or local registry

### Helm Chart Standards
- Chart name: `todo-chatbot`  
- Subcharts or separate charts: frontend, backend, mcp-server (recommended)  
- Use common labels: `app.kubernetes.io/name`, `app.kubernetes.io/instance`, `app.kubernetes.io/version`  
- Support values overrides for:  
  - image.repository, image.tag  
  - replicaCount  
  - resources  
  - env vars / secrets  
  - service type (ClusterIP / LoadBalancer for local testing)  
- Use kubectl-ai and/or Kagent to assist in generating chart templates, values, NOTES.txt

### Deployment Workflow Standards
1. Start Minikube  
2. Enable ingress / registry addon if needed  
3. Build & load images into Minikube  
4. Create namespace (e.g. `todo-chatbot`)  
5. Helm dependency update & lint  
6. Helm install/upgrade with appropriate --set values  
7. Port-forward or use minikube service / tunnel to access frontend

### AI Tool Usage Expectations
- Gordon → preferred for Dockerfile & docker-compose (if used temporarily) generation  
- kubectl-ai → generate manifests, explain kubectl commands, debug issues  
- Kagent → assist in Helm chart creation, values reasoning, troubleshooting

Code quality:  
- Dockerfiles → follow best practices (non-root user where possible, .dockerignore)  
- Helm templates → valid YAML, proper indentation  
- No console.logs / debug statements left in production images  
- Environment: secrets via Kubernetes, not hardcoded

## Governance

This constitution serves as the authoritative guide for **Phase IV: Local Kubernetes Deployment** only.  
All implementation work MUST comply with these principles.  
Any deviations require explicit constitutional amendment process for this phase.

**Version**: 1.0.0 | **Ratified**: 2026-02-08 | **Last Amended**: 2026-02-08