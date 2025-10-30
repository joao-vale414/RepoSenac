import pandas as pd
import numpy as np 
import matplotlib.pyplot as pl 

df_atendimentos = pd.read_csv("atendimentos.csv", sep = ",", encoding = "latin1")
df_avaliacoes   = pd.read_csv("avaliacoes.csv"  , sep = ",", encoding = "latin1")
df_clientes     = pd.read_csv("clientes.csv"    , sep = ",", encoding = "latin1")
df_vendas       = pd.read_csv("vendas.csv"      , sep = ",", encoding = "latin1")
df_campanhas    = pd.read_csv("campanhas.csv"   , sep = ",", encoding = "latin1")
df_produtos     = pd.read_csv("produtos.csv"    , sep = ",", encoding = "latin1")

# Limpar df's / deixar padrão + aplicar nos df's usados
def clean_df(df):
    df = df.rename(columns = lambda x: x.strip().lower().replace(" ","_"))
    return df 

df_clientes = clean_df(df_clientes)
df_vendas   = clean_df(df_vendas)
df_produtos = clean_df(df_produtos)

df_vendas["data"] = pd.to_datetime(df_vendas["data"], format = "%d/%m/%Y")

print(df_vendas)
print(df_vendas.dtypes)

