import datetime

proximo_id = 1

print("--- Entrar em um Clube de Leitura ---")
id_usuario = input("Digite o seu ID de usuário: ")
id_clube = input("Digite o ID do clube que deseja entrar: ")

id_membro = proximo_id
proximo_id += 1
data_entrada = datetime.date.today()

membro = {
    "id_membro": id_membro,
    "id_usuario": id_usuario,
    "id_clube": id_clube,
    "data_entrada": str(data_entrada)
}

print("\nAssociação de membro criada:")
print(membro)
