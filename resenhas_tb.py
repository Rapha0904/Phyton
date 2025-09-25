import datetime

proximo_id = 1

print("--- Criar Resenha ---")
id_leitura = input("Digite o ID da leitura à qual a resenha se refere: ")
nota_leitor = input("Digite a nota (0.0 a 5.0): ")
titulo_resenha = input("Digite o título da resenha: ")
conteudo_resenha = input("Digite o conteúdo da resenha: ")

id_resenha = proximo_id
proximo_id += 1
data_publicacao = datetime.date.today()

resenha = {
    "id_resenha": id_resenha,
    "id_leitura": id_leitura,
    "nota_leitor": nota_leitor,
    "titulo_resenha": titulo_resenha,
    "conteudo_resenha": conteudo_resenha,
    "data_publicacao": str(data_publicacao)
}

print("\nResenha criada:")
print(resenha)

