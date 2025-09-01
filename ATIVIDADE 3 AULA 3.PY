print("===================================")
print("FORMULÁRIO DE MANUTENÇÃO DO VEÍCULO")
print("===================================")

while True: # Nome do Usuário
 nome = input("[Nome]: ") 
 if nome.replace(" ","").isalpha():
  nome = nome.title()
  break 
 else:
  print("Apenas letras! Digite de novo, por favor.")

while True: # Marcação Diária Odômetro
 entrada1 = input("[Marcação Odômetro DIA (km)]: ")
 entrada2 = input("[Marcação Odômetro NOITE (km)]: ")
 try:
  dia = float(entrada1)
  noite = float (entrada2)
  break
 except:
  print("!!INFORME UM VALOR VÁLIDO!!") 

while True: # Combustível Consumido
 entrada3 = input("[Combustível diário consumido (L)]: ")
 try:
  comb = float(entrada3)
  break
 except:
  print("!!INFORME UM VALOR VÁLIDO!!")

while True: # Lucro Diário
 entrada4 = input("[Lucro Diário (R$)]: ")
 try:
  lcr = float(entrada4)
  break
 except:
  print("!!INFORME UM VALOR VÁLIDO!!")

odo = (noite - dia) # Km rodados no dia
mediaconsumo = (odo / comb) # Km/L 
gasto = (mediaconsumo * 4.87) # Gasto do dia com combustível
lcrd = (lcr - gasto) # Lucro do dia

print(f"Senhor(a) {nome} seu carro tem uma média de consumo de {mediaconsumo:.2f} Km/L.")
print(f"Seu gasto com combustível no dia foi R$ {gasto:.2f}.")
print(f"E seu lucro diário foi R$ {lcrd:.2f}")