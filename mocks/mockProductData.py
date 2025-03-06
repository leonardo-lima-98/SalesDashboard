import uuid
import random
import pandas as pd
# import db_func as db_func
from faker import Faker
from fast_zero.models import Product

# Criar instância do Faker
fake = Faker(['pt_BR'])

categorias = {
    'Categoria 1','Categoria 2','Categoria 3','Categoria 4','Categoria 5','Categoria 6','Categoria 7','Categoria 8','Categoria 9','Categoria 10','Categoria 11','Categoria 12','Categoria 13','Categoria 14','Categoria 15','Categoria 16','Categoria 17','Categoria 18','Categoria 19','Categoria 20','Categoria 21','Categoria 22','Categoria 23','Categoria 24','Categoria 25','Categoria 26','Categoria 27','Categoria 28','Categoria 29','Categoria 30'
}

def create_product(index: int):
    id = str(uuid.uuid4())
    product_name = f"Produto {index}"
    category = random.choice(list(categorias))
    description = f"Descrição {index}"
    value = fake.pyfloat(min_value=1, max_value=100, right_digits=2)
    on_offer = int(fake.random_int(min=0, max=1))
    offer_percent = None if on_offer == 0 else fake.random_int(min=1, max=22)

    return Product(
        id=id,
        name=product_name,
        category=category,
        description=description,
        value=value,
        on_offer=on_offer,
        offer_percent=offer_percent,
    )

# Criar lista de produtos
products = [create_product(x) for x in range(30000)]

# Transformar em DataFrame
data = pd.DataFrame([product.to_dict() for product in products])

# Exibir DataFrame
# print(data)
data.to_csv("products.csv", index=False, encoding="utf-8")
print("✅ Arquivo CSV gerado com sucesso!")