import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df_clientes   = pd.read_csv("clientes.csv"          , sep = ",", encoding = "utf-8-sig")
df_vendas     = pd.read_csv("vendas.csv"            , sep = ";", encoding = "utf-8-sig")
df_vendas1    = pd.read_csv("Vendas1.csv"           , sep = ";", encoding = "utf-8-sig")
df_vendas2    = pd.read_csv("Vendas2.csv"           , sep = ";", encoding = "utf-8-sig")
df_vendas3    = pd.read_csv("Vendas3.csv"           , sep = ";", encoding = "utf-8-sig")
df_produtos   = pd.read_csv("produtos.csv"          , sep = ",", encoding = "utf-8-sig")
df_produto1   = pd.read_csv("Produto adicional.csv" , sep = ",", encoding = "utf-8-sig")

# Remover qualquer coluna com BOM ou cabeçalho 
for df in [df_vendas, df_vendas1, df_vendas2, df_vendas3]:
    df.drop(df.columns[df.columns.str.contains("ï»¿|ID_Venda,ID_Cliente")], axis=1, inplace=True)

# Base Unificada Vendas 
vendas   = pd.concat([df_vendas,df_vendas1,df_vendas2,df_vendas3] ,ignore_index = True)
produtos = pd.concat([df_produto1,df_produtos]                    ,ignore_index = True)

# Limpar e padronizar nomes
def clean_df(df):
    df = df.rename(columns = lambda x: x.strip().lower().replace(" ","_"))
    return df 

df_clientes   = clean_df (df_clientes)
vendas        = clean_df (vendas)
produtos      = clean_df (produtos)

def faixa_etaria(idade):
    if idade <= 18:
        return "Jovem"
    elif idade > 18 and idade <= 60:
        return "Adulto"
    else:
        return "Idoso"

df_clientes["faixa_etaria"] = df_clientes["idade"].apply(faixa_etaria)

vendas = vendas.merge(df_clientes[["id_cliente", "faixa_etaria"]], on = "id_cliente", how = "left")

mais_comprados_faixa                = vendas.groupby (["faixa_etaria","id_produto"])   ["valor_total"]        .sum().sort_values (ascending = False)
frequencia_de_compras_por_canal     = vendas.groupby ("faixa_etaria")                  ["canal"]              .value_counts      (normalize = True)
ticket_medio_por_idade              = vendas.groupby (["canal", "faixa_etaria"])       ["valor_total"]        .mean()
gasto_medio                         = vendas.groupby ("faixa_etaria")                  ["valor_total"]        .mean()
quantidade_media_produtos           = vendas.groupby ("faixa_etaria")                  ["quantidade"]         .mean()

mais_comprados_faixa  = mais_comprados_faixa             .reset_index()
frequencia_canal      = frequencia_de_compras_por_canal  .reset_index()
ticket_medio          = ticket_medio_por_idade           .reset_index()
gasto_medio           = gasto_medio                      .reset_index()
quantidade_media      = quantidade_media_produtos        .reset_index()

mais_comprados_faixa .to_csv      ("mais_comprados_faixa.csv" , index = False, encoding = "utf-8-sig")
frequencia_canal     .to_csv      ("frequencia_canal.csv"     , index = False, encoding = "utf-8-sig")
ticket_medio         .to_csv      ("ticket_medio.csv"         , index = False, encoding = "utf-8-sig")
gasto_medio          .to_csv      ("gasto_medio.csv"          , index = False, encoding = "utf-8-sig")
quantidade_media     .to_csv      ("quantidade_media.csv"     , index = False, encoding = "utf-8-sig")


