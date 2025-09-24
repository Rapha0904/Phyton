proximo_id = 1

print("--- Informações do Livro ---")
titulo = input("Digite o título do livro: ")
isbn = input("Digite o ISBN do livro: ")
ano_publicacao = input("Digite o ano de publicação: ")
numero_paginas = input("Digite o número de páginas: ")
editora = input("Digite a editora: ")
sinopse = input("Digite a sinopse: ")

id_livro = proximo_id
proximo_id += 1

livro = {
    "id_livro": id_livro,
    "titulo": titulo,
    "isbn": isbn,
    "ano_publicacao": ano_publicacao,
    "numero_paginas": numero_paginas,
    "editora": editora,
    "sinopse": sinopse
}

print("\nDados do livro criados:")
print(livro)
