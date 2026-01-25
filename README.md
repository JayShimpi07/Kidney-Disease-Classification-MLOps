# Kidney-Disease-Classification-MLflow-DVC


## Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/JayShimpi07/Kidney-Disease-Classification-MLOps.git
```

### STEP 01 - Create a conda environment after opening the repository

```bash
conda create -n kidney python=3.10 -y
```

```bash
conda activate kidney
```

### STEP 02 - Install the requirements
```bash
pip install -r requirements.txt
```

## MLflow Experiment Tracking

MLflow is used to track experiments, log metrics, parameters, artifacts, and models.

- 📘 [MLflow Documentation ↗](https://mlflow.org/docs/latest/index.html)
- 🎥 [MLflow Tutorial ↗](https://www.youtube.com/watch?v=qdcHHrsXA48)


### Run MLflow UI locally
```bash
mlflow ui
```

### Then open:
```bash
http://127.0.0.1:5000
```
### Remote Tracking with DagsHub

This project supports remote MLflow tracking using DagsHub.

### Step 1: Create a DagsHub account

🔗 https://dagshub.com/

### Step 2: Generate Access Token

Go to:
DagsHub → Settings → Tokens → Generate Token

### Export Environment Variables (Linux / Mac)
```bash
export MLFLOW_TRACKING_URI="https://dagshub.com/<YOUR_USERNAME>/<YOUR_REPO>.mlflow"
export MLFLOW_TRACKING_USERNAME="<YOUR_USERNAME>"
export MLFLOW_TRACKING_PASSWORD="<YOUR_ACCESS_TOKEN>"
```

### Set Environment Variables (Windows PowerShell)
```bash
$env:MLFLOW_TRACKING_URI="https://dagshub.com/<YOUR_USERNAME>/<YOUR_REPO>.mlflow"
$env:MLFLOW_TRACKING_USERNAME="<YOUR_USERNAME>"
$env:MLFLOW_TRACKING_PASSWORD="<YOUR_ACCESS_TOKEN>"
```

## DVC (Data Version Control)

This project uses **DVC** to manage and reproduce the complete ML pipeline stages (end-to-end training workflow).

### Why DVC?
- Tracks **data + model artifacts** efficiently without pushing large files to GitHub
- Helps create reproducible **ML pipelines**
- Supports orchestration using `dvc.yaml` stages (pipeline automation)

---

### 📌 Common DVC Commands

#### Initialize DVC
```bash
dvc init
```

#### Run the full pipeline
```bash
dvc repro
```

#### Visualize the pipeline DAG (Directed Acyclic Graph)
```bash
dvc dag
```
### Pipeline DAG Output
![Pipeline DAG Output](https://raw.githubusercontent.com/JayShimpi07/Kidney-Disease-Classification-MLOps/ce163a550259c3c8d9e97b0a64db9753a682480e/dvc_dag.png)

````md
```` 
## 🚀 AWS CI/CD Deployment with GitHub Actions (EC2 + ECR)

This project supports **automated deployment on AWS** using, **Docker**, **ECR (Elastic Container Registry)**, and **EC2 (Ubuntu Server)**.

---

### Deployment Workflow (How it works)

1. **Build Docker Image** from source code  
2. **Push Docker Image** to AWS **ECR**  
3. **Launch EC2 Instance** (Ubuntu)  
4. EC2 **pulls latest image** from ECR  
5. **Run Docker container** on EC2

---

## 1️⃣ Create IAM User (Deployment User)

Login to AWS Console → IAM → Users → Create user.

### Required Access
- **EC2 access** → to manage virtual machine
- **ECR access** → to push/pull Docker images

### Attach Policies
Attach these policies to the IAM user:

- `AmazonEC2ContainerRegistryFullAccess`
- `AmazonEC2FullAccess`

---

## 2️⃣ Create ECR Repository

AWS Console → ECR → Create repository

Example URI:
```bash
230153192159.dkr.ecr.ap-south-1.amazonaws.com/kidneyclassification
```
---

## 3️⃣ Create EC2 Instance (Ubuntu)

AWS Console → EC2 → Launch Instance
Choose: **Ubuntu**

---

## 4️⃣ Install Docker on EC2

SSH into EC2 and run the following commands:

### Optional:

```bash
sudo apt-get update -y
sudo apt-get upgrade -y
```

### Required:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

### Add ubuntu user to docker group:

```bash
sudo usermod -aG docker ubuntu
newgrp docker
```

---

## 5️⃣ Configure EC2 as Self Hosted GitHub Runner

Go to your GitHub repo:

`Settings → Actions → Runners → New self-hosted runner`

Choose OS: **Linux**

Run the commands shown by GitHub **one by one inside EC2 terminal**.

---

## 6️⃣ Setup GitHub Secrets

Go to:

`Repo Settings → Secrets and variables → Actions → New repository secret`

Add the following secrets:

```txt
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_REGION=us-east-1
AWS_ECR_LOGIN_URI=566373416292.dkr.ecr.us-east-1.amazonaws.com
ECR_REPOSITORY_NAME=simple-app
```

---

After this, whenever you push code to GitHub, the GitHub Actions pipeline will:

* Build Docker Image
* Push to ECR
* Deploy on EC2 automatically

```

