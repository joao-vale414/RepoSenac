nome_produto = []
valor_produto = []
while True:
 try: 
  nome = input("[Digite o nome do produto]: ") 
  nome_produto.append(nome)
  valor = float(input("[Digite o valor do produto]: "))
  valor_produto.append(valor)
  sair = input("Deseja adicionar mais um item (S/N)? ").upper()
  if sair == "N":
   break 
 except:
  print("!ERROR!")

for i in range(len(nome_produto)): # len() retorna o comprimento de um objeto ou seja quantos itens tem nele
 print(f"O produto {nome_produto[i]} custa R${valor_produto[i]:.2f}")
