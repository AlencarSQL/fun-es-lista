def aplicar_desconto(preco):
    return preco * 0.9
precoproduto = float(input("Digite o preço do produto: "))
precofinal = aplicar_desconto(precoproduto)
print(f"Preço com desconto: R$ {precofinal:.2f}")
