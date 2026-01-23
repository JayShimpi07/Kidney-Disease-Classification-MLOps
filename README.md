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

