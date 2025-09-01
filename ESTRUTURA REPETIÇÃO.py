# While Contador
'''contador = 1 
while contador <= 5:
 print(f"Contador: {contador}")
 contador += 1'''

#Validação com While
'''senha = ""
while senha != "1234":
 senha = input("Digite a senha: ").strip() #.strip() tira os espaços antes e depois.
 if senha == "1234":
  print("ACESSO LIBERADO")
 else:
  print("SENHA INCORRETA! DIGITE NOVAMENTE")'''

#Laço for com range() / Usado para repetir um bloco um número 
#range(1,10,2) -> começa no 1 vai até o 10 de 2 em 2 (1,3,5,7,9)
#range(5,0,-1) positivo se distanciando do zero negativo se aproximando (5 a 1)

for i in range(0,31,10):
 print(i)
 #RESULTADO: 0,1,2,3,4,5,6,7,8,9,10
 #Pode colocar a variavél que quiser no (i) pois ela vai mudando conforme o range segue
 

