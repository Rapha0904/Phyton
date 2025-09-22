print("--- Relação entre Livro e Autor ---")
id_livro = input("Digite o ID do livro: ")
id_autor = input("Digite o ID do autor: ")

livros_autores = {
    "id_livro": id_livro,
    "id_autor": id_autor
}

print("\nRelação livro-autor criada:")
print(livros_autores)