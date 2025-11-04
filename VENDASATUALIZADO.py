import pandas as pd 

vendas1  = pd.read_csv("venda 1.csv"   , sep = "," , encoding = "latin1")
vendas2  = pd.read_csv("venda 2.csv"   , sep = "," , encoding = "latin1")
vendas3  = pd.read_csv("venda 3.csv"   , sep = "," , encoding = "latin1")

vendas1["Data"] = vendas1["Data"].str.replace("00:00:00"," ")
vendas2["Data"] = vendas2["Data"].str.replace("00:00:00"," ")
vendas3["Data"] = vendas3["Data"].str.replace("00:00:00"," ")

vendas1["Valor_Total"] = vendas1["Valor_Total"].astype(str).apply(lambda x: x[:-2] + "." + x[-2:])
vendas2["Valor_Total"] = vendas2["Valor_Total"].astype(str).apply(lambda x: x[:-2] + "." + x[-2:])
vendas3["Valor_Total"] = vendas3["Valor_Total"].astype(str).apply(lambda x: x[:-2] + "." + x[-2:])

vendas1["Valor_Total"] = vendas1["Valor_Total"].astype(float)
vendas2["Valor_Total"] = vendas2["Valor_Total"].astype(float)
vendas3["Valor_Total"] = vendas3["Valor_Total"].astype(float)


vendas1.to_csv("Vendas1.csv", index = False, sep = ";")
vendas2.to_csv("Vendas2.csv", index = False, sep = ";")
vendas3.to_csv("Vendas3.csv", index = False, sep = ";")