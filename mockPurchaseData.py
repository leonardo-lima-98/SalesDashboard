import db_func
import uuid
import random
import json
from models import Purchase
from faker import Faker

# Criar instância do Faker
fake = Faker(['pt_BR'])

def gerar_numero():
    prob = random.random()  # PROB é a variavel de probabilidade com um número entre 0 e 1
    if prob < 0.55:  # 55% de chance
        return random.randint(1, 5)
    elif prob < 0.90:  # 35% de chance (50% + 35% = 85%)
        return random.randint(6, 10)
    else:  # 10% de chance (85% + 15% = 100%)
        return random.randint(11, 15)


def get_customer_to_purchase():
    customer_json_string = json.loads(db_func.select_random_customer_to_purchase())
    customer_id = customer_json_string[0]["id"]
    return customer_id

def get_itens_to_purchase():
    itens_json_string = json.loads(db_func.select_random_itens_to_purchase(gerar_numero()))
    item_data = [
        (item["id"], round(item["value"] * (1 - item["offer_percent"] / 100), 2) if item["on_offer"] else item["value"])
        for item in itens_json_string
    ]
    return item_data

def create_purchase(customer_id: str, item_data: list):
    """ Cria uma instância de Purchase para um cliente específico, associando os itens comprados. """
    purchase_id = str(uuid.uuid4())  # Gera um ID único para a compra
    purchase_date = fake.date_time_between_dates(datetime_start='-3y', datetime_end='now')  # Data da compra

    purchase = [
        Purchase(
            id=purchase_id,  # ID único para cada registro na tabela de compras
            customer_id=customer_id,
            product_id=item_id,
            purchase_date=purchase_date,
            purchase_value=item_value,
            coupon_used=False  # Define um valor fixo para esta simulação
        )
        for item_id, item_value in item_data
    ]

    return purchase  # Retorna uma lista de objetos Purchase

purchases = []
for _ in range(10):
    purchases.extend(create_purchase(get_customer_to_purchase(), get_itens_to_purchase()))

db_func.insert_purchase(purchases)