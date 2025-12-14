# 🚀 Rick & Morty DevOps Exercise

This repository contains a **complete end-to-end DevOps solution** for the **Rick & Morty API exercise**, including application logic, containerization, Kubernetes deployment, Helm chart packaging, and CI/CD automation.

The project was built as part of a **DevOps Engineer home assignment** and demonstrates **real-world DevOps best practices**.

---

## 📌 Project Overview

The application:

- Queries the **Rick & Morty public API**
- Filters characters that are:
  - **Species:** Human  
  - **Status:** Alive  
  - **Origin:** Earth (all Earth variants)
- Stores the results in a **CSV file**
- Exposes a **REST API** to fetch the data
- Includes a **healthcheck endpoint**

The solution is delivered with:

- 🐳 Docker  
- ☸️ Kubernetes (YAML)  
- ⎈ Helm chart  
- 🔁 GitHub Actions CI/CD pipeline  

---

## 🧱 Architecture

```
Client
  |
  | HTTP
  v
Ingress (NGINX)
  |
Service (ClusterIP)
  |
Deployment (2 replicas)
  |
Flask Application
  |
Rick & Morty Public API
```

---

## 🚀 Application Endpoints

| Endpoint        | Description                                      |
|-----------------|--------------------------------------------------|
| `/healthcheck`  | Health status of the application                 |
| `/characters`   | Returns filtered Rick & Morty characters as JSON |

---

## 🧠 Application Logic

### Filtering Rules
- `species == "Human"`
- `status == "Alive"`
- `origin.name.startswith("Earth")`

### CSV Output Fields
- `name`
- `location`
- `image`

---

## 🐳 Docker

### Build Image
```bash
docker build -t rick-morty:1.0 .
```

### Run Container
```bash
docker run -p 5000:5000 rick-morty:1.0
```

### Test
```bash
curl http://localhost:5000/healthcheck
curl http://localhost:5000/characters
```

---

## ☸️ Kubernetes (YAML)

Kubernetes manifests are located in the `yamls/` directory.

### Deploy
```bash
kubectl apply -f yamls/
```

### Verify
```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

### Access
```bash
curl http://rick-morty.local/healthcheck
```

---

## ⎈ Helm Chart

The application is packaged as a **Helm chart** for reusable and configurable deployments.

### Helm Structure
```
helm/rick-morty/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    └── ingress.yaml
```

### Install
```bash
helm install rick-morty ./helm/rick-morty
```

### Upgrade
```bash
helm upgrade rick-morty ./helm/rick-morty
```

### Uninstall
```bash
helm uninstall rick-morty
```

---

## ⚙️ Configuration (`values.yaml`)

Key configurable values:

- Replica count
- Docker image & tag
- Service ports
- Ingress host

### Example
```yaml
replicaCount: 2

image:
  repository: rick-morty
  tag: "1.0"

ingress:
  enabled: true
  host: rick-morty.local
```

---

## 🔁 CI/CD — GitHub Actions

A complete **CI/CD pipeline** is implemented using **GitHub Actions**.

### Pipeline Steps
1. Checkout repository  
2. Build Docker image  
3. Create Kubernetes cluster (KinD)  
4. Load Docker image into cluster  
5. Install NGINX Ingress  
6. Deploy application using **Helm**  
7. Test `/healthcheck` endpoint  
8. Test `/characters` endpoint  

### Workflow File
```
.github/workflows/ci.yaml
```

### Triggered On
- Push to `main`
- Pull requests

---

## 🧪 Automated Tests

The CI pipeline validates:
- Application availability
- Healthcheck endpoint
- Characters endpoint returns real data

---

## 🧹 Cleanup

### Remove Helm Deployment
```bash
helm uninstall rick-morty
```

### Stop Local Cluster
```bash
minikube stop
```

---

## 📦 Technologies Used

- Python (Flask)
- Rick & Morty REST API
- Docker
- Kubernetes
- Helm
- GitHub Actions
- Minikube / KinD

---

## 👤 Author

**Tareq Suliman**  
GitHub: https://github.com/zDR34M

---

## ✅ Status

✔ Core requirements completed  
✔ Docker bonus completed  
✔ Kubernetes bonus completed  
✔ Helm bonus completed  
✔ GitHub Actions bonus completed  
