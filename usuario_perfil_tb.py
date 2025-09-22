nome = input("Digite o nome do usuário: ")
email = input("Digite o email: ")
senha = input("Digite a senha: ")
ddd = input("Digite o DDD: ")
telefone = input("Digite o número de telefone: ")
caminho_foto = input("Digite o caminho da foto de perfil: ")

usuario = {
    "nome": nome,
    "email": email,
    "senha": senha,
    "ddd": ddd,
    "telefone": telefone,
    "caminho_foto": caminho_foto
}

print("Dados do usuário criados:")
print(usuario)