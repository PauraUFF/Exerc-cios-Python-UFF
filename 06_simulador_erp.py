usuarios = {
    "admin": "1234",
    "user1": "senha1"
}

usuario = input("Usuário: ")
senha = input("Senha: ")

if usuario in usuarios and usuarios[usuario] == senha:
    print("\nLogin realizado com sucesso!")
    print("Bem-vindo ao Sistema ERP")
    print("1. Consultar Estoque\n2. Emitir Nota\n3. Sair")
else:
    print("Usuário ou senha inválidos.")