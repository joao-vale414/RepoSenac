import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df_clientes = pd.read_csv("clientes.csv" , sep = ",", encoding = "latin1")
df_vendas   = pd.read_csv("vendas.csv"   , sep = ",", encoding = "latin1")
df_produtos = pd.read_csv("produtos.csv" , sep = ",", encoding = "latin1")

# Limpar e padronizar nomes
def clean_df(df):
    df = df.rename(columns = lambda x: x.strip().lower().replace(" ","_"))
    return df 

df_clientes = clean_df(df_clientes)
df_vendas   = clean_df(df_vendas)
df_produtos = clean_df(df_produtos)

# Base Unificada 
df = df_vendas.merge(df_clientes, on = "id_cliente").merge(df_produtos, on = "id_produto")

# Jovem < 18
# Adulto 18 ate 60 
# Idoso 60 + 

intervalo = [0, 18, 60, 120]
categoria = ["Jovem", "Adulto", "Idoso"]

df["faixa_etaria"] = pd.cut(df["idade"], bins = intervalo , labels = categoria, right = True)

mais_comprados_faixa_etaria_          = df.groupby (["faixa_etaria","id_produto"])       ["valor_total"]        .sum().sort_values (ascending = False)
frequencia_de_compras_por_canal       = df.groupby ("faixa_etaria")                      ["canal_aquisicao"]    .value_counts      (normalize = True)
ticket_medio_por_faixa_etaria         = df.groupby (["canal_aquisicao", "faixa_etaria"]) ["valor_total"]        .mean()
gasto_medio_faixa                     = df.groupby ("faixa_etaria")                      ["valor_total"]        .mean()
quantidade_media_produtos             = df.groupby("faixa_etaria")                       ["quantidade"]         .mean()

gasto_medio_faixa.plot(kind = "bar", title = "Gasto médio por faixa etária")
plt.ylabel("Valor médio")
plt.show()



