import os
import uuid
import random
import time
import pandas as pd
from faker import Faker

# Criar instância do Faker
fake = Faker(['pt_BR'])
start_time = time.time()
df_customers = pd.read_csv("customers.csv")
df_products = pd.read_csv("products.csv")


def gerar_numero():
    prob = random.random()  # PROB é a variavel de probabilidade com um número entre 0 e 1
    if prob < 0.55:  # 55% de chance
        return random.randint(1, 5)
    elif prob < 0.90:  # 35% de chance (50% + 35% = 85%)
        return random.randint(6, 10)
    else:  # 10% de chance (85% + 15% = 100%)
        return random.randint(11, 15)


def get_customer_to_purchase():
    customer_id = df_customers.sample(n=1)["id"].values[0]
    return customer_id

def get_itens_to_purchase():
    # Selecionando um número aleatório de itens a partir da função gerar_numero()
    itens_json_string = df_products.sample(n=gerar_numero())  # seleciona itens aleatórios

    # Iterando sobre as linhas do DataFrame e aplicando o cálculo de valor com desconto, se necessário
    item_data = [
        (item[0], round(item[4] * (1 - item[6] / 100), 2) if item[5] else item[4])
        for _, item in itens_json_string.iterrows()  # Usando iterrows para acessar as linhas do DataFrame
    ]
    return item_data

def create_purchase(customer_id: str, item_data: list):
    """ Cria uma instância de Purchase para um cliente específico, associando os itens comprados. """
    purchase_id = str(uuid.uuid4())  # Gera um ID único para a compra
    purchase_date = fake.date_time_between_dates(datetime_start='-3y', datetime_end='now')  # Data da compra

    purchase = [
        (
            purchase_id,  # ID único para cada registro na tabela de compras
            customer_id, item_id,
            purchase_date, item_value,
            False  # Define um valor fixo para esta simulação
        )
        for item_id, item_value in item_data
    ]
    return purchase  # Retorna uma lista de objetos Purchase

# Criar lista de cliente
purchases = []
for _ in range(100000):  # Adicionando 5 compras
    purchases.extend(create_purchase(get_customer_to_purchase(), get_itens_to_purchase()))

# Transformar em DataFrame

data = pd.DataFrame([purchase for purchase in purchases])

# Exibir DataFrame
# print(data)

file_name = 'purchases.csv'

# Verifica se o arquivo já existe
if os.path.exists(file_name):
    # Se o arquivo já existe, faz append sem o cabeçalho
    data.to_csv(file_name, mode='a', header=False, index=False, encoding='utf-8')
else:
    # Se o arquivo não existe, cria e salva com o cabeçalho
    data.to_csv(file_name, mode='w', header=True, index=False, encoding='utf-8')

print("Dados adicionados com sucesso!")

end_time = time.time()

# Calcula o tempo de execução
execution_time = end_time - start_time

# Exibe o tempo de execução
print(f"Tempo de execução: {execution_time} segundos")