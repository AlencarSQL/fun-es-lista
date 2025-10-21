# QUESTÃO 1
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print(f"Resultado: {resultado}")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

# QUESTÃO 2
try:
    numero = int(input("Digite um número: "))
    print(f"Você digitou o número: {numero}")
except ValueError:
    print("Erro: Você não digitou um número válido!")

# QUESTÃO 3
try:
    entrada = input("Digite um número: ")
    valor = int(entrada)
    resultado = 100 / valor
    print(f"100 dividido por {valor} = {resultado}")
except ValueError:
    print("Erro: Entrada inválida, digite apenas números")
except ZeroDivisionError:
    print("Erro: Zero não pode ser usado como divisor")

# QUESTÇAO 4
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: não é possível dividir por zero"

num_a = float(input("Digite o primeiro número: "))
num_b = float(input("Digite o segundo número: "))
resultado_divisao = dividir(num_a, num_b)
print(f"Resultado: {resultado_divisao}")
