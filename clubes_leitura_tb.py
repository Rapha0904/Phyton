proximo_id = 1

print("--- Adicionar Clube de Leitura ---")
nome_clube = input("Digite o nome do clube de leitura: ")
descricao = input("Digite uma breve descrição do clube: ")
id_moderador = input("Digite o ID do moderador: ")

id_clube = proximo_id
proximo_id += 1

clube = {
    "id_clube": id_clube,
    "nome_clube": nome_clube,
    "descricao": descricao,
    "id_moderador": id_moderador
}

print("\nClube de leitura criado:")
print(clube)