proximo_id = 1

print("--- Adicionar Meta de Leitura ---")
id_usuario = input("Digite o ID do usuário: ")
ano = input("Digite o ano da meta (Ex: 2024): ")
quantidade_desejada = input("Digite a quantidade de livros que você deseja ler: ")

id_meta = proximo_id
proximo_id += 1
quantidade_atual = 0  # Valor padrão para novas metas

meta = {
    "id_meta": id_meta,
    "id_usuario": id_usuario,
    "ano": ano,
    "quantidade_desejada": quantidade_desejada,
    "quantidade_atual": quantidade_atual
}

print("\nMeta de leitura criada:")
print(meta)