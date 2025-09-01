while True:
 n = input("Digite um número maior que 10: ")
 try:
  n1 = int(n)
  if n1 <= 10:
   print("O valor tem que ser maior que 10.")
  elif n1 > 10:
   print(f"O Nº {n1} é maior que 10.")
  break
 except: 
  print("ERROR!")
