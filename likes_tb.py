import datetime

proximo_id = 1

print("--- Adicionar Like ---")
id_usuario = input("Digite o ID do usuário que deu o like: ")
id_resenha = input("Digite o ID da resenha que recebeu o like (se aplicável): ")
id_comentario = input("Digite o ID do comentário que recebeu o like (se aplicável): ")

id_like = proximo_id
proximo_id += 1
data_like = datetime.datetime.now()

like = {
    "id_like": id_like,
    "id_usuario": id_usuario,
    "id_resenha": id_resenha if id_resenha else None,
    "id_comentario": id_comentario if id_comentario else None,
    "data_like": str(data_like)
}

print("\nLike registrado:")
print(like)
