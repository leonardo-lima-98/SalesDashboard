import pandas as pd
import uuid
import random
from faker import Faker

# Criar instância do Faker
fake = Faker(['pt_BR'])

# Dicionário de estados e siglas do Brasil
estados = {
    "Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM", "Bahia": "BA", "Ceará": "CE", "Distrito Federal": "DF", "Espírito Santo": "ES", "Goiás": "GO", "Maranhão": "MA", "Mato Grosso": "MT", "Mato Grosso do Sul": "MS", "Minas Gerais": "MG", "Pará": "PA", "Paraíba": "PB", "Paraná": "PR", "Pernambuco": "PE", "Piauí": "PI", "Rio de Janeiro": "RJ", "Rio Grande do Norte": "RN", "Rio Grande do Sul": "RS", "Rondônia": "RO", "Roraima": "RR", "Santa Catarina": "SC", "São Paulo": "SP", "Sergipe": "SE", "Tocantins": "TO"
}

# Criar dados para a tabela 'sales'
sales = []
for _ in range(5):  # Criando 20 vendas fictícias
    customer_id = str(uuid.uuid4())
    customer_name = fake.name()
    email = customer_name.lower().replace(" ", ".") + "@example.test.com"
    birthday = fake.date_of_birth(minimum_age=21, maximum_age=70)
    country = fake.current_country()
    state = random.choice(list(estados.keys()))
    state_abbr = estados[state]
    created_at = fake.date_time_between_dates(datetime_start='-3y', datetime_end='now')

    sales.append((customer_id, customer_name, email, birthday, country, state, state_abbr, created_at))

df = pd.DataFrame(sales)

# Imprimir o DataFrame (tabela formatada)
print(df)

# Listas de categorias de produtos
# categorias = ["Eletrônicos", "Roupas", "Calçados", "Acessórios", "Beleza", "Esportes", "Livros", "Brinquedos", "Móveis", "Alimentos"]

# def gerar_produto():
#     categoria = random.choice(categorias)  # Escolhe uma categoria aleatória
#     nome_produto = fake.sentence(nb_words=3)  # Nome do produto fictício
#     preco = round(random.uniform(10, 5000), 2)  # Preço entre R$10 e R$5000
#     estoque = random.randint(0, 500)  # Quantidade de estoque
#     descricao = fake.text(max_nb_chars=100)  # Descrição curta do produto
#     sku = fake.unique.bothify(text="SKU-#######")  # Código SKU único
#     avaliacao = round(random.uniform(1, 5), 1)  # Avaliação entre 1 e 5 estrelas
#     data_lancamento = fake.date_between(start_date="-2y", end_date="today")  # Data aleatória dos últimos 2 anos

#     return {
#         "nome": nome_produto,
#         "categoria": categoria,
#         "preco": preco,
#         "estoque": estoque,
#         "descricao": descricao,
#         "sku": sku,
#         "avaliacao": avaliacao,
#         "data_lancamento": data_lancamento
#     }

# # Gerar 10 produtos fictícios
# produtos_mock = [gerar_produto() for _ in range(10)]

# df = pd.DataFrame(produtos_mock)
# print(df)

# Exibir os produtos
# for produto in produtos_mock:
#     print(produto)