print("--- Relação entre Livro e Gênero ---")
id_livro = input("Digite o ID do livro: ")
id_genero = input("Digite o ID do gênero: ")

livros_generos = {
    "id_livro": id_livro,
    "id_genero": id_genero
}

print("\nRelação livro-gênero criada:")
print(livros_generos)