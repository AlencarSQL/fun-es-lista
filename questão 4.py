def verificar_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    return "Menor de idade"
idadepessoa = int(input("Digite a idade: "))
resultado = verificar_idade(idadepessoa)
print(resultado)
