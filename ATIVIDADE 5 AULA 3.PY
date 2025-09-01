print("======================")
print("?POSITIVO OU NEGATIVO?")
print("======================")

while True:
 n = input("[Informe seu número]: ")
 try:
  n1 = int(n)
  if n1 >= 0: 
   print(f"{n} é um número positivo.")
  elif n1 < 0:
   print(f"{n} é um número negativo.")
  break
 except:
  print("Valor Inválido(ERROR)")
 