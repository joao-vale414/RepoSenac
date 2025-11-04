import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df_clientes  = pd.read_csv("clientes.csv"   , sep = ";", encoding = "latin1")
df_vendas    = pd.read_csv("vendas.csv"     , sep = ";", encoding = "latin1")
df_vendas1   = pd.read_csv("Vendas1.csv"    , sep = ";", encoding = "latin1")
df_vendas2   = pd.read_csv("Vendas2.csv"    , sep = ";", encoding = "latin1")
df_vendas3   = pd.read_csv("Vendas3.csv"    , sep = ";", encoding = "latin1")
df_produtos  = pd.read_csv("produtos.csv"   , sep = ";", encoding = "latin1")


# Limpar e padronizar nomes
def clean_df(df):
    df = df.rename(columns = lambda x: x.strip().lower().replace(" ","_"))
    return df 

df_clientes   = clean_df (df_clientes)
df_vendas     = clean_df (df_vendas)
df_vendas1    = clean_df (df_vendas1)
df_vendas2    = clean_df (df_vendas2)
df_vendas3    = clean_df (df_vendas3)
df_produtos   = clean_df (df_produtos)

# Base Unificada Vendas 
vendas = pd.concat([df_vendas,df_vendas1,df_vendas2,df_vendas3],ignore_index = True)

intervalo = [0, 18, 60, 120]
categoria = ["Jovem", "Adulto", "Idoso"]

df_clientes["faixa_etaria"] = pd.cut(df_clientes["idade"], bins = intervalo , labels = categoria, right = True)

'''mais_comprados_faixa                = vendas.groupby (["idade","id_produto"])        ["valor_total"]        .sum().sort_values (ascending = False)
frequencia_de_compras_por_canal       = vendas.groupby ("idade")                       ["canal_aquisicao"]    .value_counts      (normalize = True)
ticket_medio_por_idade                = vendas.groupby (["canal_aquisicao", "idade"])  ["valor_total"]        .mean()
gasto_medio                           = vendas.groupby ("idade")                       ["valor_total"]        .mean()
quantidade_media_produtos             = vendas.groupby ("idade")                       ["quantidade"]         .mean()'''