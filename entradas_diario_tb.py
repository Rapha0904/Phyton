import datetime

proximo_id = 1

print("--- Entrada de Diário de Leitura ---")
id_leitura = input("Digite o ID da leitura à qual esta entrada se refere: ")
conteudo = input("Digite o conteúdo da sua anotação: ")

id_entrada = proximo_id
proximo_id += 1
data_entrada = datetime.date.today()

entrada_diario = {
    "id_entrada": id_entrada,
    "id_leitura": id_leitura,
    "data_entrada": str(data_entrada),
    "conteudo": conteudo
}

print("\nEntrada de diário criada:")
print(entrada_diario)