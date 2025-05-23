import db_connection as db_connection
import json
from sqlalchemy import select, func
from fast_zero.models import Product, Customer


def select_random_itens_to_purchase(qtd: int):
    session, engine = db_connection.open_connection()
    """Seleciona um número específico de registros aleatórios do banco."""
    stmt = select(Product).order_by(func.random()).limit(qtd)
    data = session.execute(stmt).scalars().all()
    produtos_dict = [p.to_dict() for p in data]
        
    db_connection.close_connection(session, engine)

    return(json.dumps(produtos_dict, indent=2))


def select_random_customer_to_purchase():
    session, engine = db_connection.open_connection()
    """Seleciona um número específico de registros aleatórios do banco."""
    stmt = select(Customer).order_by(func.random()).limit(1)
    data = session.execute(stmt).scalars().all()
    customer_dict = [p.to_dict() for p in data]
        
    db_connection.close_connection(session, engine)

    return(json.dumps(customer_dict, indent=2))


def insert_new_customer(customer: list):
    """Insere um novo cliente no banco de dados"""
    session, engine = db_connection.open_connection()
    
    session.add_all(customer)  # Agora adicionamos um objeto do modelo
    session.commit()  # Confirmando o insert
    print(f"✅ {len(customer)} Novos clientes inseridos com sucesso!") 

    db_connection.close_connection(session, engine)


def insert_purchase(purchase: list):
    """Insere o registro de compra no banco de dados"""
    session, engine = db_connection.open_connection()
    
    session.add_all(purchase)  # Adiciona a instância da compra ao banco
    session.commit()  # Comita a compra no banco
    print(f"✅ {len(purchase)} Novos registros de compra inserido com sucesso!")
    
    db_connection.close_connection(session, engine)