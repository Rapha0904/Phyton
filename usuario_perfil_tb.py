import re

print("--- Cadastro de Usuário ---")

proximo_id = 1

nome = input("Digite o nome do usuário: ")
email = input("Digite o email: ")
senha = input("Digite a senha: ")

while True:
    telefone_bruto = input("Digite o DDD e o número de telefone (ex: 41 99999-9999): ")
    telefone_limpo = re.sub(r'\D', '', telefone_bruto)
    
    if len(telefone_limpo) == 11:
        ddd = telefone_limpo[:2]
        numero = telefone_limpo[2:]
        telefone_formatado = f"{ddd}; {numero}"
        break
    else:
        print("Número inválido. Por favor, digite 11 dígitos (2 para o DDD e 9 para o número).")

caminho_foto = input("Digite o caminho da foto de perfil: ")

id_usuario = proximo_id
proximo_id += 1

usuario = {
    "id_usuario": id_usuario,
    "nome": nome,
    "email": email,
    "senha": senha,
    "telefone": telefone_formatado,
    "caminho_foto": caminho_foto
}

print("\nDados do usuário criados:")
print(usuario)
