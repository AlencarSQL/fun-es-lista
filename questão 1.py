def validar_login(email, senha):
    if email == 'admin' and senha == 'admin':
        return True
    return False
emailusuario = input("Digite o email: ")
senhausuario = input("Digite a senha: ")
if validar_login(emailusuario, senhausuario):
    print("Login realizado com sucesso!")
else:
    print("Email ou senha incorretos.")
