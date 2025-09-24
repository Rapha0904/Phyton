import re

nome = input("Digite o nome do usuário: ")
email = input("Digite o email: ")
senha = input("Digite a senha: ")
ddd = input("Digite o DDD: ")
telefone = input("Digite o número de telefone: ")
caminho_foto = input("Digite o caminho da foto de perfil: ")

# Remove todos os caracteres não numéricos do telefone e do DDD.
ddd_limpo = re.sub(r'\D', '', ddd)
telefone_limpo = re.sub(r'\D', '', telefone)

# Combina o DDD e o número no formato "DDD; NUMERO".
telefone_formatado = f"{ddd_limpo}; {telefone_limpo}"

usuario = {
    "nome": nome,
    "email": email,
    "senha": senha,
    "telefone_formatado": telefone_formatado,
    "caminho_foto": caminho_foto
}

print("Dados do usuário criados:")
print(usuario)
