import matplotlib.pyplot as plt
import pandas as pd

# A distribuição tem caudas similares às de uma distribuição normal.
meso  = [40, 41, 42, 44, 45, 46, 47, 48, 50, 51, 55, 52, 
         53, 51, 50, 48, 47, 46, 44, 42, 40]

# Indica que a distribuição tem caudas mais pesadas e mais outliers do que uma distribuição normal.
lepto = [45, 46, 47, 48, 49, 50, 50, 49, 48, 47, 46, 45, 45]

# Indica que a distribuição tem caudas mais leves e menos outliers do que uma distribuição normal.
plati = [45, 46, 47, 48, 49, 50, 49, 48, 47, 46, 45]

df_meso  = pd.DataFrame({"valores":meso})
df_lepto = pd.DataFrame({"valores":lepto})
df_plati = pd.DataFrame({"valores":plati})

assimetria_meso  = df_meso["valores"].skew()
curtose_meso     = df_meso["valores"].kurt()

assimetria_lepto = df_lepto["valores"].skew()
curtose_lepto    = df_lepto["valores"].kurt()

assimetria_plati = df_plati["valores"].skew()
curtose_plati    = df_plati["valores"].kurt()

plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.plot(df_meso.index, df_meso["valores"], marker = "o", color = "blue")
plt.title(f"Mesocúrtica{(curtose_meso)}")
plt.xlabel("Índice")
plt.ylabel("Valor")

plt.subplot(2, 3, 1)
plt.plot(df_meso.index, df_meso["valores"], marker = "o", color = "blue")
plt.title(f"Mesocúrtica{(curtose_meso)}")
plt.xlabel("Índice")
plt.ylabel("Valor")

plt.subplot(1, 3, 2)
plt.plot(df_lepto.index, df_lepto["valores"], marker = "o", color = "darkgreen")
plt.title(f"Leptocúrtica{(curtose_lepto * 100):.2f}")
plt.xlabel("Índice")
plt.ylabel("Valor")

plt.subplot(1, 3, 3)
plt.plot(df_plati.index, df_plati["valores"], marker = "o", color = "red")
plt.title(f"Platicúrtica{(curtose_plati * 100):.2f}")
plt.xlabel("Índice")
plt.ylabel("Valor")

plt.tight_layout()
plt.show()