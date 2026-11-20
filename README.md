# PySpark Project Demo

A small PySpark playground that reads the [Music & Mental Health survey](https://www.kaggle.com/datasets/catherinerasgaitis/mxmh-survey-results) dataset from Kaggle and explores it with Spark, either from a script or from Jupyter Notebook / JupyterLab.

## Prerequisites

| Tool | Version | Check |
|------|---------|-------|
| Python | 3.11+ | `python3 --version` |
| Java (JDK) | 17 (PySpark 3.5 also supports 8 and 11) | `java -version` |

On macOS with Homebrew:

```bash
brew install python@3.11
brew install openjdk@17
```

If `java -version` doesn't find Java after installing it, point `JAVA_HOME` at it:

```bash
export JAVA_HOME="$(/usr/libexec/java_home -v 17)"
```

## 1. Create and activate a virtual environment

From the project root:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Your prompt should now start with `(.venv)`. To leave the environment later, run `deactivate`.

## 2. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

This installs PySpark, pandas, Jupyter Notebook, JupyterLab and the other libraries the project uses.

## 3. (Optional) Download the dataset

The data is expected at `data/mxmh_survey_results.csv`. If it isn't there yet, download it with the Kaggle CLI (needs a Kaggle API token in `~/.kaggle/`):

```bash
pip install kaggle
mkdir -p data
kaggle datasets download -d catherinerasgaitis/mxmh-survey-results -p data --unzip
```

## 4. Start Jupyter

With the virtual environment active, start either interface:

```bash
# JupyterLab (recommended)
jupyter lab

# or the classic Jupyter Notebook
jupyter notebook
```

The browser opens at `http://localhost:8888`. Open `Untitled.ipynb`, or create a new notebook, and start a Spark session:

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("notebook-demo").getOrCreate()

df = spark.read.csv("data/mxmh_survey_results.csv", header=True, inferSchema=True)
df.show(5)
```

Stop the server with `Ctrl+C` in the terminal.

> **Tip:** if the notebook can't import `pyspark`, the kernel is probably using a different Python. Make sure you launched Jupyter from the activated `.venv`, or register the environment as a kernel and pick it in the UI:
>
> ```bash
> python -m ipykernel install --user --name pyspark-project --display-name "Python (pysparkProject)"
> ```

## Run the demo script

```bash
python kaggle_demo.py
# or
spark-submit kaggle_demo.py
```

## Project structure

```
.
├── data/                   # Kaggle dataset (mxmh_survey_results.csv)
├── kaggle_demo.py          # Reads the dataset with Spark and prints schema/row count
├── Untitled.ipynb          # Exploration notebook
├── activate-steps.md       # Personal setup notes
└── requirements.txt        # Python dependencies
```
