print("====================")
print("? QUANTAS LÂMPADAS ?")
print("====================")

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

while True: # Potência em Watts
 entrada4 = input("Informe a potência por bocal (watts): ")
 try:
  watts = float(entrada4)
  break
 except:
  print("ERROR! INFORME UM VALOR VÁLIDO")

area = (2 * (comp * alt)) + (2* (larg * alt)) # Área em m² 
bocal = area / 3 # Quantidade de bocais 
pot_tot = bocal * 9 # Se são 3W por m² e 1 bocal a cada 3 m² o total de W por bocal é 9W
arredondado1 = round(bocal)
arredondado2 = round(pot_tot)
print(f"Senhor(ª) {nome}, a área do comôdo é {area:.1f} m² e serão necessários {arredondado1} bocais.")
print(f"A potência das lâmpadas escolhidas é {watts:.0f}W e a potência total necessária é {arredondado2}W.")