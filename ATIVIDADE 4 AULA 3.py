print("=======================")
print(" PREENCHA O FORMULÁRIO ")
print("=======================")

while True:
 nome = input("[Nome]: ")
 if nome.replace(" ","").isalpha():
   nome = nome.title()
   break 
 else:
  print("Apenas letras! Digite de novo, por favor.")

while True:
 try:
  op = input("Você fez a avaliação optativa (S/N)? ").strip().upper()
  if op == "S":
    n1 = float(input("[Informe a nota da 1º avaliação]: "))
    n2 = float(input("[Informe a nota da 2º avaliação]: "))
    n3 = float(input("[Avaliação Optativa]: "))
    if n3 > n2 and n3 < n1:
     media = (n1 + n3) / 2
    elif n3 > n1 and n3 < n2:
     media = (n2 + n3) / 2
    elif n3 < n1 and n3 < n2:
     media = (n1 + n2) / 2
  elif op == "N":
    n1 = float(input("[Informe a nota da 1º avaliação]: "))
    n2 = float(input("[Informe a nota da 2º avaliação]: "))
    media = (n1 + n2) / 2
  break 
 except:
  print("Digite uma opção válida!") 

if media >= 6:
 print(f"Parabéns {nome} com média {media:.2f} você foi APROVADO!!")
elif media < 3:
 print(f"Infelizmente {nome}, sua média foi {media:.2f} e você está REPROVADO!!")
elif media >= 3 and media < 6:
 print(f"Quase lá {nome}, sua média foi {media:.2f} você está de RECUPERAÇÃO!!")