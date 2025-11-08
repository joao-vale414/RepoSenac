import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

df_clientes   = pd.read_csv("clientes.csv"           , sep = ",")
df_vendas     = pd.read_csv("vendas.csv"             , sep = ",")
df_vendas1    = pd.read_csv("venda 1.csv"            , sep = ",")
df_vendas2    = pd.read_csv("venda 2.csv"            , sep = ",")
df_vendas3    = pd.read_csv("venda 3.csv"            , sep = ",")
df_produtos   = pd.read_csv("produtos.csv"           , sep = ",")
df_produto1   = pd.read_csv("Produto adicional.csv"  , sep = ",")

# Remover qualquer coluna com BOM ou cabeçalho 
'''for df in [df_vendas, df_vendas1, df_vendas2, df_vendas3]:
    df.drop(df.columns[df.columns.str.contains("ï»¿|ID_Venda,ID_Cliente")], axis = 1, inplace = True)'''

# Base Unificada Vendas 
vendas_atualizado   = pd.concat([df_vendas,df_vendas1,df_vendas2,df_vendas3] ,ignore_index = True)
produtos_atualizado = pd.concat([df_produto1,df_produtos]                    ,ignore_index = True)
 
def faixa_etaria(idade):
    if idade <= 18:
        return "Jovem"
    elif idade > 18 and idade <= 60:
        return "Adulto"
    else:
        return "Idoso"

df_clientes["faixa_etaria"] = df_clientes["Idade"].apply(faixa_etaria)


vendas_atualizado = pd.merge(vendas_atualizado, df_clientes[["ID_Cliente","faixa_etaria"]], on = "ID_Cliente", how = "left")

vendas_atualizado["Data"] =vendas_atualizado["Data"].str.replace("00:00:00"," ")

mais_comprados_faixa_1                 = vendas_atualizado.groupby (["faixa_etaria","ID_Produto"])   ["Valor_Total"]        .sum().sort_values (ascending = False) .reset_index()
frequencia_de_compras_por_canal_1      = vendas_atualizado.groupby ("faixa_etaria")                  ["Canal"]              .value_counts      (normalize = True)  .reset_index()
ticket_medio_por_idade_1               = vendas_atualizado.groupby (["Canal", "faixa_etaria"])       ["Valor_Total"]        .mean()                                .reset_index()
gasto_medio_1                          = vendas_atualizado.groupby ("faixa_etaria")                  ["Valor_Total"]        .mean()                                .reset_index()
quantidade_media_produtos_1            = vendas_atualizado.groupby ("faixa_etaria")                  ["Quantidade"]         .mean()                                .reset_index()
                          
mais_comprados_faixa_1              .to_csv  ("mais_comprados.csv" , index = False, encoding = "utf-8-sig")
frequencia_de_compras_por_canal_1   .to_csv  ("frequencia_c.csv"     , index = False, encoding = "utf-8-sig")
ticket_medio_por_idade_1            .to_csv  ("ticket_m.csv"         , index = False, encoding = "utf-8-sig")
gasto_medio_1                       .to_csv  ("gasto_m.csv"          , index = False, encoding = "utf-8-sig")
quantidade_media_produtos_1         .to_csv  ("quantidade_m.csv"     , index = False, encoding = "utf-8-sig")
vendas_atualizado                   .to_csv  ("vendas_att.csv"    , index = False, sep      = ";")

# bibliotecas selenium e pyautogui



