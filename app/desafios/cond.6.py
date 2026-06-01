#VERIFICAÇÃO DE ESTOQUE

estoque = int(input("Quantidade disponível em estoque: "))
pedido = int(input("Quantidade pedida: "))

if pedido > estoque:
    print("Estoque insuficiente.")
else:
    print("Pedido confirmado.")