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

# How much we are collecting from our sales?
total_sales = df_stock['qtd']*df_stock['preco']
print('\nTotal das Vendas: '+'{:.2f}'.format(total_sales.sum()))

# In med, how much is being the value of our last sales?
array_total_sales = np.array(total_sales)
med_sales = np.mean(array_total_sales)
median_sales = np.median(array_total_sales)
print('Média das Vendas: '+'{:.2f}'.format(med_sales))
print('Mediana das Vendas: '+'{:.2f}'.format(median_sales))
