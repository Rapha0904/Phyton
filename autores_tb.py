proximo_id = 1

print("--- Informações do Autor ---")
nome_completo = input("Digite o nome completo do autor: ")
biografia = input("Digite a biografia do autor: ")

id_autor = proximo_id
proximo_id += 1

autor = {
    "id_autor": id_autor,
    "nome_completo": nome_completo,
    "biografia": biografia
}

print("\nDados do autor criados:")
print(autor)