If you want, I can also generate the **complete GitHub Actions YAML file** (`.github/workflows/main.yaml`) for this AWS CI/CD setup.
```
Ohhh this is already **solid level README** 🔥
Now you’re at the stage where we make it look like a **FINAL-YEAR / INDUSTRY PROJECT**.

You’ve written:
✔ MLflow
✔ DVC
✔ AWS CI/CD
✔ EC2 + ECR
✔ GitHub Actions

Now what’s missing is the **“Project Finish Touch” section** 👇
Add this **AFTER** your current content.

---

# 🌐 Live Deployment (Render)

The application is deployed on **Render Cloud Platform** for real-time inference.

🔗 **Live App:**
[https://deep-learning-kidney-disease.onrender.com](https://deep-learning-kidney-disease.onrender.com/)

### Render handles:

* Dependency installation
* Model loading
* Flask server via Gunicorn
* Automatic redeployment on GitHub push

---

# 🔁 CI/CD for Render Deployment

This project also supports **automatic deployment to Render** using GitHub integration.

Whenever you push code:

1. GitHub triggers deployment
2. Render pulls latest code
3. Builds environment
4. Deploys updated model & API

No manual server handling required.

---

# 🐳 Docker Support (Production Ready)

The project is fully Dockerized for portability and scalable deployment.

### Build Docker Image

```bash
docker build -t kidney-classifier .
```

### Run Container

```bash
docker run -p 8080:8080 kidney-classifier
```

---

# 🧠 Model Details

| Parameter     | Value                    |
| ------------- | ------------------------ |
| Architecture  | CNN                      |
| Input Size    | 224x224                  |
| Classes       | Normal / Tumor           |
| Loss Function | Categorical Crossentropy |
| Optimizer     | Adam                     |
| Framework     | TensorFlow / Keras       |

---

# 📊 Output Example

```json
{
  "prediction": "Tumor",
  "confidence": 92.45,
  "probabilities": {
    "Normal": 7.55,
    "Tumor": 92.45
  }
}
```

---

# 📂 Screenshots

### 🧾 Application Interface

![UI](assets/ui.png)

# 🧩 Complete System Flow

```
Data → DVC Pipeline → Model Training → MLflow Logging → Model Saving  
→ Flask API → Web UI → Docker → CI/CD → Cloud Deployment (Render + AWS)
```

---

# 🔮 Future Enhancements

* Grad-CAM for medical explainability
* Model optimization (TensorRT / ONNX)
* User authentication
* Database logging of predictions
* Multi-class disease detection

---

# 👨‍💻 Author

**Jay Shimpi**
AI & Data Science Engineer 🚀

---

Now your README shows:

🧠 AI
⚙ MLOps
☁ Cloud
🔄 CI/CD
🐳 Docker
📊 Tracking
📦 Pipelines

This is **resume + interview ready**.

---
