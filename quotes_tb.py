import datetime

proximo_id = 1

print("--- Adicionar Citação ---")
id_leitura = input("Digite o ID da leitura à qual a citação se refere: ")
texto_quote = input("Digite o texto da citação: ")
pagina_livro = input("Digite o número da página: ")

id_quote = proximo_id
proximo_id += 1
data_salvo = datetime.datetime.now()

quote = {
    "id_quote": id_quote,
    "id_leitura": id_leitura,
    "texto_quote": texto_quote,
    "pagina_livro": pagina_livro,
    "data_salvo": str(data_salvo)
}

print("\nCitação criada:")
print(quote)