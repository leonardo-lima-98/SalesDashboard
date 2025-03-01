
import uuid
from faker import Faker
from random import choice, uniform

# Criar instância do Faker
fake = Faker()

# Criar dados para a tabela 'purchase'
purchases = []
for _ in range(10):  # Criando 10 produtos fictícios
    purchase_id = str(uuid.uuid4())
    item_id = str(uuid.uuid4())
    item_name = fake.word().capitalize()
    item_value = round(uniform(10, 500), 2)
    on_offer = fake.boolean()
    offer_percent = round(uniform(5, 50), 2) if on_offer else None

    purchases.append((purchase_id, item_id, item_name, item_value, on_offer, offer_percent))


# Criar dados para a tabela 'sales'
sales = []
for _ in range(20):  # Criando 20 vendas fictícias
    sale_id = str(uuid.uuid4())
    customer_id = str(uuid.uuid4())
    customer_name = fake.name()
    birthday = fake.date_of_birth(minimum_age=18, maximum_age=70)
    country = fake.country()
    state = fake.state()
    purchase = choice(purchases)  # Pegando um produto aleatório da tabela 'purchase'
    purchase_id = purchase[0]
    purchase_date = fake.date_this_decade()
    purchase_value = round(uniform(20, 1000), 2)
    coupon_used = fake.boolean()

    sales.append((sale_id, customer_id, customer_name, birthday, country, state, purchase_id, purchase_date, purchase_value, coupon_used))

print("Dados mockados inseridos com sucesso!")
