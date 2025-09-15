# Cardápio e Funções Principais do Código 

cardapio = [
    {"Nº": 1, "Prato": "Lamen", "Descricao": "Macarrão Japonês No Caldo", "Valor": 25.0},
    {"Nº": 2, "Prato": "Yakisoba", "Descricao": "Macarrão Com Legumes E Carne", "Valor": 30.0},
    {"Nº": 3, "Prato": "Guioza", "Descricao": "Pastelzinho Japonês Recheado", "Valor": 18.0},
    {"Nº": 4, "Prato": "Sushi", "Descricao": "Bolinho De Arroz Com Peixe Cru", "Valor": 28.0},
    {"Nº": 5, "Prato": "Sashimi", "Descricao": "Fatias Finas De Peixe Cru", "Valor": 32.0},
    {"Nº": 6, "Prato": "Temaki", "Descricao": "Cone De Alga Com Recheio", "Valor": 26.0},
    {"Nº": 7, "Prato": "Onigiri", "Descricao": "Bolinhos De Arroz Enrolados Em Alga", "Valor": 15.0},
    {"Nº": 8, "Prato": "Okonomiyaki", "Descricao": "Panqueca Japonesa Salgada", "Valor": 27.0},
    {"Nº": 9, "Prato": "Takoyaki", "Descricao": "Bolinhos Recheados Com Polvo", "Valor": 22.0},
    {"Nº": 10, "Prato": "Katsudon", "Descricao": "Tigela De Arroz Com Porco Empanado", "Valor": 35.0},
    {"Nº": 11, "Prato": "Tonkatsu", "Descricao": "Filé De Porco Empanado Crocante", "Valor": 33.0},
    {"Nº": 12, "Prato": "Donburi", "Descricao": "Arroz Com Diversas Coberturas", "Valor": 29.0},
    {"Nº": 13, "Prato": "Ramen Miso", "Descricao": "Lamen Com Caldo De Missô", "Valor": 31.0},
    {"Nº": 14, "Prato": "Udon", "Descricao": "Macarrão Grosso Servido No Caldo", "Valor": 24.0},
    {"Nº": 15, "Prato": "Tempurá", "Descricao": "Legumes E Frutos Do Mar Empanados", "Valor": 34.0},
    {"Nº": 16, "Prato": "Karaage", "Descricao": "Frango Frito Japonês Crocante", "Valor": 28.0},
    {"Nº": 17, "Prato": "Chahan", "Descricao": "Arroz Frito Estilo Japonês", "Valor": 20.0},
    {"Nº": 18, "Prato": "Mochi", "Descricao": "Doce Japonês De Arroz", "Valor": 12.0},
    {"Nº": 19, "Prato": "Dorayaki", "Descricao": "Panquecas Recheadas Com Doce De Feijão", "Valor": 14.0},
    {"Nº": 20, "Prato": "Matcha Latte", "Descricao": "Chá Verde Japonês Com Leite", "Valor": 16.0},
]

pedidos = {}
contador_pedido = 1

# 1. Função para Exibir o Cardápio: 

def menu_cardapio():
 print("=====[CARDÁPIO]=====")
 for item in cardapio:
  print(f"{item['Nº']} - {item["Prato"]} ({item["Descricao"]}) - R$ {item["Valor"]:.2f}")
 
# 2. Função para Registrar Pedidos: 

def registrar_pedido():
    global contador_pedido
    mesa = input("Mesa: ")
    garcom = input("Garçom: ")
    itens_pedido = []
    total = 0 

    while True:
     item_numero = int(input("Digite o Nº do item (0 para finalizar): "))
     if item_numero == 0:
      break 
     quantidade = int(input("Quantidade: "))

     item = next((i for i in cardapio if i["Nº"] == item_numero), None)

     if item:
      subtotal = item["Valor"] * quantidade
      itens_pedido.append({
        "Prato": item["Prato"],
        "Qtd": quantidade,
        "Valor": item["Valor"],
        "Subtotal": subtotal
     })
      total += subtotal
     else:
      print("Não encontrado.")

    pedidos[contador_pedido] = {
        "Mesa": mesa,
        "Garcom": garcom,
        "Itens": itens_pedido,
        "Total": total,
        "Status": "Aberto"
    }

    print(f"Pedido registrado com Nº {contador_pedido}")
    contador_pedido += 1

# 3. Função Fechar Conta

def fechar():
    pedido_id = int(input("Número do pedido: "))
    
    if pedido_id not in pedidos:
        print("Pedido não encontrado.")
        return 
    pedido = pedidos[pedido_id]

    print("\n=====[CONTA]=====")
    print(f"Pedido: {pedido_id}")
    print(f"Mesa: {pedido["Mesa"]}")
    print(f"Garçom: {pedido["Garcom"]}")
    print("\nPedidos:")

    for item in pedido["Itens"]:
        print(f"{item["Prato"]} x{item["Qtd"]} - R$ {item["Subtotal"]:.2f}")
    
    print(f"\nTOTAL: R$ {pedido["Total"]:.2f}")

    pedido["Status"] = "Fechado"
   
# Menu Oficial 

while True:
 print("\n=====[MENU]=====")
 print("1 - Cardápio")
 print("2 - Registrar pedido")
 print("3 - Fechar conta")
 print("0 - Sair")

 opcao = input("Escolha: ")
 if opcao == "1":
  menu_cardapio()
 elif opcao == "2":
  registrar_pedido()
 elif opcao == "3":
  fechar()
 elif opcao == "0":
  print("Encerrando...")
  break
 else:
  print("!!Selecione um opção Válida!!")