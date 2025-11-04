import pandas as pd

df_vendas    = pd.read_csv("vendas.csv"              , sep = ";", encoding = "latin1")
df_vendas1   = pd.read_csv("VendasAtualizado.csv"   , sep = ";", encoding = "latin1")

def clean_df(df):
    df = df.rename(columns = lambda x: x.strip().lower().replace(" ","_"))
    return df 

df_vendas     = clean_df (df_vendas)
df_vendas1    = clean_df (df_vendas1)

vendas = df_vendas.merge(df_vendas, on = "id_cliente").merge(df_vendas1, on = "id_produto").merge