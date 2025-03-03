import uuid
import random
import db_func
from faker import Faker
from models import Customer

# Criar instância do Faker
fake = Faker(['pt_BR'])

# Dicionário de estados e siglas do Brasil
estados = {
    "Acre": "AC", "Alagoas": "AL", "Amapá": "AP", "Amazonas": "AM", "Bahia": "BA", "Ceará": "CE", "Distrito Federal": "DF", "Espírito Santo": "ES", "Goiás": "GO", "Maranhão": "MA", "Mato Grosso": "MT", "Mato Grosso do Sul": "MS", "Minas Gerais": "MG", "Pará": "PA", "Paraíba": "PB", "Paraná": "PR", "Pernambuco": "PE", "Piauí": "PI", "Rio de Janeiro": "RJ", "Rio Grande do Norte": "RN", "Rio Grande do Sul": "RS", "Rondônia": "RO", "Roraima": "RR", "Santa Catarina": "SC", "São Paulo": "SP", "Sergipe": "SE", "Tocantins": "TO"
}
def create_customer():
    id = str(uuid.uuid4())
    customer_name = fake.name()
    email = customer_name.lower().replace(" ", ".") + "@example.test.com"
    birthday = fake.date_of_birth(minimum_age=21, maximum_age=70)
    country = fake.current_country()
    state = random.choice(list(estados.keys()))
    state_abbr = estados[state]
    created_at = fake.date_time_between_dates(datetime_start='-3y', datetime_end='now')

    return Customer(
        id=id,
        name=customer_name,
        email=email,
        birthday=birthday,
        country=country,
        state=state,
        state_abbr=state_abbr,
        created_at=created_at,
    )

customer = []
for _ in range(4):
    customer.append(create_customer())
    
db_func.insert_new_customer(customer)
