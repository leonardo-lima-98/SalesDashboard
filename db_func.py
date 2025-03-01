import db_connection
from sqlalchemy import select, func
from models import Base, Product

# Criar túnel SSH e sessão do banco
tunnel = db_connection.create_tunnel()
session, engine = db_connection.get_db_session(tunnel)

Base.metadata.create_all(engine)

def selecionar_aleatorio(qtd: int):
    """Seleciona um número específico de registros aleatórios do banco."""
    stmt = select(Product).order_by(func.random()).limit(qtd)
    resultados = session.execute(stmt).scalars().all()
    
    for resultado in resultados:
        print(resultado)
        
    db_connection.close_connection(session, engine, tunnel)