import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression  # pip install scikit-learn

# Criar DataFrame com dados

df = pd.DataFrame({"investimento_marketing" : [10, 20, 30, 40, 50, 60],
                   "vendas" : [100, 130, 160, 180, 210, 240]})

x = df[["investimento_marketing"]]
y = df["vendas"]

# Treinar Modelo

modelo = LinearRegression()
modelo.fit( x, y )

# Estender os dasdos para previsão até 

x_estendido = pd.DataFrame({"investimento_marketing" : [10, 20, 30, 40, 50, 60]})
y_pred      = modelo.predict(x_estendido)

# Visualizar 

plt.figure  (figsize=(8, 5 ))
plt.scatter (df["investimento_marketing"], df["vendas"], color = "green")
plt.plot    (x_estendido["investimento_marketing"], y_pred, color = "red")
plt.xlabel  ("Investimento em Marketing (mil R$)")
plt.ylabel  ("Vendas")
plt.title   ("Regressão Linear com Previsão até R$ 110 mil")
plt.show()