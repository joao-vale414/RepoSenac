print("============================")
print("    (: REFORMA FÁCIL :)     ")
print("PREENCHA O FORMÚLARIO ABAIXO")
print("============================")

while True: # Nome do Usuário
 nome = input("[Nome]: ") 
 if nome.replace(" ","").isalpha():
  nome = nome.title()
  break 
 else:
  print("Apenas letras! Digite de novo, por favor.")

while True: # Medidas do Cômodo 
 print("[Informe as medidas do cômodo (metros)]")
 entrada1 = input("Comprimento: ")
 entrada2 = input("Largura: ")
 entrada3 = input("Altura: ")
 try:
  comp = float(entrada1) 
  larg = float(entrada2) 
  alt = float(entrada3)
  break 
 except:
  print("ERROR! INFORME UM VALOR VÁLIDO") 

area = (2 * (comp * alt)) + (2* (larg * alt)) # Área em m² 
caixas = area / 1.5 # Quantidade de caixas utilizadas a cada 1,5 m²
print(f"Senhor(a) {nome}, com as medidas escolhidas calculamos que a área do comôdo é {area:.2f} m².")
print(f"Sendo necessária {caixas:.0f} caixas para revestir todas as paredes.")