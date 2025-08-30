print("==================================")
print("Apresente as seguintes informações")
print("================================== \n")
while True: 
   largura = float(input("[Largura (metros)]: "))
   comprimento = float(input("[Comprimento (metros)]: "))
   pot = int(input("[Potência (watts)]: "))
   print("")
   if pot <3:
    print("Potência Mínima -> 3 watts")
   break
   
  