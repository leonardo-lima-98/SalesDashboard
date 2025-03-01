import db_func
import random

def gerar_numero():
    prob = random.random()  # Gera um número entre 0 e 1

    if prob < 0.55:  # 50% de chance
        return random.randint(1, 5)
    elif prob < 0.90:  # 35% de chance (50% + 35% = 85%)
        return random.randint(6, 10)
    else:  # 15% de chance (85% + 15% = 100%)
        return random.randint(11, 15)

qtd = gerar_numero()
print(qtd) 
db_func.selecionar_aleatorio(qtd) 

