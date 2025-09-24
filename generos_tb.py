proximo_id = 1

print("--- Informações de Gêneros ---")
nome_genero = input("Digite o nome do gênero: ")

id_genero = proximo_id
proximo_id += 1

genero = {
    "id_genero": id_genero,
    "nome_genero": nome_genero
}

print("\nDados do gênero criados:")
print(genero)
