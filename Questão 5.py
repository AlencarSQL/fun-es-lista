def calcular_imc(peso, altura):
    return peso / (altura ** 2)
def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc <= 24.9:
        return "Peso normal"
    else:
        return "Acima do peso"
pesopessoa = float(input("Digite o peso (kg): "))
alturapessoa = float(input("Digite a altura (m): "))
imc = calcular_imc(pesopessoa, alturapessoa)
classificacao = classificar_imc(imc)
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
