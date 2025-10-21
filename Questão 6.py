def adicionar_imposto(preco):
    return preco * 1.15
precoproduto = float(input("Digite o preço do produto: "))
precofinal = adicionar_imposto(precoproduto)
print(f"Preço final com imposto: R$ {precofinal:.2f}")
