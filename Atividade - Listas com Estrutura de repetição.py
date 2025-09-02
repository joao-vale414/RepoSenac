nome_produto = []
while True:
 try: 
  nome = input("[Digite o nome do produto]: ") 
  nome_produto.append(nome)
  sair = input("Deseja adicionar mais um item (S/N)? ").upper()
  if sair == "N":
   break 
 except:
  print("!ERROR!")
