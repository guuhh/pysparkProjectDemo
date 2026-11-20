from IPython.display import display
import pandas as pd

dataset = [
    [0,0,0],
    [0,1,1],
    [1,0,1],
    [1,1,1]
]
columns = ["a","b","a_or_b"]
ordf = pd.DataFrame(dataset, columns = columns)
display(ordf)
ordf.to_csv('./ordf.csv',index=False)
read_data_active = pd.read_csv('./ordf.csv')
display(read_data_active)

json_array = [{'a':1,'b':2},{'a':3,'b':4},{'a':5,'b':6}]
df = pd.DataFrame(json_array)
df.to_json('./data/json_array.json', orient='records')
df.to_csv('./data/csv_array.csv')
df.to_excel('./data/excel_array.xlsx')

iris_array = [{'sepal_lenght': 'NaN', 'sepal_wight': 'NaN', 'petal_lenght': 'NaN', 'petal_wight': 0.2, 'encoded_target': 0 },
            {'sepal_lenght': 'NaN', 'sepal_wight': 3.0, 'petal_lenght': 1.4, 'petal_wight': 0.2, 'encoded_target': 0 },
            {'sepal_lenght': 5.0, 'sepal_wight': 3.6, 'petal_lenght': 1.4, 'petal_wight': 'NaN', 'encoded_target': 0 },
            {'sepal_lenght': 10.0, 'sepal_wight': 3.0, 'petal_lenght': 1.0, 'petal_wight': 0.3, 'encoded_target': 0 }]


iris_df = pd.DataFrame(iris_array)
iris_df.to_csv('./data/null_array.csv', index=False) # index=False remove "Unnamed: 0".
file_iris_df = pd.read_csv('./data/null_array.csv') # drop "Unnamed: 0" column when is reading the file with parameter ", index_col=0"
file_iris_df.info()
#localizando especificamente linhas com qualquer coluna nula
file_iris_df[file_iris_df.isna().any(axis=1)]

# lidando com dados nulos, substituição

# 1. opcao - substituir pela média da coluna
iris_df_mean = file_iris_df.fillna(file_iris_df.mean())

# 2. Substituir por zero
iris_df_zero = file_iris_df.fillna(0)

# 3. Substituir por um valor impossivel
iris_df_valores_impossiveis = file_iris_df.fillna(-999)

print("Mean:")
display(iris_df_mean)

print("Zero:")
display(iris_df_zero)

print("Impossible value (-999):")
display(iris_df_valores_impossiveis)

