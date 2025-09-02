tupla = ("Joao" , 22 , "R$ 4800,50", "rua tavares nº 414") # TUPLAS () são váriaveis com múltiplos dados e são imutáveis (não mudam)
print(tupla)

lista = ["Joao" , 22 , "R$ 4800,50", "rua tavares nº 414"] # LISTAS [] 
print(lista[3]) # Vai printar o terceiro indice da lista (lembrando que a contagem sempre começa com 0), caso queira o 1º e 3º indice (nome[1:3])

telefone = 1234

lista.append(telefone) # lista.append() adiciona itens a lista
print(lista)

for i in lista: # Apresenta os dados da lista um embaixo do outro
 print(i)

lista = [] # Pode criar a lista sozinha e ir adicionando informações
while True:
 try:
  n = int(input("Digite um Nº: "))
  lista.append(n)
  sair = input("Deseja inserir outro número (S/N): ").upper() # Enquanto a resposta for sim o código se repete adicionando mais valores a lista
  if sair == "N":
    break
 except:
  print("Nº Inválido")

print(lista)

print("1\n2\n3\n4") # Estrutura simples para o usuário escolher um opção
while True:
 try:
  opcao = int(input("Escolha uma das opções: "))
  if opcao in [1,2,3,4]:
   break
  else: 
   print("OPÇÃO INVÁLIDA!")
 except:
  print("!ERROR!")

