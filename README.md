# kidney-Disease-Classification_DL

## Workflows
1. Update config.yaml
2. Update secrets.yaml [optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py

# How to run

## steps

Clone the repository

`bash https://github.com/shlok-dadhich/kidney-Disease-Classification_DL `

### Step 1 : Create a conda environment after opening the repository

```bash
conda create -n cnncls python=3.8 -y
```

```bash
conda activate cnncls
```

### Step 2 : install the requirements

```bash
pip install -r requirenents.txt
```
### dagshub
[dagshub](https://dagshub.com/)\
MLFLOW_TRACKING_URI = https://dagshub.com/shlok-dadhich/kidney-Disease-Classification_DL.mlflow\
MLFLOW_TRACKING_USERNAME = 'shlok-dadhich'\
MLFLOW_TRACKING_PASSWORD = '585f29336580f8c0e6967749768d16c35060e4ca'

RUn this to export as env variables:
```bash
export MLFLOW_TRACKING_URI = https://dagshub.com/shlok-dadhich/kidney-Disease-Classification_DL.mlflow
export MLFLOW_TRACKING_USERNAME = 'shlok-dadhich'
export MLFLOW_TRACKING_PASSWORD = '585f29336580f8c0e6967749768d16c35060e4ca'
```

