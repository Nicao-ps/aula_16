from sqlalchemy import create_engine
from dotenv import load_dotenv
import pandas as pd
import numpy as np
import os

load_dotenv()

# variables:
host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')
database = os.getenv('DB_DATABASE')

# call engine:
engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')

# dataframe read and capture:
df_stock = pd.read_sql('tb_produtos', engine)
print(df_stock)

df_stock['TotalEstoque'] = df_stock['qtd']*df_stock['preco']

print(df_stock[['produto', 'TotalEstoque']])
print(f'\nTotal Geral de produtos: R$ {df_stock["TotalEstoque"].sum()}')

array_stock = np.array(df_stock['TotalEstoque'])
lenn = np.mean(array_stock)
mediann = np.median(array_stock)

print('Medidas de Tendência Central')
print(f'Média: {lenn:.2f}')
print(f'Mediana:{mediann:.2f}')
