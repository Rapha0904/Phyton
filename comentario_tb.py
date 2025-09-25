import datetime

proximo_id = 1

print("--- Adicionar Comentário ---")
id_usuario = input("Digite o seu ID de usuário: ")
id_resenha = input("Digite o ID da resenha que você está comentando: ")
id_entrada = input("Digite o ID da entrada do diário (se aplicável, caso contrário, deixe em branco): ")
conteudo_comentario = input("Digite o seu comentário: ")

id_comentario = proximo_id
proximo_id += 1
data_comentario = datetime.datetime.now()

comentario = {
    "id_comentario": id_comentario,
    "id_usuario": id_usuario,
    "id_resenha": id_resenha,
    "id_entrada": id_entrada if id_entrada else None,
    "conteudo_comentario": conteudo_comentario,
    "data_comentario": str(data_comentario)
}

print("\nComentário criado:")
print(comentario)
