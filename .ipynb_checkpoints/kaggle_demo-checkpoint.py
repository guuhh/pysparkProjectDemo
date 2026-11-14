from pyspark.sql import SparkSession
import os

#pysparkProject source .venv/bin/activate

# Inicializa a sessão Spark
spark = SparkSession.builder.appName("Kaggle-demo").getOrCreate()

#userdata.get('KAGGLE_TOKEN')
#from pathlib import Path
#token = (Path.home() / ".kaggle" / "access_token").read_text().strip()

path = os.path.expanduser("~/.kaggle/access_token")
with open(path) as f:
    token = f.read().strip()

# Como o arquivo já foi baixado anteriormente, podemos lê-lo diretamente
csv_path = os.path.expanduser("~/pysparkProject/data/mxmh_survey_results.csv")
df = spark.read.csv(csv_path, header=True, inferSchema=True)
 
# Exibe os dados e informações 
df.show(10)
df.printSchema()
print(f"Total de registros: {df.count()}")